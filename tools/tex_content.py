"""Conservative conversion of imported scientific prose to explicit TeX.

This module is called only for prose/table cells, never for executable code.
Known compound formulae are curated; the fallback preserves linear notation.
"""
import html,re,unicodedata

SPECIAL={
 'R ∝ t^1/2':r'R\propto t^{1/2}',
 'R ∝ t^1/3':r'R\propto t^{1/3}',
 'Δt ≲ √(ρ̄Δx³/(2πσ))':r'\Delta t\lesssim\sqrt{\frac{\bar\rho\Delta x^3}{2\pi\sigma}}',
 'V_P(T_P^{n+1}−T_P^n)/Δt+Σ_f F_f=S_PV_P':r'\frac{V_P(T_P^{n+1}-T_P^n)}{\Delta t}+\sum_f F_f=S_P V_P',
 'I全=(2π/Δθ)I楔':r'I_{\mathrm{full}}=\frac{2\pi}{\Delta\theta}I_{\mathrm{wedge}}',
 'ρ=αρ水+(1−α)ρ气':r'\rho=\alpha\rho_{\mathrm{water}}+(1-\alpha)\rho_{\mathrm{gas}}',
 'V水=ΣαᵢVᵢ':r'V_{\mathrm{water}}=\sum_i\alpha_i V_i',
 'y气=Σ[(1−αᵢ)Vᵢyᵢ]/Σ[(1−αᵢ)Vᵢ]':r'y_{\mathrm{gas}}=\frac{\sum_i(1-\alpha_i)V_i y_i}{\sum_i(1-\alpha_i)V_i}',
 'I楔=Δθ∫∫fr dr dy':r'I_{\mathrm{wedge}}=\Delta\theta\iint f r\,\mathrm{d}r\,\mathrm{d}y',
 'I全=2π∫∫fr dr dy':r'I_{\mathrm{full}}=2\pi\iint f r\,\mathrm{d}r\,\mathrm{d}y',
 'ψ平衡=0.4/0.6=2/3':r'\psi_{\mathrm{eq}}=\frac{0.4}{0.6}=\frac{2}{3}',
 'c平均':r'\overline{c}',
 '∂U/∂t+∇·(UU)=−∇p+ν∇²U':r'\frac{\partial\boldsymbol U}{\partial t}+\nabla\cdot(\boldsymbol U\boldsymbol U)=-\nabla p+\nu\nabla^2\boldsymbol U',
 '∂U/∂t+∇·(UU)=−∇pₖ+ν∇²U+S':r'\frac{\partial\boldsymbol U}{\partial t}+\nabla\cdot(\boldsymbol U\boldsymbol U)=-\nabla p_k+\nu\nabla^2\boldsymbol U+\boldsymbol S',
 '∂α/∂t+∇·(αU)=0':r'\frac{\partial\alpha}{\partial t}+\nabla\cdot(\alpha\boldsymbol U)=0',
 '∂α/∂t+∇·(Uα)=0':r'\frac{\partial\alpha}{\partial t}+\nabla\cdot(\boldsymbol U\alpha)=0',
 '∂T/∂t+∇·(UT)=∇·(D∇T)+S':r'\frac{\partial T}{\partial t}+\nabla\cdot(\boldsymbol U T)=\nabla\cdot(D\nabla T)+S',
 '∂c/∂t+∇·(Uc)=D∇²c':r'\frac{\partial c}{\partial t}+\nabla\cdot(\boldsymbol U c)=D\nabla^2c',
 '∂T/∂t+U∂T/∂x=0':r'\frac{\partial T}{\partial t}+U\frac{\partial T}{\partial x}=0',
 '∂c/∂t=D∂²c/∂y²':r'\frac{\partial c}{\partial t}=D\frac{\partial^2 c}{\partial y^2}',
 '∂cGas/∂t+∇·(UcGas)−∇·(DGas∇cGas)=0':r'\frac{\partial c_{\mathrm{Gas}}}{\partial t}+\nabla\cdot(\boldsymbol U c_{\mathrm{Gas}})-\nabla\cdot(D_{\mathrm{Gas}}\nabla c_{\mathrm{Gas}})=0',
 'H∂ψ/∂t=∂(DH∂ψ/∂x)/∂x':r'H\frac{\partial\psi}{\partial t}=\frac{\partial}{\partial x}\left(DH\frac{\partial\psi}{\partial x}\right)',
 'ρCp(∂T/∂t+U·∇T)=∇·(k∇T)+qv':r'\rho C_p\left(\frac{\partial T}{\partial t}+\boldsymbol U\cdot\nabla T\right)=\nabla\cdot(k\nabla T)+q_v',
 'k_f∂T_f/∂n_f+k_s∂T_s/∂n_s=0':r'k_f\frac{\partial T_f}{\partial n_f}+k_s\frac{\partial T_s}{\partial n_s}=0',
 'Co = |U|Δt/Δx':r'\mathrm{Co}=\frac{|\boldsymbol U|\Delta t}{\Delta x}',
 'Co=UΔt/Δx':r'\mathrm{Co}=\frac{U\Delta t}{\Delta x}',
 'Co=U*deltaT/dx':r'\mathrm{Co}=\frac{U\Delta t}{\Delta x}',
 'Re=UL/ν':r'\mathrm{Re}=\frac{UL}{\nu}',
 'Re=UD/ν':r'\mathrm{Re}=\frac{UD}{\nu}',
 'ν=UL/Re':r'\nu=\frac{UL}{\mathrm{Re}}',
 'Δp = 2σ/R':r'\Delta p=\frac{2\sigma}{R}',
 'Δp=2σ/R':r'\Delta p=\frac{2\sigma}{R}',
 'Δp=σ/R':r'\Delta p=\frac{\sigma}{R}',
 'Cd=Fx/(0.5ρU²A)':r'C_d=\frac{F_x}{\tfrac12\rho U^2 A}',
 'St=fD/U':r'\mathrm{St}=\frac{fD}{U}',
 'c(y,t)=2N√[t/(πD)]exp[−y²/(4Dt)]−(Ny/D)erfc[y/(2√Dt)]':r'c(y,t)=2N\sqrt{\frac{t}{\pi D}}\exp\left(-\frac{y^2}{4Dt}\right)-\frac{Ny}{D}\operatorname{erfc}\left(\frac{y}{2\sqrt{Dt}}\right)',
 'c(0,t) = 2N√(t/(πD))':r'c(0,t)=2N\sqrt{\frac{t}{\pi D}}',
 'cwall=2N√[t/(πD)]':r'c_{\mathrm{wall}}=2N\sqrt{\frac{t}{\pi D}}',
 '2N√[t/(πD)]':r'2N\sqrt{\frac{t}{\pi D}}',
 'cs=2J0√(t/πD)':r'c_s=2J_0\sqrt{\frac{t}{\pi D}}',
 'N=j/(zF)':r'N=\frac{j}{zF}',
 'Q=ṅRT/pg':r'Q=\frac{\dot nRT}{p_g}',
 'Q=ηgjAeRT/(zFpg)':r'Q=\frac{\eta_g j A_e RT}{zFp_g}',
 'Q=eta IRT/(zFp_abs)':r'Q=\frac{\eta IRT}{zF p_{\mathrm{abs}}}',
 'Uin=Q/Ain':r'U_{\mathrm{in}}=\frac{Q}{A_{\mathrm{in}}}',
 'εV=|Vnum−(V0+Qt)|/(V0+Qt)':r'\varepsilon_V=\frac{|V_{\mathrm{num}}-(V_0+Qt)|}{V_0+Qt}',
 'Dd=0.0208θ√[σ/(gΔρ)]':r'D_d=0.0208\theta\sqrt{\frac{\sigma}{g\Delta\rho}}',
 'R_eq=(3V_g/4π)^(1/3)':r'R_{\mathrm{eq}}=\left(\frac{3V_g}{4\pi}\right)^{1/3}',
 'Rv=(3Vg/4π)^(1/3)':r'R_v=\left(\frac{3V_g}{4\pi}\right)^{1/3}',
 'Req=(3Vg/4π)^(1/3)':r'R_{\mathrm{eq}}=\left(\frac{3V_g}{4\pi}\right)^{1/3}',
 '∇sσ=(I−nn)∇σ':r'\nabla_s\sigma=(\boldsymbol I-\boldsymbol n\boldsymbol n)\nabla\sigma',
 '∇·U=0':r'\nabla\cdot\boldsymbol U=0',
 'div(U)=0':r'\nabla\cdot\boldsymbol U=0',
 '∇·(κ∇φ)=0':r'\nabla\cdot(\kappa\nabla\varphi)=0',
 'div(kappa grad(Velec))=0':r'\nabla\cdot(\kappa\nabla V_{\mathrm{elec}})=0',
 'i=−kappa grad(Velec)':r'\boldsymbol i=-\kappa\nabla V_{\mathrm{elec}}',
 'I=−integral(i·n dA)':r'I=-\int\boldsymbol i\cdot\boldsymbol n\,\mathrm{d}A',
 'kappa_f=1/interpolate(1/kappa)':r'\kappa_f=\frac{1}{\operatorname{interpolate}(1/\kappa)}',
 'C^(n+1)=C^n+I_applied^n Δt':r'C^{n+1}=C^n+I_{\mathrm{applied}}^n\Delta t',
 'V_expected=V0+eta RT C/(zFp)':r'V_{\mathrm{expected}}=V_0+\frac{\eta RTC}{zFp}',
 'Vexpected=V0+ηRT/(zFp)∫Iapplied dt':r'V_{\mathrm{expected}}=V_0+\frac{\eta RT}{zFp}\int I_{\mathrm{applied}}\,\mathrm{d}t',
 'k = 1.5*(I*U)^2':r'k=1.5(IU)^2',
 'epsilon = Cmu^0.75*k^1.5/L':r'\varepsilon=\frac{C_\mu^{0.75}k^{1.5}}{L}',
 'omega = sqrt(k)/(Cmu^0.25*L)':r'\omega=\frac{\sqrt{k}}{C_\mu^{0.25}L}',
 'ε = Cμ^0.75 · k^1.5 / l':r'\varepsilon=\frac{C_\mu^{0.75}k^{1.5}}{l}',
 'ω = k^0.5 / (Cμ^0.25 · l)':r'\omega=\frac{k^{0.5}}{C_\mu^{0.25}l}',
 'p_rgh = p - rho*gh':r'p_{\mathrm{rgh}}=p-\rho gh',
 'p_rgh = p − ρg·h':r'p_{\mathrm{rgh}}=p-\rho\boldsymbol g\cdot\boldsymbol h',
 "R_s''=δ_s/k_s":r"R_s''=\frac{\delta_s}{k_s}",
}
GREEK=dict(zip('αβγδεζηθικλμνξπρστυφχψωΔΓΘΛΠΣΦΨΩ',
 'alpha beta gamma delta varepsilon zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon varphi chi psi omega Delta Gamma Theta Lambda Pi sum Phi Psi Omega'.split()))
