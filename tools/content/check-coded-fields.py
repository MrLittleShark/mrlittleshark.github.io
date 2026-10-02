"""Check VM results against prescribed fields and render the tutorial figures."""
from pathlib import Path
import re, json, csv, runpy
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT=Path(__file__).resolve().parents[2]
WORK=Path('F:/UbuntuShareFolder/.foamlab-build/coded-fields')
RESULTS=WORK/'results'
REF=WORK/'source/foamLabCodedFields/reference-results'
FIG=ROOT/'source-openfoam/assets/science'
REF.mkdir(parents=True,exist_ok=True); FIG.mkdir(parents=True,exist_ok=True)
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'axes.titlesize':15,'axes.labelsize':12,'axes.spines.top':False,'axes.spines.right':False,'axes.edgecolor':'#8da19a','axes.labelcolor':'#243934','text.color':'#243934','xtick.color':'#526b63','ytick.color':'#526b63','grid.color':'#dce5e0','grid.alpha':0.75,'figure.facecolor':'#fcfdfb','axes.facecolor':'#fcfdfb','savefig.facecolor':'#fcfdfb'})
GREEN='#2d715e';BLUE='#3278ae';GOLD='#bd8126'

def vtk(path, field):
    text=path.read_text()
    block=text.split('CELL_DATA ',1)[1].split('POINT_DATA ',1)[0]
    m=re.search(r'\b'+field+r'\s+(\d+)\s+(\d+)\s+\w+\s*\n',block)
    assert m, (path,field)
    dim,count=map(int,m.groups())
    a=np.fromstring(block[m.end():],sep=' ')[:dim*count].reshape(count,dim)
    assert np.isfinite(a).all()
    return a[:,0] if dim==1 else a

def field(path, name='internalField', dim=3):
    text=path.read_text()
    if name=='inlet':
        text=text.split('boundaryField',1)[1].split('inlet',1)[1]; name='value'
    m=re.search(r'\b'+name+r'\s+nonuniform\s+List<\w+>\s+(\d+)\s*\(',text)
    if m:
        count=int(m.group(1)); tail=text[m.end():].split(';',1)[0]
        a=np.fromstring(tail.replace('(',' ').replace(')',' '),sep=' ')[:count*dim]
        return a.reshape(count,dim) if dim>1 else a
    m=re.search(r'\b'+name+r'\s+uniform\s+([^;]+);',text)
    assert m,(path,name)
    return np.fromstring(m.group(1).replace('(',' ').replace(')',' '),sep=' ')

def series(base, name):
    files=list((base/'postProcessing'/name).glob('*/*Value.dat'))
    data=[]
    for p in files:
        for line in p.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith('#'):
                data.append([float(x) for x in line.replace('(',' ').replace(')',' ').split()])
    a=np.array(data); a=a[np.argsort(a[:,0])]
    assert len(a)>0 and np.isfinite(a).all(),(base,name)
    return a

