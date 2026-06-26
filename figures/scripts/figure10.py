"""
Figure 10: Dimensional Scenarios in TTH
4-panel comparison of dimensional interpretations
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse, FancyArrowPatch
from matplotlib.gridspec import GridSpec
import matplotlib.patches as mpatches

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 9
plt.rcParams['mathtext.fontset'] = 'dejavuserif'

fig = plt.figure(figsize=(14, 11))
gs = GridSpec(2, 2, figure=fig, hspace=0.40, wspace=0.35)

def fbox(ax, x, y, w, h, fc, ec, lw=2, alpha=0.9, zorder=5):
    ax.add_patch(FancyBboxPatch((x,y), w, h,
                                boxstyle="round,pad=0.15",
                                facecolor=fc, edgecolor=ec,
                                linewidth=lw, alpha=alpha, zorder=zorder))

# ============================================================================
# PANEL A: 4D Fundamental TTH
# ============================================================================
ax1 = fig.add_subplot(gs[0, 0])
ax1.set_xlim(0, 10); ax1.set_ylim(0, 10); ax1.axis('off')
ax1.set_title('(A) Scenario I: TTH as Fundamental 4D Theory',
              fontsize=11, fontweight='bold', pad=12)

# Spacetime grid
for i in range(11):
    ax1.plot([i*1.0, i*1.0+1.5], [i*0.5, i*0.5+6.5],
             color='#85C1E9', linewidth=0.8, alpha=0.5)
    ax1.plot([0+i*0.5, 10], [i*1.0-1, i*1.0+4],
             color='#85C1E9', linewidth=0.8, alpha=0.5)

# 4D spacetime box
fbox(ax1, 1, 3.5, 8, 4.5, '#EBF5FB','#2980B9', lw=3)
ax1.text(5, 7.7, r'$\mathcal{M}^4$: 4D Riemann-Cartan Spacetime',
         ha='center', fontsize=10, fontweight='bold', color='#1A5276')

# Fields living in 4D
fields = [
    (2.5, 6.0, r'$g_{\mu\nu}$', '#E74C3C', 'Metric'),
    (5.0, 6.0, r'$T^\lambda_{\mu\nu}$', '#E67E22', 'Torsion'),
    (7.5, 6.0, r'$\phi(x)$', '#27AE60', 'Holofractal'),
    (2.5, 4.8, r'$\Psi(x)$', '#8E44AD', 'Matter'),
    (7.5, 4.8, r'$\Phi_{TTH}$', '#C0392B', 'Information'),
]
for (fx, fy, label, col, name) in fields:
    ax1.add_patch(Circle((fx, fy), 0.55, facecolor=col, edgecolor='black',
                          linewidth=1.5, alpha=0.85, zorder=8))
    ax1.text(fx, fy, label, ha='center', va='center',
             fontsize=8.5, fontweight='bold', color='white', zorder=9)
    ax1.text(fx, fy-0.85, name, ha='center', fontsize=7.5, color=col, fontweight='bold')

# Properties
fbox(ax1, 0.5, 0.3, 9.0, 2.8, '#FDFEFE','#2980B9', lw=2)
ax1.text(5, 2.8, 'Properties:', ha='center', fontsize=9, fontweight='bold', color='#1A5276')
props = [
    ('+ Simple & testable: all predictions in 4D', '#27AE60'),
    ('+ Compatible with standard model fields', '#27AE60'),
    ('+ Non-minimal coupling xi*phi^2*R(Gamma)', '#27AE60'),
    ('~ Non-renormalizable: needs UV completion', '#E67E22'),
    ('~ Addressed via asymptotic safety (Reuter 2012)', '#E67E22'),
]
for i, (p, col) in enumerate(props):
    ax1.text(1.0, 2.3-i*0.42, p, fontsize=8, color=col, fontweight='bold')

# ============================================================================
# PANEL B: 10D String Compactification
# ============================================================================
ax2 = fig.add_subplot(gs[0, 1])
ax2.set_xlim(0, 10); ax2.set_ylim(0, 10); ax2.axis('off')
ax2.set_title('(B) Scenario II: Effective Theory from 10D Strings',
              fontsize=11, fontweight='bold', pad=12)

# 10D space visualization
fbox(ax2, 0.3, 7.0, 9.4, 2.8, '#EBF5FB','#1A5276', lw=3)
ax2.text(5, 9.55, r'10D Superstring Theory: $\mathcal{M}^{10}$',
         ha='center', fontsize=10, fontweight='bold', color='#1A5276')

# 4 large dims
fbox(ax2, 0.7, 7.3, 4.0, 2.1, '#D6EAF8','#2980B9', lw=2.5)
ax2.text(2.7, 8.9, r'$\mathcal{M}^4$', ha='center', fontsize=12,
         fontweight='bold', color='#1A5276')
ax2.text(2.7, 8.4, '4 large dimensions\n(observable)', ha='center',
         fontsize=8.5, color='#1A5276', fontweight='bold')
ax2.text(2.7, 7.55, r'Scale: $\sim$ m to Gpc', ha='center', fontsize=8, color='#1A5276')

# 6 compact dims (Calabi-Yau)
fbox(ax2, 5.2, 7.3, 4.3, 2.1, '#FDEBD0','#E67E22', lw=2.5)
ax2.text(7.35, 8.9, r'$\mathcal{CY}_6$', ha='center', fontsize=12,
         fontweight='bold', color='#D35400')
ax2.text(7.35, 8.4, '6 compact dims\n(Calabi-Yau)', ha='center',
         fontsize=8.5, color='#D35400', fontweight='bold')
ax2.text(7.35, 7.55, r'Scale: $\sim \Phi M_{Pl}^{-1}$', ha='center', fontsize=8, color='#D35400')

# CY shape (torus-like visual)
theta_cy = np.linspace(0, 2*np.pi, 100)
for r_cy in [0.25, 0.45]:
    ax2.plot(7.35 + r_cy*np.cos(theta_cy)*0.7,
             8.0  + r_cy*np.sin(theta_cy)*0.35,
             color='#E67E22', linewidth=1.5, alpha=0.6, zorder=8)

# Times symbol
ax2.text(4.9, 8.4, r'$\times$', ha='center', fontsize=18, color='black', fontweight='bold')

# Compactification arrow
ax2.annotate('', xy=(5, 5.85), xytext=(5, 6.95),
            arrowprops=dict(arrowstyle='->', color='purple', lw=3, mutation_scale=30))
ax2.text(5, 6.4, 'Compactification\n(integrate over CY)',
         ha='center', fontsize=8.5, color='purple', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lavender',
                   edgecolor='purple', linewidth=1.5))

# Result: TTH 4D
fbox(ax2, 1.5, 3.8, 7.0, 1.8, '#D5F5E3','#27AE60', lw=3)
ax2.text(5, 5.35, r'Effective TTH in 4D', ha='center', fontsize=10,
         fontweight='bold', color='#1D6A39')
ax2.text(5, 4.85, r'$\phi(x) = M_{Pl}(V_{CY}/V_*)^{1/6}$   (radion field)',
         ha='center', fontsize=9, color='#1D6A39',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
ax2.text(5, 4.3, r'$v = \Phi M_{Pl}$ emerges from $V_{CY}/V_* = \Phi^6$',
         ha='center', fontsize=8.5, color='#1D6A39',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))

# Properties
fbox(ax2, 0.3, 0.3, 9.4, 3.2, '#FDFEFE','#27AE60', lw=2)
ax2.text(5, 3.2, 'Predictions:', ha='center', fontsize=9, fontweight='bold', color='#1D6A39')
ax2_props = [
    (r'+ Explains $v = \Phi M_{Pl}$ from topology', '#27AE60'),
    (r'+ $\delta$ from Laplacian eigenvalues on CY$_6$', '#27AE60'),
    (r'+ Unification with gauge forces (strings)', '#27AE60'),
    (r'~ KK tower: $m_n \sim n\Phi M_{Pl}$ (inaccessible)', '#E67E22'),
    (r'~ Requires string theory framework', '#E67E22'),
]
for i, (p, col) in enumerate(ax2_props):
    ax2.text(0.7, 2.75-i*0.48, p, fontsize=8, color=col, fontweight='bold')

# ============================================================================
# PANEL C: Hilbert Space Structure
# ============================================================================
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_xlim(0, 10); ax3.set_ylim(0, 10); ax3.axis('off')
ax3.set_title('(C) Scenario III: Informational Dimensionality\n'
              r'(4D physical space + $\infty$-dim Hilbert space)',
              fontsize=11, fontweight='bold', pad=8)

# Physical space (4D)
fbox(ax3, 0.3, 7.0, 4.2, 2.8, '#EBF5FB','#2980B9', lw=3)
ax3.text(2.4, 9.55, r'$\mathbb{R}^4$: Physical Spacetime',
         ha='center', fontsize=9, fontweight='bold', color='#1A5276')

# Grid inside
for i in range(5):
    ax3.plot([0.5+i*0.8, 0.5+i*0.8], [7.2, 9.5],
             color='#85C1E9', linewidth=0.8, alpha=0.6)
    ax3.plot([0.4, 4.3], [7.2+i*0.58, 7.2+i*0.58],
             color='#85C1E9', linewidth=0.8, alpha=0.6)

ax3.text(2.4, 7.5, r'$D = 4$', ha='center', fontsize=16,
         fontweight='bold', color='#2980B9')

# Tensor product symbol
ax3.text(4.75, 8.35, r'$\otimes$', ha='center', fontsize=22,
         color='black', fontweight='bold')

# Hilbert space (inf-D)
fbox(ax3, 5.2, 7.0, 4.5, 2.8, '#FDEDEC','#C0392B', lw=3)
ax3.text(7.45, 9.55, r'$\mathcal{H}$: Hilbert Space',
         ha='center', fontsize=9, fontweight='bold', color='#7B241C')

# Concentric circles representing inf dimensions
for k, r_hh in enumerate(np.linspace(0.15, 1.7, 8)):
    alpha_h = 0.9 - k*0.1
    ax3.add_patch(Circle((7.45, 8.35), r_hh*0.55,
                          fill=False, edgecolor='#C0392B',
                          linewidth=1.5, alpha=max(alpha_h, 0.2), zorder=7))

ax3.text(7.45, 8.35, r'$\infty$', ha='center', fontsize=18,
         fontweight='bold', color='#C0392B', zorder=10)
ax3.text(7.45, 7.25, r'$\dim(\mathcal{H}) = 2^N$',
         ha='center', fontsize=9, color='#7B241C', fontweight='bold')

# Effective dimension
fbox(ax3, 0.5, 4.5, 9.0, 2.2, '#FEF9E7','#D4AC0D', lw=3)
ax3.text(5, 6.45, 'Effective Dimensionality', ha='center',
         fontsize=10, fontweight='bold', color='#7D6608')
ax3.text(5, 5.95, r'$D_{eff}(\rho) = e^{S_{vN}(\rho)}$',
         ha='center', fontsize=11, color='#7D6608', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
ax3.text(5, 5.42, r'For neural system: $D_{eff} \sim 10^8 - 10^{12}$',
         ha='center', fontsize=9, color='#7D6608')

# State values
states_d = [('Deep sleep', 0.15), ('Awake', 0.55), ('Meditation', 0.80), ('Collapse', 0.02)]
colors_d  = ['#85C1E9','#27AE60','#8E44AD','#C0392B']
x_bars = [1.2, 3.2, 5.5, 7.8]
for i, ((state, val), col, xb) in enumerate(zip(states_d, colors_d, x_bars)):
    bar_h = val*3.2
    ax3.add_patch(FancyBboxPatch((xb-0.4, 0.5), 0.8, bar_h,
                                  boxstyle="round,pad=0.05",
                                  facecolor=col, edgecolor='black',
                                  linewidth=1.5, alpha=0.85, zorder=6))
    ax3.text(xb, bar_h+0.65, state, ha='center', fontsize=7.5,
             fontweight='bold', color=col, rotation=20)
    ax3.text(xb, bar_h+0.3, f'{val:.2f}', ha='center', fontsize=7.5,
             fontweight='bold', color='black')

ax3.text(5, 0.2, r'$D_{eff}/D_{max}$ for different states',
         ha='center', fontsize=8.5, color='black', fontweight='bold')

# Properties
ax3.text(5, 4.25, 'Collapse = Dimensional Reduction: '
         r'$D_{eff}^{before} \gg D_{eff}^{after}$',
         ha='center', fontsize=8.5, color='purple', fontweight='bold')

# ============================================================================
# PANEL D: Holographic Duality
# ============================================================================
ax4 = fig.add_subplot(gs[1, 1])
ax4.set_xlim(0, 10); ax4.set_ylim(0, 10); ax4.axis('off')
ax4.set_title('(D) Scenario IV: Holographic Duality\n'
              '4D TTH bulk / 3D boundary consciousness',
              fontsize=11, fontweight='bold', pad=8)

# 4D Bulk (AdS-like)
fbox(ax4, 0.3, 4.8, 9.4, 5.0, '#EBF5FB','#2980B9', lw=3)
ax4.text(5, 9.55, r'BULK: 4D Torsional Gravity (TTH)',
         ha='center', fontsize=10, fontweight='bold', color='#1A5276')

# Bulk content: geodesics and torsion
theta_b = np.linspace(0, 2*np.pi, 100)
for r_b in [0.8, 1.6, 2.4]:
    x_b = 5 + r_b*np.cos(theta_b)
    y_b = 7.2 + r_b*np.sin(theta_b)*0.45
    ax4.plot(x_b, y_b, '#85C1E9', linewidth=1.2, alpha=0.5)

ax4.text(5, 7.2, r'$g_{\mu\nu},\, T^\lambda_{\mu\nu},\, \phi(x)$',
         ha='center', va='center', fontsize=11, fontweight='bold', color='#1A5276')

# Minimal surface (RT surface)
theta_rt = np.linspace(0, np.pi, 100)
x_rt = 5 + 2.5*np.cos(theta_rt)
y_rt = 5.3 + 1.8*np.sin(theta_rt)
ax4.plot(x_rt, y_rt, 'orange', linewidth=3, alpha=0.9,
         zorder=8, label='Minimal surface')
ax4.fill_between(x_rt, 5.3, y_rt, alpha=0.15, color='orange')
ax4.text(5, 6.5, r'$\gamma_A$ minimal surface',
         ha='center', fontsize=8.5, color='#D35400', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.25', facecolor='white', alpha=0.85))

# Ryu-Takayanagi formula
ax4.text(5, 5.12, r'$\Phi_{TTH}(A) = \mathrm{Area}(\gamma_A)/(4G_{eff})$',
         ha='center', fontsize=9, color='darkorange', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow',
                   edgecolor='orange', linewidth=2))

# Holographic duality arrow
ax4.annotate('', xy=(5, 4.45), xytext=(5, 4.82),
            arrowprops=dict(arrowstyle='<->', color='purple',
                            lw=3.5, mutation_scale=30))
ax4.text(5, 4.62, 'Holographic duality',
         ha='center', fontsize=8.5, color='purple', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.2', facecolor='lavender',
                   edgecolor='purple', linewidth=1.5))

# 3D boundary (cortex)
fbox(ax4, 0.3, 2.4, 9.4, 1.9, '#D5F5E3','#27AE60', lw=3)
ax4.text(5, 4.1, 'BOUNDARY: 3D Cortical Sheet (Consciousness)',
         ha='center', fontsize=10, fontweight='bold', color='#1D6A39')

# Cortical surface
x_cort = np.linspace(0.6, 9.4, 200)
y_cort = 3.1 + 0.2*np.sin(15*x_cort/10*np.pi) + 0.1*np.sin(25*x_cort/10*np.pi)
ax4.plot(x_cort, y_cort, '#27AE60', linewidth=3, zorder=8)
ax4.fill_between(x_cort, 2.5, y_cort, alpha=0.3, color='#27AE60')
ax4.text(5, 2.68, r'$\Phi_{IIT}(A) \propto \mathrm{Area}_{cortical}(A)$  '
         '(Area-, not Volume-scaling)',
         ha='center', fontsize=8.5, color='#1D6A39', fontweight='bold')

# Properties
fbox(ax4, 0.3, 0.3, 9.4, 1.85, '#FDFEFE','#27AE60', lw=2)
ax4.text(5, 1.95, 'Key Predictions:', ha='center', fontsize=9,
         fontweight='bold', color='#1D6A39')
holo_props = [
    (r'+ $\Phi_{IIT}$ scales with cortical AREA not VOLUME', '#27AE60'),
    (r'+ Entanglement entropy = torsional RT formula', '#27AE60'),
    (r'+ Confirms IIT empirical area scaling (Tononi 2016)', '#27AE60'),
    (r'~ Requires AdS/CFT-like correspondence for brain', '#E67E22'),
]
for i, (p, col) in enumerate(holo_props):
    ax4.text(0.6, 1.5-i*0.30, p, fontsize=7.8, color=col, fontweight='bold')

# ============================================================================
# Main title
# ============================================================================
fig.suptitle('Dimensional Scenarios in TTH: Four Interpretations\n'
             'All scenarios predict identical observational signatures in Sec. V',
             fontsize=13, fontweight='bold', y=0.995,
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#2C3E50',
                       edgecolor='black', linewidth=2))
plt.gcf().get_axes()[0]  # ensure rendered

plt.savefig('/home/claude/tth_figures/figure10_dimensional_scenarios.pdf',
            dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig('/home/claude/tth_figures/figure10_dimensional_scenarios.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Figure 10 saved")
plt.close()
