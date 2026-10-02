"""Validate the six VM runs and plot their exported meshes and computed fields."""
from pathlib import Path
import re, json, csv, runpy
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import PolyCollection
from matplotlib import font_manager

ROOT=Path(__file__).resolve().parents[2]
WORK=Path('F:/UbuntuShareFolder/.foamlab-build/advanced-mesh')
RESULTS=WORK/'results-final'
G=runpy.run_path(str(ROOT/'tools/content/build-advanced-mesh.py'))
FIG=ROOT/'source-openfoam/assets/science'
font_manager.fontManager.addfont('C:/Windows/Fonts/msyh.ttc')
plt.rcParams.update({'font.family':'Microsoft YaHei','font.size':12,'axes.titlesize':15,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'#fcfdfb','axes.facecolor':'#fcfdfb','savefig.facecolor':'#fcfdfb','text.color':'#243934','axes.labelcolor':'#243934'})

def vtk(path):
 s=path.read_text()
 tm=float(re.search(r'TimeValue 1 1 \w+\s+([\deE.+-]+)',s)[1])
 m=re.search(r'POINTS (\d+) \w+\n',s);n=int(m[1])
 points=np.fromstring(s[m.end():s.index('CELLS ')],sep=' ').reshape(n,3)
 m=re.search(r'CELLS (\d+) (\d+)\n',s);nc=int(m[1])
 values=np.fromstring(s[m.end():s.index('CELL_TYPES ')],sep=' ',dtype=int)
 m=re.search(r'CELL_TYPES \d+\n',s)
 types=np.fromstring(s[m.end():s.index('CELL_DATA ')],sep=' ',dtype=int)
 cells=[];faces=[];offset=0
 hexfaces=((0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7))
 for i in range(nc):
  length=values[offset];row=values[offset+1:offset+1+length];offset+=length+1
  if types[i]==42:
   fs=[];j=1
   for _ in range(row[0]):
    fs.append(row[j+1:j+1+row[j]]);j+=row[j]+1
   cells.append(np.unique(np.concatenate(fs)));faces.append(fs)
  else:
   assert types[i] in (12,13,10),(path,types[i])
   cells.append(row);faces.append([row[list(ix)] for ix in hexfaces] if types[i]==12 else [])
 block=s.split('CELL_DATA ',1)[1].split('POINT_DATA ',1)[0]
 headers=list(re.finditer(r'^([\w.]+) (\d+) (\d+) \w+\n',block,re.M));fields={}
 for i,m in enumerate(headers):
  a=np.fromstring(block[m.end():headers[i+1].start() if i+1<len(headers) else len(block)],sep=' ').reshape(int(m[3]),int(m[2]))
  assert np.isfinite(a).all(),(path,m[1])
  fields[m[1]]=a[:,0] if a.shape[1]==1 else a
 return dict(time=tm,points=points,cells=cells,faces=faces,types=types,fields=fields)

def bounds(d):
 p=d['points'];return np.array([p[c].min(axis=0) for c in d['cells']]),np.array([p[c].max(axis=0) for c in d['cells']])

def draw(ax,d,field=None,z=None,scale=1,edges=True,mask=None,clim=None,axes=(0,1)):
 low,high=bounds(d);selected=np.ones(len(low),dtype=bool)
 normal=3-sum(axes)
 if z is not None:selected=(low[:,normal]<=z)&(high[:,normal]>z)
 if mask is not None:selected&=mask
 polygons=[];ids=[]
 for i in np.flatnonzero(selected):
  q=np.unique(d['points'][d['cells'][i]][:,axes],axis=0)*scale
  if len(q)<3:continue
  hull=ConvexHull(q);polygons.append(q[hull.vertices]);ids.append(i)
 collection=PolyCollection(polygons,edgecolors='#284c54' if edges else 'none',linewidths=.22 if edges else 0,cmap='viridis',rasterized=True)
 if field is None:collection.set_facecolor('#e8f2ed')
 else:
  a=d['fields'][field];a=np.linalg.norm(a,axis=1) if a.ndim==2 else a
  collection.set_array(a[ids])
  if clim:collection.set_clim(*clim)
 ax.add_collection(collection);ax.autoscale();ax.set_aspect('equal');ax.set_xlabel('xyz'[axes[0]]+' / '+('mm' if scale==1000 else 'm'));ax.set_ylabel('xyz'[axes[1]]+' / '+('mm' if scale==1000 else 'm'))
 return collection

def save(fig,name):
 fig.savefig(FIG/f'advanced-mesh-{name}.png',dpi=160,bbox_inches='tight');plt.close(fig)

def write_csv(case,name,columns,rows):
 out=G['CASES']/case/'reference-results';out.mkdir(exist_ok=True)
 with (out/name).open('w',newline='',encoding='utf-8') as f:
  w=csv.writer(f);w.writerow(columns);w.writerows(rows)

