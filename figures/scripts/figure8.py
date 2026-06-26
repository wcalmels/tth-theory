import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.gridspec import GridSpec

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

fig = plt.figure(figsize=(14, 11))
gs = GridSpec(2, 2, figure=fig, hspace=0.38, wspace=0.35)
phi_golden = 1.618
delta = 4.669

# ============================================================================
# PANEL A: Tesla Vortex 3-6-9
# ============================================================================
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_xlim(-1.7, 1.7); ax1.set_ylim(-1.8, 1.7)
ax1.set_aspect('equal'); ax1.axis('off')
ax1.set_title('(A) Tesla Vortex Mathematics:\nThe 3-6-9 Pattern', fontsize=12, fontweight='bold', pad=10)

theta_c = np.linspace(0, 2*np.pi, 300)
ax1.plot(1.3*np.cos(theta_c), 1.3*np.sin(theta_c), 'k-', linewidth=2, alpha=0.4)

positions = {}
for n in range(1, 10):
    angle = np.pi/2 - (n-1)*2*np.pi/9
    r = 1.15
    positions[n] = (r*np.cos(angle), r*np.sin(angle))
    color = 'red' if n in [3,6,9] else 'navy'
    size  = 16  if n in [3,6,9] else 13
    fc    = 'gold' if n in [3,6,9] else 'lightblue'
    ax1.text(positions[n][0], positions[n][1], str(n),
             ha='center', va='center', fontsize=size, fontweight='bold', color=color,
             bbox=dict(boxstyle='circle,pad=0.3', facecolor=fc, edgecolor=color, linewidth=2))

seq = [1,2,4,8,7,5,1]
for i in range(len(seq)-1):
    p1, p2 = positions[seq[i]], positions[seq[i+1]]
    ax1.annotate('', xy=(p2[0]*0.85, p2[1]*0.85), xytext=(p1[0]*0.85, p1[1]*0.85),
                arrowprops=dict(arrowstyle='->', color='blue', lw=2.5, mutation_scale=20))

for pair in [(3,6),(6,9),(9,3)]:
    p1, p2 = positions[pair[0]], positions[pair[1]]
    ax1.plot([p1[0]*0.85, p2[0]*0.85], [p1[1]*0.85, p2[1]*0.85], 'r-', linewidth=3, alpha=0.7)

ax1.text(0, 0, '9', ha='center', va='center', fontsize=22, fontweight='bold', color='red',
         bbox=dict(boxstyle='circle,pad=0.4', facecolor='yellow', edgecolor='red', linewidth=3))
ax1.text(0, -1.58, 'Blue: Doubling (1→2→4→8→7→5→1)\nRed: Axis (3-6-9)', ha='center',
         fontsize=9, fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='gray', linewidth=1.5))
ax1.text(0, 1.53, '$2^n$ mod 9 $\\leftrightarrow$ Octave structure in TTH',
         ha='center', fontsize=8.5, style='italic', color='darkblue',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='blue', linewidth=1.5))

# ============================================================================
# PANEL B: Russell 7 Octaves
# ============================================================================
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_xlim(-0.5, 8.5); ax2.set_ylim(-1.8, 9.2)
ax2.axis('off')
ax2.set_title("(B) Russell's Seven-Octave Cosmogony:\nMatter as Compressed Light",
              fontsize=12, fontweight='bold', pad=10)

octaves = [
    (1,'Primordial','H, He',   '#FF6B6B',0.8),
    (2,'Light Elem.','Li-Ne',  '#FFA07A',1.0),
    (3,'Metals','Na-Ar',       '#FFD700',1.2),
    (4,'Transition','K-Kr',    '#90EE90',1.4),
    (5,'Heavy','Rb-Xe',        '#87CEEB',1.6),
    (6,'Radioactive','Cs-Rn',  '#DDA0DD',1.8),
    (7,'Transuranics','Fr+',   '#F0E68C',2.0),
]

for n, name, elems, color, comp in octaves:
    y = 8.5 - n*1.1
    bw = comp * 3
    ax2.add_patch(FancyBboxPatch((4-bw/2, y-0.35), bw, 0.7,
                                 boxstyle="round,pad=0.05",
                                 facecolor=color, edgecolor='black', linewidth=1.5, alpha=0.85))
    ax2.text(0.2, y, str(n), ha='center', va='center', fontsize=14, fontweight='bold',
             bbox=dict(boxstyle='circle,pad=0.3', facecolor=color, edgecolor='black', linewidth=1.5))
    ax2.text(4, y+0.04, name,  ha='center', va='center', fontsize=10, fontweight='bold')
    ax2.text(4, y-0.2, f'({elems})', ha='center', va='center', fontsize=8.5, color='darkslategray')
    ax2.text(8.1, y, f'$\\Phi^{{-{n}}}$', ha='center', va='center',
             fontsize=9, color='darkgreen', fontweight='bold')

