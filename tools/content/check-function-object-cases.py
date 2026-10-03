"""Check VM outputs, draw result figures and package the tested input files."""
from pathlib import Path
import tarfile,re,json,zipfile,hashlib,io,csv,runpy
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT=Path(__file__).resolve().parents[2]
G=runpy.run_path(str(ROOT/'tools/content/build-function-object-cases.py'))
WORK,CASES=G['WORK'],G['CASES']
FIG=ROOT/'source-openfoam/assets/science'
OUT=ROOT/'source-openfoam/downloads/function-objects'
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':11,'axes.titlesize':14,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#fcfdfb','axes.facecolor':'#fcfdfb','savefig.facecolor':'#fcfdfb','text.color':'#263b35','axes.labelcolor':'#263b35'})
T=tarfile.open(WORK/'results-linux.tar.gz')
def text(name):return T.extractfile('foamLabFunctionObjects/'+name).read().decode()
def data(name):
 s=text(name);s=re.sub(r'[()]',' ',s)
 return np.loadtxt(io.StringIO(s),comments='#',ndmin=2)
def field(name):
 s=text(name);m=re.search(r'internalField\s+nonuniform\s+List<\w+>\s+(\d+)\s*\((.*?)\)\s*;',s,re.S)
 assert m,name
 return np.fromstring(re.sub('[()]',' ',m[2]),sep=' ').reshape(int(m[1]),-1)
def save(fig,name):
 fig.savefig(FIG/f'functionobjects-{name}.png',dpi=160,bbox_inches='tight');plt.close(fig)
