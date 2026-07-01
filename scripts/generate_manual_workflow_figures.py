from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.08,
})

COLORS = {
    'blue': '#dbeafe', 'blue_edge': '#2563eb',
    'green': '#dcfce7', 'green_edge': '#16a34a',
    'purple': '#f3e8ff', 'purple_edge': '#9333ea',
    'orange': '#ffedd5', 'orange_edge': '#ea580c',
    'cyan': '#e0f2fe', 'cyan_edge': '#0284c7',
    'gray': '#f8fafc', 'gray_edge': '#475569',
    'dark': '#0f172a'
}

def rounded_box(ax, xy, w, h, face, edge, lw=1.6, radius=0.06):
    x, y = xy
    box = FancyBboxPatch((x, y), w, h,
                         boxstyle=f'round,pad=0.025,rounding_size={radius}',
                         linewidth=lw, edgecolor=edge, facecolor=face)
    ax.add_patch(box)
    return box

def arrow(ax, x0, y0, x1, y1):
    ax.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle='-|>',
                                 mutation_scale=18, linewidth=1.6,
                                 color=COLORS['gray_edge'], shrinkA=5, shrinkB=5))

def draw_workflow():
    # Manual, non-generative diagram created in matplotlib.
    # The second box title is wrapped so it does not exceed the box width.
    fig, ax = plt.subplots(figsize=(12.8, 2.35))
    ax.set_xlim(0, 12.8)
    ax.set_ylim(0, 2.35)
    ax.axis('off')

    y = 0.55
    w, h = 2.05, 0.95
    xs = [0.20, 2.72, 5.24, 7.76, 10.28]
    items = [
        (COLORS['blue'], COLORS['blue_edge'], 'Input\nparameters', r'$a, q, b, L, N_r, N_\theta$'),
        (COLORS['green'], COLORS['green_edge'], 'Exact\nimage-charge', 'reference solution'),
        (COLORS['purple'], COLORS['purple_edge'], 'Legendre-series', 'solver'),
        (COLORS['orange'], COLORS['orange_edge'], 'Diagnostics', r'$E_L,\;\sigma,\;U,\;F_b$'),
        (COLORS['cyan'], COLORS['cyan_edge'], 'Figures, CSV data', 'and archive'),
    ]

    for i, (face, edge, title, subtitle) in enumerate(items):
        rounded_box(ax, (xs[i], y), w, h, face, edge, lw=1.8, radius=0.075)
        # Title: multiline titles use a slightly smaller size and centered vertical placement.
        title_fs = 10.0 if '\n' in title else 10.2
        ax.text(xs[i] + w/2, y + 0.61, title,
                ha='center', va='center', fontsize=title_fs,
                color=COLORS['dark'], weight='bold', linespacing=0.95)
        ax.text(xs[i] + w/2, y + 0.29, subtitle,
                ha='center', va='center', fontsize=9.6,
                color=COLORS['dark'])
        if i < len(xs) - 1:
            arrow(ax, xs[i] + w, y + h/2, xs[i+1], y + h/2)

    fig.savefig(OUT / 'figure_08_computational_workflow.pdf')
    fig.savefig(OUT / 'figure_08_computational_workflow.png', dpi=300)
    plt.close(fig)