ax2.text(0.2, 8.25, 'Oct.', ha='center', fontsize=10, fontweight='bold')
ax2.text(4,   8.25, 'Element Group', ha='center', fontsize=10, fontweight='bold')
ax2.text(8.1, 8.25, 'TTH $\\phi$',  ha='center', fontsize=10, fontweight='bold', color='darkgreen')
ax2.axhline(7.95, color='black', linewidth=1.5)

theta_s = np.linspace(0, 3*np.pi, 300)
r_s = 0.4 * phi_golden**(theta_s/(2*np.pi))
y_s = theta_s*1.15/np.pi - 0.5
mask_s = (y_s > -1.3) & (y_s < 7.8)
ax2.plot(r_s[mask_s]*0.3*np.cos(theta_s[mask_s])+4, y_s[mask_s], 'b-', linewidth=1.5, alpha=0.5)

ax2.text(4, -1.35,
         'Russell: "Matter is light in motion"\nTTH: $\\phi_n = \\Phi^{-n}M_{Pl}$ at each octave',
         ha='center', fontsize=8.5, style='italic', color='darkblue',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='aliceblue', edgecolor='blue', linewidth=1.5))

# ============================================================================
# PANEL C: Feigenbaum Bifurcation
# ============================================================================
ax3 = fig.add_subplot(gs[1, 0])

def logistic_attractor(r, x0=0.5, n_skip=500, n_plot=100):
    x = x0
    for _ in range(n_skip):
        x = r*x*(1-x)
    xs = []
    for _ in range(n_plot):
        x = r*x*(1-x)
        xs.append(x)
    return xs

r_vals = np.linspace(2.5, 4.0, 2000)
r_plot, x_plot = [], []
for r in r_vals:
    xs = logistic_attractor(r)
    r_plot.extend([r]*len(xs))
    x_plot.extend(xs)

ax3.plot(r_plot, x_plot, ',', color='navy', alpha=0.15, markersize=0.3)

bifs = [3.0, 3.449, 3.544, 3.5644]
for i, rb in enumerate(bifs):
    ax3.axvline(rb, color='red', linestyle='--', linewidth=1.5, alpha=0.8)
    ax3.text(rb, 0.93, f'$r_{i+1}$', ha='center', fontsize=9, color='red', fontweight='bold')

for i in range(len(bifs)-1):
    mid = (bifs[i]+bifs[i+1])/2
    ax3.annotate('', xy=(bifs[i+1], 0.07), xytext=(bifs[i], 0.07),
                arrowprops=dict(arrowstyle='<->', color='orange', lw=2.5))

ax3.text(3.22, 0.03,
         f'$\\delta = \\lim_{{n\\to\\infty}}'
         f'\\frac{{r_n-r_{{n-1}}}}{{r_{{n+1}}-r_n}} = {delta:.3f}$',
         ha='center', fontsize=9, color='darkorange', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', edgecolor='orange', linewidth=2))

ax3.axvspan(3.57, 4.0, alpha=0.08, color='red')
ax3.text(3.78, 0.5, 'Chaos', fontsize=11, color='red', fontweight='bold', rotation=90, va='center')
ax3.text(2.65, 0.87, f'$\\delta = {delta}$\nuniversal constant',
         fontsize=9, fontweight='bold', color='darkorange',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='orange', linewidth=2))

ax3.set_xlabel('Parameter $r$', fontsize=11, fontweight='bold')
ax3.set_ylabel('Steady-state $x$', fontsize=11, fontweight='bold')
ax3.set_title('(C) Feigenbaum Period-Doubling:\nUniversal Route to Chaos',
              fontsize=12, fontweight='bold', pad=10)
ax3.set_xlim(2.5, 4.0); ax3.set_ylim(0, 1)
ax3.grid(True, alpha=0.3)

# ============================================================================
# PANEL D: TTH Unification
# ============================================================================
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_xlim(0, 10); ax4.set_ylim(0, 10)
ax4.axis('off')
ax4.set_title('(D) TTH Unification:\nAll Three Principles in One Framework',
              fontsize=12, fontweight='bold', pad=10)