def main():
 assert (WORK/'run.log').read_text().count('PASS ')==5
 assert 'COMPLETE' in (WORK/'run.log').read_text()
 report={}
 for case,(_,solver,end,*_) in G['SPECS'].items():
  s=text(case+'/log.'+solver)
  assert '\nEnd' in s and 'FOAM FATAL' not in s and 'FOAM Warning' not in s,case
  assert abs(float(re.findall(r'^Time = (.+)',s,re.M)[-1])-end)<1e-8
  assert 'Mesh OK.' in text(case+'/log.checkMesh')
  for p in (CASES/case).rglob('*'):
   if p.is_file() and p.parts[-2]!='reference-results':
    try:actual=T.extractfile('foamLabFunctionObjects/'+case+'/'+p.relative_to(CASES/case).as_posix()).read()
    except KeyError:continue
    # setFields legitimately updates the initial alpha field; inputs in 0.orig are preserved.
    if not (case=='04-damBreak' and '/0/' in p.as_posix()):assert actual==p.read_bytes(),p
  report[case]={'solver':solver,'end':end,'mesh':'OK','function_objects':'strict errors; no function-object warnings'}
 for suffix in ('mag','grad','vorticity','vortex','dictionary'):
  s=text('01-cavity/log.postProcess.'+suffix);assert '\nEnd' in s and 'FOAM Warning' not in s and 'FOAM FATAL' not in s,suffix
 s=text('02-pitzDaily/log.solverPostProcess');assert '\nEnd' in s and 'FOAM Warning' not in s
 s=text('05-autoStop/log.icoFoam');assert 'Stopping calculation' in s and '\nEnd' in s
 report['05-autoStop']={'end':float(re.findall(r'^Time = (.+)',s,re.M)[-1])}
 # Each demonstrated output is required, including objects that could otherwise fail silently.
 required=['01-cavity/0.5/speed','01-cavity/0.5/gradU','01-cavity/0.5/vorticity','01-cavity/0.5/Q','01-cavity/0.5/Lambda2','01-cavity/0.5/kineticEnergy','01-cavity/0.5/UMean','01-cavity/0.5/UPrime2Mean','01-cavity/0.5/postSpeed','01-cavity/postProcessing/statistics/0/U.dat','01-cavity/postProcessing/speedHistogram/0/histogram.dat','01-cavity/postProcessing/sets/streamlines/0.5/track0.vtp','02-pitzDaily/100/yPlus','02-pitzDaily/100/wallShearStress','02-pitzDaily/postProcessing/pressureDrop/0/multiFieldValue.dat','03-hotRoom/0.2/htc','03-hotRoom/postProcessing/heatGauge/0/convective.dat','04-damBreak/postProcessing/freeSurface/0.2/waterAir.vtp']
 for name in required:assert len(text(name))>20,name
 # Spatial field, sampling positions and centre-line profile from the computed cavity.
 C=field('01-cavity/0.5/C');U=field('01-cavity/0.5/U');speed=np.linalg.norm(U,axis=1)
 x=np.unique(C[:,0]);y=np.unique(C[:,1]);order=np.lexsort((C[:,0],C[:,1]));u=U[order].reshape(len(y),len(x),3)
 fig,axs=plt.subplots(1,2,figsize=(12.5,5.1),layout='constrained')
 im=axs[0].pcolormesh(x,y,np.linalg.norm(u,axis=2),shading='nearest',cmap='viridis');fig.colorbar(im,ax=axs[0],label='速度大小 / (m/s)')
 axs[0].streamplot(x,y,u[:,:,0],u[:,:,1],color='#ffffffaa',density=.85,linewidth=.65,arrowsize=.7)
 axs[0].scatter([.05,.05],[.05,.075],s=42,color='#f7bc5d',edgecolors='white',zorder=4)
 axs[0].set(xlabel='x / m',ylabel='y / m',title='方腔速度与探针位置 · t = 0.5 s',aspect='equal')
 line=data('01-cavity/postProcessing/centreLines/0.5/vertical_p_U.xy')
 axs[1].plot(line[:,2],line[:,0],color='#287663',lw=2);axs[1].axvline(0,c='#ccd8d3',lw=1)
 axs[1].set(xlabel='水平速度 Ux / (m/s)',ylabel='y / m',title='中心竖线速度剖面 · x = 0.05 m');axs[1].grid(alpha=.2)
 save(fig,'sampling')
 probe=data('01-cavity/postProcessing/pointHistory/0/U')
 fig,axs=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
 axs[0].plot(probe[:,0],probe[:,1],label='探针 0：y = 0.05 m',c='#287663');axs[0].plot(probe[:,0],probe[:,4],label='探针 1：y = 0.075 m',c='#3d7bad');axs[0].legend()
 axs[0].set(xlabel='t / s',ylabel='Ux / (m/s)',title='两个位置的速度随时间变化')
 h=data('01-cavity/postProcessing/speedHistogram/0/histogram.dat');h=h[np.isclose(h[:,0],.5)]
 axs[1].bar(h[:,1],h[:,3],width=.085,color='#3d7bad');axs[1].set(xlabel='速度分箱中心 / (m/s)',ylabel='所占体积分数',title='速度分布直方图 · t = 0.5 s')
 for ax in axs:ax.grid(alpha=.15)
 save(fig,'statistics')
 fig,axs=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
 coeff=data('02-pitzDaily/postProcessing/wallCoefficients/0/coefficient.dat')
 axs[0].plot(coeff[:,0],coeff[:,1],label='Cd',c='#287663');axs[0].plot(coeff[:,0],coeff[:,4],label='Cl',c='#3d7bad');axs[0].legend();axs[0].set(xlabel='SIMPLE 迭代步',ylabel='力系数',title='后台阶壁面力系数')
 flow=[]
 for name,label in [('inletFlux','入口'),('outletFlux','出口')]:
  a=data('02-pitzDaily/postProcessing/'+name+'/0/surfaceFieldValue.dat');flow.append(a[-1,1]);axs[1].plot(a[:,0],a[:,1]*1e4,label=label)
 axs[1].set(xlabel='SIMPLE 迭代步',ylabel=r'有符号体积流量 / ($10^{-4}$ m³/s)',title='入口与出口的通量');axs[1].legend()
 for ax in axs:ax.grid(alpha=.2)
 save(fig,'forces');report['02-pitzDaily']['final_inlet_outlet_flux']=flow
 fig,axs=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
 heat=text('03-hotRoom/postProcessing/wallHeatFlux/0/wallHeatFlux.dat');heatrows=[l.split() for l in heat.splitlines() if l and not l.startswith('#')]
 for patch in ('floor','ceiling'):
  a=np.array([[float(r[0]),float(r[-1])] for r in heatrows if r[1]==patch]);axs[0].plot(a[:,0],a[:,1],'o-',label=patch)
 axs[0].legend();axs[0].set(xlabel='t / s',ylabel='壁面热流积分 / W',title='热量由底部进入，从顶部流出')
 gauge=np.loadtxt(io.StringIO(text('03-hotRoom/postProcessing/heatGauge/0/convective.dat')),comments='#',delimiter=',',ndmin=2)
 for i in (1,2):axs[1].plot(gauge[:,0],gauge[:,i],'o-',label='探针 '+str(i-1))
 axs[1].legend();axs[1].set(xlabel='t / s',ylabel='传感器对流热流 / (W/m²)',title='固定 300 K 传感器的预测读数')
 for ax in axs:ax.grid(alpha=.2)
 save(fig,'heat')
 fig,axs=plt.subplots(1,2,figsize=(12,4.5),layout='constrained')
 water=data('04-damBreak/postProcessing/waterVolume/0/volFieldValue.dat');height=data('04-damBreak/postProcessing/level/0/height.dat')
 drift=(water[:,1]/water[0,1]-1)*100
 axs[0].plot(water[:,0],drift,c='#287663');axs[0].set(xlabel='t / s',ylabel='水量相对变化 / %',title='溃坝过程中的水相体积');axs[0].ticklabel_format(axis='y',style='sci',scilimits=(-2,2))
 axs[1].plot(height[:,0],height[:,1],label='x = 0.1 m');axs[1].plot(height[:,0],height[:,3],label='x = 0.3 m');axs[1].legend();axs[1].set(xlabel='t / s',ylabel='等效液柱高度 / m',title='由相分数积分计算的液面高度')
 for ax in axs:ax.grid(alpha=.2)
 save(fig,'multiphase');report['04-damBreak']['relative_water_drift']=float(np.max(np.abs(drift))/100);assert report['04-damBreak']['relative_water_drift']<1e-5
 # Vorticity and Q: identical domain, genuinely computed fields, zero centred limits.
 fig,axs=plt.subplots(1,2,figsize=(12,4.9),layout='constrained')
 for ax,key,col,label in [(axs[0],'vorticity',2,r'$\omega_z$ / s$^{-1}$'),(axs[1],'Q',0,r'Q / s$^{-2}$')]:
  a=field('01-cavity/0.5/'+key)[order,col].reshape(len(y),len(x));lim=np.max(np.abs(a));im=ax.pcolormesh(x,y,a,shading='nearest',cmap='RdBu_r',vmin=-lim,vmax=lim);fig.colorbar(im,ax=ax,label=label);ax.set(xlabel='x / m',ylabel='y / m',aspect='equal',title=key+' · t = 0.5 s')
 save(fig,'vortex')
 # Include text reference outputs, not generated meshes or executable binaries.
 OUT.mkdir(parents=True,exist_ok=True);manifest={}
 for case in [*G['SPECS'],'05-autoStop']:
  p=OUT/(case+'.zip')
  with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED) as z:
   for f in sorted((CASES/case).rglob('*')):
    if f.is_file():z.write(f,case+'/'+f.relative_to(CASES/case).as_posix())
   for m in T.getmembers():
    prefix='foamLabFunctionObjects/'+case+'/postProcessing/'
    if m.isfile() and m.name.startswith(prefix) and (m.name.endswith('.dat') or '/pointHistory/' in m.name or '/centreLines/0.5/' in m.name):
     z.writestr(case+'/reference-results/'+m.name[len(prefix):],T.extractfile(m).read())
  manifest[case]={'url':'/downloads/function-objects/'+p.name,'bytes':p.stat().st_size,'size':f'{p.stat().st_size/1024:.0f} KB','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 with zipfile.ZipFile(OUT/'function-objects-v2512.zip','w',zipfile.ZIP_DEFLATED) as allz:
  for case in manifest:
   with zipfile.ZipFile(OUT/(case+'.zip')) as z:
    for name in z.namelist():allz.writestr(name,z.read(name))
 (OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 (ROOT/'tools/content/function-objects-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
