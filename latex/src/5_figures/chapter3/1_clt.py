# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm, uniform, expon

# -------------------------------------------------
# Styling
# -------------------------------------------------
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

# Colors
main_color = "#1f77b4"
highlight_color = 'firebrick'
figsize = (7, 4.5)


# Central Limit Theorem: Small to Large Sample Histograms

sample_sizes = [10, 100, 10000]
filenames = ["clt_1", "clt_2", "clt_3"]

# Normal distribution parameters
mu = 0
sigma = 1
bin_edges = np.linspace(mu - 4*sigma, mu + 4*sigma, 16)

for size, fname in zip(sample_sizes, filenames):

    # Generate Gaussian data
    np.random.seed(42)
    data = np.random.normal(loc=mu, scale=sigma, size=size)

    # Histogram
    fig, ax = plt.subplots(figsize=figsize)
    ax.hist(data, bins=bin_edges, density=True, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

    # Plot true Gaussian PDF
    x_vals = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y_vals = norm.pdf(x_vals, mu, sigma)
    ax.plot(x_vals, y_vals, 'k--', lw=1.5, alpha=0.8)

    # Axis labels
    ax.set_xlabel(r"$\bar{x}$", fontsize=14)
    ax.set_ylabel(r"Frequency", fontsize=14)

    # Ticks and grid
    ax.tick_params(axis='both', direction='in', length=4, width=1)
    ax.grid(True, linestyle='--', alpha=0.3)

    # Box styling
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_linewidth(1)

    # Limits
    ax.set_xlim(mu - 4*sigma, mu + 4*sigma)
    ax.set_ylim(0, max(ax.get_ylim()[1], 0.45 if size == 10 else 0.5))

    plt.tight_layout()
    fig.savefig(f"{fname}.png", dpi=300, bbox_inches='tight')
    fig.savefig(f"{fname}.pdf", bbox_inches='tight')
    plt.show()