SYMBOLS={'∂':r'\partial ','∇':r'\nabla ','∫':r'\int ','∮':r'\oint ','∑':r'\sum ','∞':r'\infty ','≤':r'\le ','≥':r'\ge ','≠':r'\ne ','≈':r'\approx ','∝':r'\propto ','×':r'\times ','·':r'\cdot ','−':'-','±':r'\pm ','≫':r'\gg ','≪':r'\ll ','°':r'^{\circ}','ṅ':r'\dot{n}','̃':r'\widetilde{}'}
SUP='⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺ⁿ⁽⁾ⁱᴺ⁄';SUB='₀₁₂₃₄₅₆₇₈₉ₖᵢⱼₙₚₜₓ'
TRANSLATE=str.maketrans(SUP+SUB,'0123456789-+n()iN/'+'0123456789kijnptx')
WORDS={'p_rgh':r'p_{\mathrm{rgh}}','Velec':r'V_{\mathrm{elec}}','cGas':r'c_{\mathrm{Gas}}','DGas':r'D_{\mathrm{Gas}}','alpha':r'\alpha','rho':r'\rho','epsilon':r'\varepsilon','kappa':r'\kappa','sigma':r'\sigma','omega':r'\omega','deltaT':r'\Delta t','eta':r'\eta','Cmu':r'C_\mu','mu':r'\mu','nu':r'\nu','Co':r'\mathrm{Co}','Re':r'\mathrm{Re}','Sc':r'\mathrm{Sc}','Pe':r'\mathrm{Pe}','Pr':r'\mathrm{Pr}','Prt':r'\mathrm{Pr}_t','St':r'\mathrm{St}','Ca':r'\mathrm{Ca}','We':r'\mathrm{We}','Bo':r'\mathrm{Bo}','Bi':r'\mathrm{Bi}','Fo':r'\mathrm{Fo}','cos':r'\cos ','sin':r'\sin ','tan':r'\tan ','exp':r'\exp ','erfc':r'\operatorname{erfc}','max':r'\max ','sum':r'\sum ','integral':r'\int ','interpolate':r'\operatorname{interpolate}',
 'Uin':r'U_{\mathrm{in}}','Ain':r'A_{\mathrm{in}}','Ae':r'A_e','Aref':r'A_{\mathrm{ref}}','Vref':r'V_{\mathrm{ref}}','Uref':r'U_{\mathrm{ref}}','Vnum':r'V_{\mathrm{num}}','Vgas':r'V_{\mathrm{gas}}','Vexpected':r'V_{\mathrm{expected}}','cideal':r'c_{\mathrm{ideal}}','cref':r'c_{\mathrm{ref}}','cwall':r'c_{\mathrm{wall}}','Tref':r'T_{\mathrm{ref}}','Ttop':r'T_{\mathrm{top}}','Umax':r'U_{\max}','cmean':r'\overline{c}',
 'Cp':r'C_p','Cd':r'C_d','Fx':r'F_x','Sm':r'S_m','ST':r'S_T','qv':r'q_v','aP':r'a_P','UP':r'U_P','rAU':r'r_{AU}',
}
SUBWORDS=['Vg','pg','yc','xc','zc','hN','T1','Tp','Sp','Ep','Qh','Q0','QA','QB','cA','cB','CA','CB','cf','cP','wf','φf','Vi','yi','ei','Ti','TL','TP','Tw','T0','V0','R0','j0','J0','x0','w0','Vm','Ux','Uf','Sf','Iapplied']
for v in SUBWORDS:WORDS.setdefault(v,v[0]+'_{'+v[1:]+'}')
for v in ['αwater','αwater,i','αg','αg,i','αi','αw','ρl','ρg','νl','μl','θg','θ0','φw','δ99','εV','ηg','tσ','∇sσ','Cμ']:
 base,suffix=(v[0],v[1:]);WORDS[v]=('\\'+GREEK[base] if base in GREEK else r'\nabla' if base=='∇' else base)+'_{'+(r'\mathrm{'+suffix+'}' if len(suffix)>2 else suffix)+'}'
