import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from pathlib import Path

OUT_HERO = Path("figures/hero/tth_3d_hero.png")
OUT_GIF = Path("figures/gifs/tth_holofractal_animation.gif")

OUT_HERO.parent.mkdir(parents=True, exist_ok=True)
OUT_GIF.parent.mkdir(parents=True, exist_ok=True)

phi = (1 + np.sqrt(5)) / 2
delta = 4.669201609

theta = np.linspace(0, 10 * np.pi, 1800)
r = np.exp(0.035 * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)
z = 0.08 * theta * np.sin(theta / phi)

x2 = r * np.cos(theta + 2 * np.pi / 3)
y2 = r * np.sin(theta + 2 * np.pi / 3)
z2 = 0.08 * theta * np.sin(theta / phi + 2 * np.pi / 3)

x3 = r * np.cos(theta + 4 * np.pi / 3)
y3 = r * np.sin(theta + 4 * np.pi / 3)
z3 = 0.08 * theta * np.sin(theta / phi + 4 * np.pi / 3)


def draw_scene(ax, angle=35):
    ax.clear()

    ax.plot(x, y, z, linewidth=1.8, alpha=0.95)
    ax.plot(x2, y2, z2, linewidth=1.2, alpha=0.65)
    ax.plot(x3, y3, z3, linewidth=1.2, alpha=0.65)

    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)

    for scale, alpha in [(2.0, 0.08), (4.0, 0.06), (6.5, 0.045)]:
        xs = scale * np.outer(np.cos(u), np.sin(v))
        ys = scale * np.outer(np.sin(u), np.sin(v))
        zs = scale * 0.55 * np.outer(np.ones_like(u), np.cos(v))
        ax.plot_wireframe(xs, ys, zs, linewidth=0.25, alpha=alpha)

    ax.plot([0, 0], [0, 0], [-5, 5], linestyle="--", linewidth=1.0, alpha=0.7)
    ax.scatter([0], [0], [0], s=90, alpha=0.9)

    ax.text2D(
        0.03,
        0.94,
        "Torsional Holofractal Theory (TTH)",
        transform=ax.transAxes,
        fontsize=13,
        weight="bold",
    )
    ax.text2D(
        0.03,
        0.89,
        "φ-scaled holofractal coupling | δ-governed collapse dynamics",
        transform=ax.transAxes,
        fontsize=9,
    )
    ax.text2D(
        0.03,
        0.06,
        "Physical substrate → Holofractal field → Objective collapse → Phenomenal event",
        transform=ax.transAxes,
        fontsize=8,
    )

    ax.set_axis_off()
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_zlim(-5, 5)
    ax.view_init(elev=24, azim=angle)


fig = plt.figure(figsize=(12, 7), dpi=180)
ax = fig.add_subplot(111, projection="3d")
draw_scene(ax, angle=35)
plt.tight_layout()
plt.savefig(OUT_HERO, bbox_inches="tight", pad_inches=0.05)
plt.close(fig)

fig = plt.figure(figsize=(8, 5), dpi=120)
ax = fig.add_subplot(111, projection="3d")


def update(frame):
    draw_scene(ax, angle=frame)
    return fig,


ani = FuncAnimation(fig, update, frames=np.linspace(0, 360, 72), interval=70)
ani.save(OUT_GIF, writer=PillowWriter(fps=14))
plt.close(fig)

print(f"Saved: {OUT_HERO}")
print(f"Saved: {OUT_GIF}")