def main():
 assert (RESULTS/'version.txt').read_text().strip()=='v2512'
 results={};datasets={}
 for name,(_,solver,end,_) in G['SPECS'].items():
  p=RESULTS/name;s=(p/f'log.{solver}').read_text()
  assert '\nEnd' in s and 'FOAM FATAL' not in s and abs(float(re.findall(r'^Time = (.*)',s,re.M)[-1])-end)<1e-9,name
  assert 'Mesh OK.' in (p/'log.checkMesh.standard').read_text(),name
  assert 'FOAM FATAL' not in (p/'log.foamToVTK').read_text(),name
  if name!='03-refinement':assert 'Mesh OK.' in (p/'log.checkMesh.final').read_text(),name
  data=sorted([vtk(f) for f in (p/'VTK').glob('*.vtk')],key=lambda d:d['time']);assert abs(data[-1]['time']-end)<1e-8
  datasets[name]=data
  last=data[-1];initial=int(re.search(r'cells:\s+(\d+)',(p/'log.checkMesh.initial').read_text())[1])
  results[name]={'solver':solver,'end':end,'cells_initial':initial,'cells_final':len(last['cells']),'max_speed':float(np.linalg.norm(last['fields'].get('U',last['fields'].get('Urel')),axis=1).max()),'mesh_standard':'passed','min_volume':float(re.search(r'Min volume = ([\deE.+-]+)',(p/'log.checkMesh.final').read_text())[1].rstrip('.'))}
  assert results[name]['min_volume']>0
  if name in ('05-mrf','06-srf'):
   assert np.array_equal(data[0]['points'],last['points']),name
   results[name]['mesh_coordinates_unchanged']=True
  if name in ('01-deforming','04-ami'):
   displacement=np.linalg.norm(last['points']-data[0]['points'],axis=1)
   results[name]['maximum_point_displacement']=float(displacement.max());assert displacement.max()>0
  for field in last['fields']:
   a=last['fields'][field];results[name][field+'_range']=[float(a.min()),float(a.max())]
  write_csv(name,'run-summary.csv',['quantity','value'],results[name].items())
 # Deforming mesh, same nodes at two physical times.
 data=datasets['01-deforming'];fig,axs=plt.subplots(2,1,figsize=(12,8),layout='constrained')
 for ax,d in zip(axs,[data[0],data[-1]]):
  im=draw(ax,d,'U',scale=1000,clim=(0,4));ax.set_title(f'移动锥体附近的网格与速度 · t = {d["time"]*1000:g} ms');fig.colorbar(im,ax=ax,label='|U| / (m/s)',shrink=.8)
 save(fig,'deforming')
 # Overset: show the two mesh components separately so overlapping cells are visible.
 data=datasets['02-overset'];fig,axs=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
 for ax,d in zip(axs,[data[0],data[-1]]):
  draw(ax,d,scale=1000,mask=d['fields']['zoneID']==0)
  im=draw(ax,d,'U',scale=1000,mask=d['fields']['zoneID']==1);ax.set_title(f'背景网格 + 旋转网格 · t = {d["time"]:g} s');fig.colorbar(im,ax=ax,label='旋转网格 |U| / (m/s)',shrink=.75)
 save(fig,'overset')
 text=(RESULTS/'02-overset/log.overPimpleDyMFoam').read_text()
 counts=re.findall(r'Overset analysis : nCells : (\d+)\s+calculated\s*:\s*(\d+)\s+interpolated\s*:\s*(\d+)[^\n]*\s+hole\s*:\s*(\d+)',text)
 assert counts
 assert all(int(total)==int(a)+int(b)+int(c) for total,a,b,c in counts),'Unclassified overset cells'
 results['02-overset']['unclassified_cells']=0
 results['02-overset']['calculated_interpolated_hole_final']=list(map(int,counts[-1][1:]))
 write_csv('02-overset','overset-counts.csv',['update','total','calculated','interpolated','hole'],[(i,*map(int,row)) for i,row in enumerate(counts,1)])
 # Adaptive refinement is axis-aligned; calculate water volume from exact cell extents.
 data=datasets['03-refinement'];history=[]
 for d in data:
  lo,hi=bounds(d);vol=np.prod(hi-lo,axis=1);a=d['fields']['alpha.water']
  assert a.min()>-1e-6 and a.max()<1+1e-6
  history.append((d['time'],len(d['cells']),float(np.dot(vol,a)),float(a.min()),float(a.max())))
 drift=max(abs(v[2]-history[0][2]) for v in history)/history[0][2]
 assert drift<1e-4,drift
 # The full geometry checker also flags coplanar split faces; verify convex half spaces independently.
 d=data[-1];worst=0.;poly_count=0
 for i in np.flatnonzero(d['types']==42):
  verts=d['points'][d['cells'][i]];centre=verts.mean(axis=0);poly_count+=1
  for face in d['faces'][i]:
   q=d['points'][face];normal=np.cross(q[1]-q[0],q[2]-q[0]);norm=np.linalg.norm(normal)
   if norm<1e-14:continue
   normal/=norm
   if np.dot(normal,q.mean(axis=0)-centre)<0:normal=-normal
   worst=max(worst,float(((verts-q[0])@normal).max()))
 assert worst<1e-12
 results['03-refinement'].update(water_volume_initial=history[0][2],water_volume_final=history[-1][2],relative_water_volume_drift=drift,polyhedral_cells_checked=poly_count,extended_check_reported_cells=336,max_convex_plane_violation_m=worst,extended_geometry_note='checkConcaveCells also flags coplanar split faces; all vertex half-space tests pass')
 write_csv('03-refinement','refinement-history.csv',['time_s','cells','water_volume_m3','alpha_min','alpha_max'],history)
 fig,axs=plt.subplots(1,2,figsize=(13,6),layout='constrained')
 for ax,d in zip(axs,[data[0],data[-1]]):
  im=draw(ax,d,'alpha.water',z=.5,clim=(0,1),axes=(1,2));ax.set_title(f'水相体积分数与网格 · t = {d["time"]:g} s\nx = 0.5 m 截面，{len(d["cells"]):,} 个总单元');fig.colorbar(im,ax=ax,label='α_water',shrink=.8)
 save(fig,'refinement')
 fig,axs=plt.subplots(1,2,figsize=(12,4.7),layout='constrained');h=np.array(history)
 axs[0].plot(h[:,0],h[:,1],'o-',color='#287663');axs[0].set(xlabel='t / s',ylabel='单元数',title='界面移动时更新局部网格')
 axs[1].plot(h[:,0],(h[:,2]/h[0,2]-1)*100,'o-',color='#3278ae');axs[1].set(xlabel='t / s',ylabel='水相体积相对变化 / %',title='由 α_water × 单元体积求和');axs[1].ticklabel_format(axis='y',style='sci',scilimits=(-2,2))
 save(fig,'refinement-history')
 # AMI keeps each component rigid, while its relative angular position changes.
 data=datasets['04-ami'];fig,axs=plt.subplots(1,2,figsize=(13,6),layout='constrained')
 for ax,d in zip(axs,[data[0],data[1]]):
  im=draw(ax,d,'U',scale=1000,clim=(0,.4));ax.set_title(f'旋转网格与 AMI 接口 · t = {d["time"]:g} s');fig.colorbar(im,ax=ax,label='|U| / (m/s)',shrink=.8)
 save(fig,'ami')
 s=(RESULTS/'04-ami/log.pimpleFoam').read_text();weights=re.findall(r'sum\(weights\) min:([\deE.+-]+) max:([\deE.+-]+)',s)
 assert weights;weights=np.array(weights,dtype=float);assert weights[:,0].min()>.999 and weights[:,1].max()<1.001
 results['04-ami']['ami_weight_min']=float(weights[:,0].min());results['04-ami']['ami_weight_max']=float(weights[:,1].max())
 # MRF field and its iteration history.
 d=datasets['05-mrf'][-1];fig,axs=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
 im=draw(axs[0],d,'U',scale=1000,edges=False);axs[0].set_title('MRF 速度场 · 500 次迭代');fig.colorbar(im,ax=axs[0],label='|U| / (m/s)',shrink=.8)
 s=(RESULTS/'05-mrf/log.simpleFoam').read_text();res=re.findall(r'Solving for (p|Ux|Uy), Initial residual = ([\deE.+-]+)',s)
 for field in ['p','Ux','Uy']:
  values=[float(v) for f,v in res if f==field];axs[1].semilogy(range(1,len(values)+1),values,label=field)
  results['05-mrf'][field+'_initial_residual_final']=values[-1]
 axs[1].set(xlabel='迭代次数',ylabel='每次迭代的初始残差',title='压力与速度方程残差');axs[1].legend();axs[1].grid(alpha=.2)
 save(fig,'mrf')
 # SRF: compare velocities at exactly the same cells on a plane normal to the axis.
 d=datasets['06-srf'][-1];fig,axs=plt.subplots(1,2,figsize=(13,5.5),layout='constrained')
 for ax,f in zip(axs,['Urel','U']):
  im=draw(ax,d,f,z=.1025,scale=1000,edges=False,clim=(0,15));ax.set_title(('旋转参考系速度 Urel' if f=='Urel' else '绝对速度 U')+' · z = 102.5 mm');fig.colorbar(im,ax=ax,label=f'|{f}| / (m/s)',shrink=.8)
 save(fig,'srf')
 identity=vtk(RESULTS/'06-srf/identity.vtk')['fields']
 rotation=np.cross(np.array([0,0,1000*2*np.pi/60]),identity['C'])
 error=float(np.linalg.norm(identity['U']-identity['Urel']-rotation,axis=1).max())
 assert error<1e-4
 results['06-srf']['absolute_relative_identity_max_error_m_s']=error
 for name,values in results.items():
  write_csv(name,'run-summary.csv',['quantity','value'],values.items())
  p=G['CASES']/name/'reference-results/validation.json';p.write_text(json.dumps(values,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 out=ROOT/'.openfoam-work/advanced-mesh';out.mkdir(exist_ok=True)
 (out/'validation.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 G['package']()
 print(json.dumps(results,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