WORDS['∇sσ']=r'\nabla_s\sigma';WORDS['Cμ']=r'C_\mu';WORDS['tσ']=r't_\sigma'
UNITS='kg mol mm ms Pa rad cd'.split()
RUN=re.compile(r"[A-Za-z0-9\u0370-\u03ff\u2070-\u209f\u1d2c-\u1d7f²³¹⁄∂∇∫∮∑√∞≤≥≠≈∝×·−±≫≪̃ṅ_+*/^=<>|().,\[\]{}%'°–\-\s]+")
CODE_WORDS=set('maxCo maxAlphaCo maxDeltaT nSurfaceLayers maxLocalCells maxGlobalCells minVol scale stretch xcells expansionRatio relativeSizes finalLayerThickness locationInMesh tolerance relTol class theta0 alpha.water endTime deltaT nNonOrthogonalCorrectors lowerRefineLevel upperRefineLevel refineInterval maxRefinement maxCells nBufferLayers gradient fixedValue refValue refGradient valueFraction electricTime'.split())

def linear_tex(raw):
    # Tokenize names before converting Greek characters; never replace inside TeX commands.
    names=sorted(WORDS,key=len,reverse=True)
    tokens=[]
    def hold(value):tokens.append(value);return '\ue000'+str(len(tokens)-1)+'\ue001'
    raw=re.sub('|'.join(re.escape(n) for n in names),lambda m:hold(WORDS[m[0]]) if ((not m[0][0].isascii() or m.start()==0 or not raw[m.start()-1].isalpha() or m[0] in ['cos','sin','exp']) and (m.end()==len(raw) or not (raw[m.end()].isascii() and raw[m.end()].isalpha()))) else m[0],raw)
    raw=re.sub(r'(?<![A-Za-z])(\d+(?:\.\d+)?)[eE]([−+-]?\d+)',lambda m:m[1]+r'\times10^{'+m[2].replace('−','-')+'}',raw)
    raw=re.sub('['+SUP+']+',lambda m:'^{'+m[0].translate(TRANSLATE)+'}',raw)
    raw=re.sub('['+SUB+']+',lambda m:'_{'+m[0].translate(TRANSLATE)+'}',raw)
    raw=re.sub(r'\^\(([^()]*)\)',r'^{\1}',raw)
    raw=re.sub(r'\^(-?\d+(?:\.\d+)?)',r'^{\1}',raw)
    raw=re.sub(r'_([A-Za-z][A-Za-z0-9,]*)',lambda m:'_{'+(r'\mathrm{'+m[1]+'}' if len(m[1])>2 else m[1])+'}',raw)
    # Balanced square root arguments, including nested parentheses.
    while re.search(r'√|sqrt',raw):
        m=re.search(r'√|sqrt',raw);start=m.end()
        if start<len(raw) and raw[start] in '([':
            opener=raw[start];closer=')' if opener=='(' else ']';depth=0;end=start
            for end in range(start,len(raw)):
                if raw[end]==opener:depth+=1
                elif raw[end]==closer:
                    depth-=1
                    if depth==0:break
            if depth:break
            inside=raw[start+1:end];stop=end+1
        else:
            a=re.match(r'(?:[A-Za-z0-9]+|\ue000\d+\ue001)',raw[start:]);inside=a[0] if a else '';stop=start+len(inside)
        raw=raw[:m.start()]+hold(r'\sqrt{'+linear_tex(inside)+'}')+raw[stop:]
    raw=re.sub(r'([A-Za-z])̃',lambda m:hold(r'\widetilde{'+m[1]+'}'),raw)
    raw=''.join('\\'+GREEK[c]+' ' if c in GREEK else SYMBOLS.get(c,c) for c in raw)
    raw=raw.replace('%',r'\%').replace('–',r'\text{–}')
    for unit in UNITS:raw=re.sub(r'(?<![A-Za-z\\])'+unit+r'(?![A-Za-z])',lambda m:r'\mathrm{'+unit+'}',raw)
    # A whitespace-separated SI suffix is upright; single variables remain italic.
    raw=re.sub(r'(?<=\d)\s+([msANKWJV])(?=[/^\s]|$)',lambda m:r'\,\mathrm{'+m[1]+'}',raw)
    for _ in range(4):
        for i,value in enumerate(tokens):raw=raw.replace('\ue000'+str(i)+'\ue001',value)
    return raw.strip()

