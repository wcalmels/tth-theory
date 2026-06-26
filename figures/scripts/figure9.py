import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib

matplotlib.rcParams['font.family'] = 'serif'
matplotlib.rcParams['font.size'] = 10

fig, ax = plt.subplots(figsize=(10, 13))
ax.set_xlim(0, 10); ax.set_ylim(0, 14); ax.axis('off')

def fbox(ax, x, y, w, h, fc, ec, lw=2.5, zorder=5, alpha=0.92):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.18",
                                facecolor=fc, edgecolor=ec,
                                linewidth=lw, zorder=zorder, alpha=alpha))

def arr(ax, x1,y1,x2,y2, col, lw=3.5, rad=0.0):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle='->', color=col,
                                lw=lw, mutation_scale=35,
                                connectionstyle=f'arc3,rad={rad}'))

# Title
fbox(ax, 0.5, 12.8, 9.0, 0.9, '#2C3E50','#2C3E50', lw=3, zorder=10)
ax.text(5, 13.27,'THREE-LEVEL HIERARCHICAL CONSCIOUSNESS ARCHITECTURE IN TTH',
        ha='center', va='center', fontsize=11, fontweight='bold', color='white', zorder=15)

# ---- LEVEL I ----
fbox(ax, 0.4, 9.9, 9.2, 2.5, '#D6EAF8','#2980B9', lw=3)
ax.text(5,12.15,'LEVEL I: Classical Neural Computation  (3D space)',
        ha='center', fontsize=12, fontweight='bold', color='#1A5276')

theta = np.linspace(0,2*np.pi,200)
bx = 1.6 + (0.6+0.08*np.cos(5*theta))*np.cos(theta)
by = 11.0 + (0.6+0.08*np.cos(5*theta))*np.sin(theta)*0.75
ax.fill(bx, by, color='#AED6F1', alpha=0.7, zorder=6)
ax.plot(bx, by, '#2980B9', linewidth=2, zorder=7)

nodes = [(3.2,10.5),(3.8,11.3),(4.4,10.4),(4.9,11.0),(5.5,10.6),(6.0,11.2),(6.6,10.5)]
for i,(nx,ny) in enumerate(nodes):
    ax.plot(nx,ny,'o',color='#2980B9',markersize=9,zorder=8)
    for j,(mx,my) in enumerate(nodes):
        if abs(i-j) in [1,2] and i<j:
            ax.plot([nx,mx],[ny,my],color='#85C1E9',linewidth=1.2,alpha=0.7,zorder=7)

t_s = np.linspace(0,1.8,200); spikes = np.zeros_like(t_s)
for st in [0.2,0.5,0.9,1.3,1.6]:
    spikes[np.abs(t_s-st)<0.02] = 0.35
ax.plot(7.2+t_s, 10.9+spikes, color='#1A5276', linewidth=2, zorder=8)
ax.text(8.1,10.72,'Spike\ntrains',ha='center',fontsize=7.5,color='#1A5276',fontweight='bold')

# Use plain text (no LaTeX) for problematic symbols
ax.text(1.6,10.2, r'Eq: $\tau_i \dot{r}_i = -r_i + g(\sum_j w_{ij}r_j)$'+'\nSpace: R3  |  Deff = 3.0',
        ha='center',fontsize=8.5,color='#1A5276',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.8))
ax.text(5.2,10.15,'Cortex, thalamus\nN ~ 1.6e10 neurons',
        ha='center',fontsize=8.5,color='#1A5276',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.8))

# Arrow I→II
arr(ax, 5,9.9, 5,9.58, '#2980B9')
ax.text(5,9.72, r'$\rho_{neural}$ sources holofractal field $\phi$',
        ha='center',fontsize=9,fontweight='bold',color='#2980B9',
        bbox=dict(boxstyle='round,pad=0.25',facecolor='white',edgecolor='#2980B9',linewidth=1.5))

# ---- LEVEL II ----
fbox(ax, 0.4, 7.0, 9.2, 2.2, '#D5F5E3','#27AE60', lw=3)
ax.text(5,8.98, r'LEVEL II: Holofractal Field Mediation  $\phi(x,t)$',
        ha='center',fontsize=12,fontweight='bold',color='#1D6A39')

x_phi = np.linspace(0.7,4.5,300)
phi_v = 1.0 + 0.3*np.sin(4.669*x_phi)*np.exp(-((x_phi-2.6)**2)/2)
ax.plot(x_phi, 7.4+phi_v*0.6, color='#27AE60', linewidth=2.5, zorder=8)
ax.fill_between(x_phi, 7.4, 7.4+phi_v*0.6, alpha=0.25, color='#27AE60')
ax.text(2.6,7.22,'Holofractal field',ha='center',fontsize=8.5,color='#1D6A39',fontweight='bold')

theta_gs = np.linspace(0,4*np.pi,400)
r_gs = 0.18 * 1.618**(theta_gs/(2*np.pi))
ax.plot(5.5+r_gs*np.cos(theta_gs), 8.0+r_gs*np.sin(theta_gs)*0.7,
        'gold',linewidth=2.5,alpha=0.9,zorder=8)
ax.text(5.5,7.22,'Golden ratio\nPhi=1.618',ha='center',fontsize=8,color='#7D6608',fontweight='bold')