def fbox(ax, xy, w, h, fc, ec, lw=2, **kw):
    ax.add_patch(FancyBboxPatch(xy, w, h, boxstyle="round,pad=0.15",
                                facecolor=fc, edgecolor=ec, linewidth=lw,
                                alpha=0.9, **kw))

# Central box
fbox(ax4, (2.8, 4.0), 4.4, 2.3, 'gold', 'black', lw=3, zorder=10)
ax4.text(5, 5.35, 'TORSIONAL\nHOLOFRACTAL\nTHEORY (TTH)',
         ha='center', va='center', fontsize=13, fontweight='bold', zorder=15)
ax4.text(5, 4.2,
         '$V(\\phi) \\ni \\Lambda_\\delta^4[1-\\cos(\\delta\\phi/\\Phi M_{Pl})]$',
         ha='center', fontsize=9, color='darkred', fontweight='bold', zorder=15)

# Tesla box
fbox(ax4, (0.2, 7.5), 3.6, 2.0, '#87CEEB', 'blue', lw=2.5)
ax4.text(2.0, 8.65, 'TESLA (~1900)', ha='center', fontsize=11, fontweight='bold', color='darkblue')
ax4.text(2.0, 8.1, 'Octave resonance\n$2^n$ structure / 3-6-9',
         ha='center', fontsize=8.5, color='navy')

# Russell box
fbox(ax4, (6.2, 7.5), 3.6, 2.0, '#90EE90', 'green', lw=2.5)
ax4.text(8.0, 8.65, 'RUSSELL (~1926)', ha='center', fontsize=11, fontweight='bold', color='darkgreen')
ax4.text(8.0, 8.1, '7 octave levels\n$\\Phi$ spirals / light compression',
         ha='center', fontsize=8.5, color='darkgreen')

# Feigenbaum box
fbox(ax4, (2.8, 0.5), 4.4, 2.0, '#FFD700', 'darkorange', lw=2.5)
ax4.text(5, 1.65, 'FEIGENBAUM (~1978)', ha='center', fontsize=11, fontweight='bold', color='darkorange')
ax4.text(5, 1.1, '$\\delta=4.669$  universal | critical thresholds',
         ha='center', fontsize=8.5, color='darkred')

ap = dict(mutation_scale=25, linewidth=3)

# Tesla → TTH
ax4.annotate('', xy=(3.5, 6.1), xytext=(2.3, 7.5),
            arrowprops=dict(arrowstyle='->', color='blue', **ap))
ax4.text(2.4, 6.95, 'Octaves →\nfractal projection',
         ha='center', fontsize=8, color='blue', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='aliceblue', edgecolor='blue', linewidth=1))

# Russell → TTH
ax4.annotate('', xy=(6.5, 6.1), xytext=(7.7, 7.5),
            arrowprops=dict(arrowstyle='->', color='green', **ap))
ax4.text(7.5, 6.95, '7 levels →\n$\\Phi^{-n}$ compress.',
         ha='center', fontsize=8, color='darkgreen', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='honeydew', edgecolor='green', linewidth=1))

# Feigenbaum → TTH
ax4.annotate('', xy=(5, 4.0), xytext=(5, 2.5),
            arrowprops=dict(arrowstyle='->', color='darkorange', **ap))
ax4.text(5.9, 3.25, '$\\delta$ →\n$\\Phi_{crit}$',
         ha='center', fontsize=8, color='darkorange', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow', edgecolor='orange', linewidth=1))

# Bottom equation strip
fbox(ax4, (0.2, 0.1), 9.6, 0.65, 'lavender', 'purple', lw=2)
ax4.text(5, 0.43,
         '$\\phi_0 = \\Phi M_{Pl}$   |   $\\omega_{eff}=2\\pi\\delta/T$   |   '
         '$\\Phi_{crit}=\\hbar/(\\delta M_{Pl})$',
         ha='center', va='center', fontsize=9.5, fontweight='bold', color='purple')

# TTH year
ax4.text(5, 6.42, '2026 — W. Calmels K.',
         ha='center', fontsize=9, color='black', style='italic', fontweight='bold')

plt.savefig('/home/claude/tth_figures/figure8_tesla_russell_feigenbaum.pdf',
            dpi=300, bbox_inches='tight')
plt.savefig('/home/claude/tth_figures/figure8_tesla_russell_feigenbaum.png',
            dpi=300, bbox_inches='tight')
print("✓ Figure 8 saved")
plt.close()