def mathify(text):
    r"""Return HTML prose with explicit \(...\) formulas and protected inline code."""
    saved=[]
    def hold(tex,code=False):
        display=len(tex)>125
        value='<code>'+html.escape(tex)+'</code>' if code else (r'\[' if display else r'\(')+html.escape(tex)+(r'\]' if display else r'\)')
        saved.append(value);return '\ue100'+str(len(saved)-1)+'\ue101'
    # Already authored TeX and inline code survive re-imports unchanged.
    text=re.sub(r'\\\((.*?)\\\)',lambda m:hold(m[1]),text,flags=re.S)
    text=re.sub(r'`([^`]+)`',lambda m:hold(m[1],True),text)
    # Protect entire command fragments; dollars and equality here are syntax.
    text=re.sub(r'(?:export |env |wmSet )[A-Z_][A-Z_0-9]*=[^，。；\n]+',lambda m:hold(m[0],True),text)
    text=re.sub(r'(?:EXE|LIB|app|solver_pid)\s*=\s*\$[^，。；\n]+',lambda m:hold(m[0],True),text)
    text=re.sub(r'\b(?:'+ '|'.join(map(re.escape,CODE_WORDS))+r')\s*=\s*(?:\([^)]*\)|[A-Za-z0-9_.+−-]+)',lambda m:hold(m[0],True),text)
    # Curated multi-part formulae are applied longest-first.
    for original,tex in sorted(SPECIAL.items(),key=lambda kv:len(kv[0]),reverse=True):text=text.replace(original,hold(tex)) if original in text else text
    def convert(m):
        raw=m[0];s=raw.strip();left=raw[:len(raw)-len(raw.lstrip())];right=raw[len(raw.rstrip()):]
        if not s:return raw
        signal=bool(re.search(r'[α-ωΑ-Ω∂∇∫∮∑√≈≤≥≠≲≫≪∝²³⁰¹⁻⁺₀-₉]|\^|\b(?:Co|Re|D|U)\s*[<>]',s))
        if '=' in s and re.match(r'(?:[A-Za-z][A-Za-z0-9_]{0,10}|[0-9.]+[×*/])',s):signal=True
        if not signal or re.search(r'\b(?:FOAM_|WM_|export|directories|processors|wmake|Euler|DIR)\b',s):return raw
        if s in ['=','0 =','1 =','0=','1=']:return raw
        prefix='';suffix=''
        while s and s[0] in '([,' and (s[0]==',' or s.count(s[0])<s.count({'(':')','[':']',',':','}[s[0]])):
            prefix+=s[0];s=s[1:]
        while s and s[-1] in ')] ,' and (s[-1] in ' ,' or s.count(s[-1])>s.count({')':'(',']':'[',' ':' ',',':','}[s[-1]])):
            suffix=s[-1]+suffix;s=s[:-1]
        # Leave natural-language assignment fragments outside math when RHS is Chinese.
        if s.endswith(('=','≈','×')):suffix=s[-1]+suffix;s=s[:-1].rstrip()
        if not s:return raw
        return left+prefix+hold(linear_tex(s))+suffix+right
    text=RUN.sub(convert,text)
    result=html.escape(text).replace('\n','<br>')
    for i,value in enumerate(saved):result=result.replace('\ue100'+str(i)+'\ue101',value)
    return result