ax.text(7.8,8.35, r'$\nabla^2\phi - dV/d\phi = -y\bar{\psi}\psi$'+'\nDeff ~ 4.0-4.3\nRange ~ cm-m',
        ha='center',fontsize=8.5,color='#1D6A39',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.85))
ax.text(2.6,8.72,'Microtubules & thalamo-cortical\ncircuits as phi sources',
        ha='center',fontsize=8,color='#1D6A39',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.85))

# Arrow II→III
arr(ax, 5,7.0, 5,6.58, '#27AE60')
ax.text(5,6.77, r'$\eta(t)=(\alpha_T/M_{Pl})\phi(t)$ controls quantum coupling',
        ha='center',fontsize=9,fontweight='bold',color='#27AE60',
        bbox=dict(boxstyle='round,pad=0.25',facecolor='white',edgecolor='#27AE60',linewidth=1.5))

# ---- LEVEL III ----
fbox(ax, 0.4, 4.1, 9.2, 2.1, '#FDEDEC','#C0392B', lw=3)
ax.text(5,6.0, r'LEVEL III: Quantum State Integration  $\Psi \in \mathcal{H}$',
        ha='center',fontsize=12,fontweight='bold',color='#7B241C')

x_wf = np.linspace(0.7,4.5,300)
psi_t = 0.55*np.exp(-((x_wf-1.8)**2)/0.25)+0.55*np.exp(-((x_wf-3.5)**2)/0.25)
ax.plot(x_wf, 4.5+psi_t*0.85, color='#C0392B', linewidth=2.5, zorder=8)
ax.fill_between(x_wf, 4.5, 4.5+psi_t*0.85, alpha=0.2, color='#C0392B')
ax.text(2.6,4.22, r'Superposition $|\psi_1\rangle + |\psi_2\rangle$',
        ha='center',fontsize=8.5,color='#7B241C',fontweight='bold')

for r_h in [0.05,0.12,0.2,0.3,0.42]:
    ax.add_patch(plt.Circle((6.5,5.1),r_h*2.5,fill=False,
                             edgecolor='#C0392B',linewidth=1.5,alpha=0.5,zorder=7))
ax.text(6.5,4.28,'H: inf-dimensional\nDeff = exp(S_vN) ~ 1e8-1e12',
        ha='center',fontsize=8.5,color='#7B241C',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.85))

ax.text(8.5,5.45, r'$\Phi_{TTH}=\int\eta|\Psi|^2 S_{vN}d^3r$'+'\nCollapse: Phi > Phi_crit\ntau ~ 1e-3 - 1e-1 s',
        ha='center',fontsize=8.5,color='#7B241C',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.85))
ax.text(2.6,5.72,'Microtubule quantum\ncoherence (Orch-OR)',
        ha='center',fontsize=8,color='#7B241C',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.85))

# ---- COLLAPSE ----
fbox(ax, 3.5,2.3, 3.0,1.4, '#F9E79F','#D4AC0D', lw=3)
ax.text(5,3.22,'COLLAPSE EVENT',ha='center',fontsize=12,fontweight='bold',color='#7D6608')
ax.text(5,2.72, r'$\Phi_{TTH} > \Phi_{crit} = \hbar/(\delta M_{Pl})$',
        ha='center',fontsize=9,color='#7D6608',fontweight='bold')
arr(ax, 5,4.1, 5,3.7, '#C0392B')

# ---- CONSCIOUS EXPERIENCE ----
fbox(ax, 1.5,0.4, 7.0,1.6, '#E8DAEF','#7D3C98', lw=3.5)
ax.text(5,1.38,'PHENOMENAL CONSCIOUS EXPERIENCE',
        ha='center',fontsize=12,fontweight='bold',color='#4A235A')
ax.text(5,0.82,'Definite eigenstate -> Subjective qualia\n'
        '"What it is like" = Property of geometric collapse in torsional spacetime',
        ha='center',fontsize=8.5,color='#4A235A',
        bbox=dict(boxstyle='round,pad=0.3',facecolor='white',alpha=0.8))
arr(ax, 5,2.3, 5,2.0, '#7D3C98')

# Feedback arrow Level III→I
arr(ax, 0.7,4.5, 0.7,9.9, 'gray', lw=2.5, rad=0.0)
ax.text(0.22,7.2,'Collapse\nfeedback\nto neurons',
        ha='center',va='center',fontsize=8,color='gray',fontweight='bold',rotation=90)

# Dim labels on right
for (label, dim, col, yp) in [('I','D=3','#2980B9',11.1),
                                ('II','D~4.1','#27AE60',8.1),
                                ('III','D=inf','#C0392B',5.2)]:
    fbox(ax, 9.0,yp-0.3, 0.85,0.75, col, col, lw=1.5, alpha=0.2)
    ax.text(9.43,yp+0.07,dim,ha='center',fontsize=8,fontweight='bold',color=col)

ax.text(9.43,12.4,'Dim.',ha='center',fontsize=8,fontweight='bold')
ax.text(5,13.7,'W. Calmels K. — TUCH Systems Research Laboratory, 2026',
        ha='center',fontsize=8,style='italic',color='white')

plt.savefig('/home/claude/tth_figures/figure9_hierarchy.pdf', dpi=300, bbox_inches='tight')
plt.savefig('/home/claude/tth_figures/figure9_hierarchy.png', dpi=300, bbox_inches='tight')
print("✓ Figure 9 saved")
plt.close()