def draw_icon(ax, kind, cx, cy, edge):
    ax.add_patch(Circle((cx, cy), 0.25, facecolor='white', edgecolor=edge, linewidth=1.4))
    if kind == 'notebook':
        ax.add_patch(Rectangle((cx-0.10, cy-0.14), 0.20, 0.28, facecolor='none', edgecolor=edge, linewidth=1.1))
        for yy in [-0.07, 0, 0.07]:
            ax.add_line(Line2D([cx-0.06, cx+0.06], [cy+yy, cy+yy], color=edge, linewidth=1.0))
    elif kind in ['csv', 'table']:
        ax.add_patch(Rectangle((cx-0.12, cy-0.12), 0.24, 0.24, facecolor='none', edgecolor=edge, linewidth=1.1))
        ax.add_line(Line2D([cx-0.04, cx-0.04], [cy-0.12, cy+0.12], color=edge, linewidth=1.0))
        ax.add_line(Line2D([cx+0.04, cx+0.04], [cy-0.12, cy+0.12], color=edge, linewidth=1.0))
        ax.add_line(Line2D([cx-0.12, cx+0.12], [cy, cy], color=edge, linewidth=1.0))
    elif kind == 'figure':
        ax.add_patch(Rectangle((cx-0.11, cy-0.12), 0.22, 0.24, facecolor='none', edgecolor=edge, linewidth=1.1))
        ax.add_line(Line2D([cx-0.08, cx-0.02, cx+0.04, cx+0.09], [cy-0.08, cy, cy-0.04, cy+0.08], color=edge, linewidth=1.2))
        ax.add_patch(Circle((cx+0.05, cy+0.05), 0.025, facecolor=edge, edgecolor=edge))
    elif kind == 'box':
        ax.add_patch(Rectangle((cx-0.13, cy-0.10), 0.26, 0.19, facecolor='none', edgecolor=edge, linewidth=1.1))
        ax.add_line(Line2D([cx-0.10, cx+0.10], [cy+0.04, cy+0.04], color=edge, linewidth=1.0))
    elif kind == 'readme':
        ax.add_patch(Rectangle((cx-0.13, cy-0.11), 0.11, 0.22, facecolor='none', edgecolor=edge, linewidth=1.1))
        ax.add_patch(Rectangle((cx+0.02, cy-0.11), 0.11, 0.22, facecolor='none', edgecolor=edge, linewidth=1.1))
        ax.add_line(Line2D([cx, cx], [cy-0.11, cy+0.11], color=edge, linewidth=1.0))
    elif kind == 'gear':
        ax.text(cx, cy, '*', ha='center', va='center', fontsize=18, color=edge, weight='bold')
        ax.add_patch(Circle((cx, cy), 0.07, facecolor='none', edgecolor=edge, linewidth=1.1))
    elif kind == 'code':
        ax.text(cx, cy, '</>', ha='center', va='center', fontsize=12, color=edge, weight='bold')
    elif kind == 'meta':
        ax.add_patch(Rectangle((cx-0.12, cy-0.13), 0.24, 0.26, facecolor='none', edgecolor=edge, linewidth=1.1))
        for yy in [0.04, -0.04]:
            ax.add_patch(Circle((cx-0.055, cy+yy), 0.025, facecolor=edge, edgecolor=edge))
            ax.add_line(Line2D([cx-0.015, cx+0.08], [cy+yy, cy+yy], color=edge, linewidth=1.0))
    elif kind == 'check':
        ax.plot([cx-0.11, cx-0.03, cx+0.12], [cy-0.01, cy-0.10, cy+0.10], color=edge, linewidth=2.0)

def draw_repro_structure():
    # Manual, non-generative diagram created in matplotlib.
    fig, ax = plt.subplots(figsize=(8.2, 6.1))
    ax.set_xlim(0, 8.2)
    ax.set_ylim(0, 6.1)
    ax.axis('off')
    rounded_box(ax, (2.25, 5.2), 3.7, 0.55, '#f8fafc', COLORS['blue_edge'], lw=1.8, radius=0.06)
    ax.text(4.10, 5.48, 'Reproducibility package', ha='center', va='center', fontsize=15.0, color=COLORS['dark'], weight='bold')
    arrow(ax, 4.1, 5.20, 4.1, 4.76)
    boxes = [
        (0.7, 4.05, COLORS['blue'], COLORS['blue_edge'], 'notebooks/', 'Reproduction notebook', 'notebook'),
        (4.35, 4.05, COLORS['cyan'], COLORS['cyan_edge'], 'figures/', 'PDF and PNG figures', 'figure'),
        (0.7, 3.20, COLORS['cyan'], COLORS['cyan_edge'], 'data/', 'Figure CSV data', 'csv'),
        (4.35, 3.20, COLORS['cyan'], COLORS['cyan_edge'], 'tables/', 'Table CSV data', 'table'),
        (0.7, 2.35, COLORS['gray'], COLORS['gray_edge'], 'output/', 'Regenerated outputs', 'box'),
        (4.35, 2.35, COLORS['green'], COLORS['green_edge'], 'README.md', 'Usage instructions', 'readme'),
        (0.7, 1.50, COLORS['orange'], COLORS['orange_edge'], 'requirements.txt', 'Dependencies', 'gear'),
        (4.35, 1.50, COLORS['purple'], COLORS['purple_edge'], 'scripts/', 'Regeneration scripts', 'code'),
        (0.7, 0.65, COLORS['green'], COLORS['green_edge'], 'metadata/', 'Run settings and reports', 'meta'),
        (4.35, 0.65, COLORS['orange'], COLORS['orange_edge'], 'tests/', 'Validation tests', 'check'),
    ]
    for x, y, face, edge, title, subtitle, kind in boxes:
        rounded_box(ax, (x, y), 3.05, 0.58, face, edge, lw=1.55, radius=0.06)
        draw_icon(ax, kind, x+0.35, y+0.29, edge)
        ax.text(x+0.72, y+0.38, title, ha='left', va='center', fontsize=12.0, color=COLORS['dark'], weight='bold')
        ax.text(x+0.72, y+0.17, subtitle, ha='left', va='center', fontsize=9.3, color='#334155')
    fig.savefig(OUT / 'figure_11_reproducibility_structure.pdf')
    fig.savefig(OUT / 'figure_11_reproducibility_structure.png', dpi=300)
    plt.close(fig)

if __name__ == '__main__':
    draw_workflow()
    draw_repro_structure()
    print('Created manual Python figures in', OUT)