def csv_save(name, cols, values):
    with (REF/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(cols); w.writerows(values)

def save(fig,name):
    fig.savefig(FIG/name,dpi=155,bbox_inches='tight');plt.close(fig)

def main():
    log=(WORK/'validation.log').read_text()
    names=sorted(p.name for p in RESULTS.iterdir() if p.is_dir())
    assert len(names)==9
    metrics={'version':'OpenFOAM v2512','cases':{},'advanced':{}}
    for name in names:
        assert f'PASS {name}' in log,name
        base=RESULTS/name
        assert 'Mesh OK.' in (base/'log.checkMesh').read_text(),name
        heat=int(name[:2])<=4; solver='laplacianFoam' if heat else 'icoFoam'
        solverlog=(base/f'log.{solver}').read_text()
        assert '\nEnd' in solverlog and 'FOAM FATAL' not in solverlog,name
        metrics['cases'][name]={'solver':solver,'mesh_cells':1600,'mesh_ok':True,'completed':True}
    # Heat cases: use exported cell values at time zero, saved fields at 0.2 s.
    X,Y=np.meshgrid((np.arange(80)+.5)*.1/80,(np.arange(20)+.5)*.02/20)
    expected=[np.full((20,80),300),300+20*X/.1,300+50*np.exp(-.5*(((X-.05)/.01)**2+((Y-.01)/.003)**2)),np.where(((X-.05)/.02)**2+((Y-.01)/.005)**2<=1,350,300)]
    initial=[]; final=[]
    for i,name in enumerate(names[:4]):
        a=vtk(RESULTS/name/'VTK'/f'{name}_0.vtk','T').reshape(20,80)
        b=field(RESULTS/name/'0.2/T',dim=1)
        if b.size==1:b=np.full(1600,b[0])
        b=b.reshape(20,80)
        assert np.max(np.abs(a-expected[i]))<5.1e-4,(name,'initial formula')
        ts=series(RESULTS/name,'meanTemperature')
        mean_err=float(np.max(np.abs(ts[:,1]-expected[i].mean())))
        assert mean_err<1e-7,(name,mean_err)
        assert b.min()>299.9999 and b.max()<350.0001
        metrics['cases'][name].update(initial_min=float(a.min()),initial_max=float(a.max()),final_min=float(b.min()),final_max=float(b.max()),initial_mean=float(expected[i].mean()),max_mean_temperature_drift=mean_err)
        csv_save(name+'-temperature.csv',['x_m','y_m','T_initial_K','T_0.2s_K'],zip(X.flat,Y.flat,a.flat,b.flat))
        initial.append(a);final.append(b)
    ellipse_fraction=float(np.mean(expected[3]>300))
    metrics['cases']['04-ellipse'].update(hot_cells=int(np.sum(expected[3]>300)),hot_area_m2=ellipse_fraction*.1*.02,analytical_area_m2=float(np.pi*.02*.005))
    fig,axs=plt.subplots(2,3,figsize=(15.5,5.4),layout='constrained')
    titles=['均匀温度','沿 x 方向的线性温度','高斯热斑']
    for col in range(3):
        for row,a in enumerate([initial[col],final[col]]):
            ax=axs[row,col];im=ax.imshow(a,origin='lower',extent=[0,100,0,20],aspect='equal',cmap='inferno',vmin=300,vmax=[301,320,350][col])
            if col==0:ax.text(50,10,'300 K',ha='center',va='center',color='white',fontsize=16)
            ax.set_title(titles[col]+(' · t = 0 s' if row==0 else ' · t = 0.2 s'));ax.set_xlabel('x / mm');ax.set_ylabel('y / mm')
            fig.colorbar(im,ax=ax,label='T / K',fraction=.035,pad=.025)
    save(fig,'coded-fields-temperature.png')
    fig,axs=plt.subplots(2,1,figsize=(12,6.7),layout='constrained')
    for i,ax in enumerate(axs):
        im=ax.imshow([initial[3],final[3]][i],origin='lower',extent=[0,100,0,20],aspect='equal',cmap='inferno',vmin=300,vmax=350)
        ax.set_title(['按单元中心选择椭圆热区 · t = 0 s','绝热扩散 · t = 0.2 s'][i]);ax.set_xlabel('x / mm');ax.set_ylabel('y / mm')
        if i==0:
            theta=np.linspace(0,2*np.pi,300);ax.plot(50+20*np.cos(theta),10+5*np.sin(theta),'--',color='#68dbd1',lw=2,label='解析椭圆');ax.legend(loc='upper right')
        fig.colorbar(im,ax=ax,label='T / K',fraction=.03,pad=.025)
    save(fig,'coded-fields-ellipse.png')
    y=(np.arange(20)+.5)*.01/20; g=4*(y/.01)*(1-y/.01)
    profiles={}
    for name in names[4:]:
        base=RESULTS/name; ts=series(base,'inletMean'); t=ts[:,0]
        if name in ['05-fixed-profile','06-coded-steady']: expect=np.full(len(t),.15*g.mean())
        elif name=='07-ramp':expect=.1*np.minimum(t/.2,1)
        else:expect=.1*(1+.5*np.sin(2*np.pi*t))
        err=float(np.max(np.abs(ts[:,1]-expect)));assert err<1e-10,(name,err)
        inf=series(base,'inletFlux');outf=series(base,'outletFlux')
        assert np.allclose(inf[:,0],outf[:,0])
        imbalance=float(np.max(np.abs(inf[:,1]+outf[:,1])))
        assert imbalance<1e-10,(name,imbalance)
        prof=field(base/'1/U',name='inlet');profiles[name]=prof[:,0] if prof.ndim==2 else np.full(20,prof[0])
        metrics['cases'][name].update(max_mean_velocity_error=err,max_flow_imbalance_m3_s=imbalance)
        csv_save(name+'-history.csv',['t_s','mean_Ux_m_s','inlet_flux_m3_s','outlet_flux_m3_s'],zip(t,ts[:,1],inf[:,1],outf[:,1]))
    # Fixed inlet: inlet sample positions and final computed field.
    fig,axs=plt.subplots(1,2,figsize=(14,5.4),layout='constrained')
    smooth=np.linspace(0,.01,300)
    axs[0].plot(.15*4*(smooth/.01)*(1-smooth/.01),smooth*1000,color=GREEN,lw=2,label='解析抛物线')
    axs[0].scatter(profiles['05-fixed-profile'],y*1000,s=32,facecolors='white',edgecolors=BLUE,zorder=3,label='入口面中心值')
    axs[0].set(xlabel='Ux / (m/s)',ylabel='y / mm',title='固定入口剖面');axs[0].legend();axs[0].grid()
    u=field(RESULTS/'05-fixed-profile/1/U')[:,0].reshape(20,80)
    im=axs[1].imshow(u,origin='lower',extent=[0,100,0,10],aspect='equal',cmap='viridis',vmin=0,vmax=.15)
    axs[1].set(xlabel='x / mm',ylabel='y / mm',title='通道速度场 · t = 1 s');fig.colorbar(im,ax=axs[1],label='Ux / (m/s)',fraction=.035)
    save(fig,'coded-fields-fixed.png')
    a=field(RESULTS/'05-fixed-profile/1/U');b=field(RESULTS/'06-coded-steady/1/U')
    metrics['comparison_fixed_implementations_max_U_difference']=float(np.max(np.abs(a-b)))
    assert np.max(np.abs(a-b))<1e-8
    fig,axs=plt.subplots(1,2,figsize=(14,5.4),layout='constrained')
    axs[0].plot(profiles['05-fixed-profile'],y*1000,color=GREEN,lw=2,label='fixedValue + codeStream')
    axs[0].scatter(profiles['06-coded-steady'],y*1000,facecolors='none',edgecolors=GOLD,s=46,label='codedFixedValue',zorder=3)
    axs[0].set(xlabel='Ux / (m/s)',ylabel='y / mm',title='相同空间公式，入口结果重合');axs[0].legend();axs[0].grid()
    for name,color,style in [('05-fixed-profile',GREEN,'-'),('06-coded-steady',GOLD,'--')]:
        ts=series(RESULTS/name,'inletMean');axs[1].plot(ts[:,0],ts[:,1],color=color,ls=style,lw=2,label=name.split('-',1)[1])
    axs[1].set(xlabel='t / s',ylabel='平均 Ux / (m/s)',title='固定公式保持恒定的入口平均速度',ylim=(.095,.105));axs[1].legend();axs[1].grid()
    save(fig,'coded-fields-steady.png')
    fig,axs=plt.subplots(1,2,figsize=(14,5),layout='constrained')
    t=np.linspace(0,1,501)
    for i,name in enumerate(['07-ramp','08-sine']):
        expect=.1*np.minimum(t/.2,1) if i==0 else .1*(1+.5*np.sin(2*np.pi*t))
        ts=series(RESULTS/name,'inletMean')
        axs[i].plot(t,expect,color=GREEN,lw=2,label='设定时间函数')
        axs[i].scatter(ts[::25,0],ts[::25,1],facecolors='white',edgecolors=BLUE,s=23,label='v2512 输出',zorder=3)
        axs[i].set(xlabel='t / s',ylabel='入口平均 Ux / (m/s)',title=['0.2 s 线性启动','1 Hz 正弦脉动'][i]);axs[i].grid();axs[i].legend()
    save(fig,'coded-fields-time.png')
    fig,axs=plt.subplots(1,2,figsize=(14,5.4),layout='constrained')
    ts=series(RESULTS/'09-pulsed-profile','inletMean')
    axs[0].plot(t,.1*(1+.5*np.sin(2*np.pi*t)),color=GREEN,lw=2,label='设定平均速度')
    axs[0].scatter(ts[::25,0],ts[::25,1],facecolors='white',edgecolors=BLUE,s=23,label='v2512 输出',zorder=3)
    axs[0].set(xlabel='t / s',ylabel='入口平均 Ux / (m/s)',title='面积归一化后的入口均值');axs[0].grid();axs[0].legend()
    for tm,color in [('0.25',GOLD),('0.5',GREEN),('0.75',BLUE)]:
        prof=field(RESULTS/'09-pulsed-profile'/tm/'U',name='inlet')[:,0]
        axs[1].plot(prof,y*1000,'o-',color=color,ms=4,label=f't = {tm} s')
        csv_save('09-profile-'+tm+'.csv',['y_m','Ux_m_s'],zip(y,prof))
    axs[1].set(xlabel='Ux / (m/s)',ylabel='y / mm',title='三个时刻的离散入口剖面');axs[1].grid();axs[1].legend()
    save(fig,'coded-fields-pulsed.png')
    advanced=(WORK/'advanced.log').read_text()
    assert all(x in advanced for x in ['RESTART_PASS','PARALLEL_PASS','ZERO_AMPLITUDE_PASS'])
    restart=field(WORK/'advanced/restart/1.25/U',name='inlet')[:,0]
    assert abs(restart.mean()-.15)<1e-10
    serial=field(RESULTS/'09-pulsed-profile/1/U');parallel=field(WORK/'advanced/parallel/1/U')
    pe=float(np.max(np.abs(serial-parallel)));assert pe<1e-7
    zero=series(WORK/'advanced/steady','inletMean');ze=float(np.max(np.abs(zero[:,1]-.1)));assert ze<1e-10
    metrics['advanced']={'restart_1.25s_mean_Ux':float(restart.mean()),'parallel_processes':2,'parallel_max_U_difference':pe,'zero_amplitude_max_mean_error':ze}
    (REF/'metrics.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (ROOT/'tools/content/coded-fields-validation.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    runpy.run_path(str(ROOT/'tools/content/build-coded-fields.py'))['package']()
    print(json.dumps(metrics,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
