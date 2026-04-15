# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters for plot
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Palatino", "Computer Modern Roman"],
    "mathtext.fontset": "cm",
    "axes.facecolor": "none",
    "figure.facecolor": "white",
})

# --- Estimators: balanced asymmetric density ---

# Parameters
mu = 1.0
sigma = 0.35
n = 12

# Sample
np.random.seed(2)
sample = np.random.normal(mu, sigma, n)
sample = sample[sample > 0]
xbar = sample.mean()

# x grid (positive, centred)
xg = np.linspace(0, 3.0, 1000)

# Asymmetric density (simple mixture)
pdf = (
    0.7 * np.exp(-(xg - mu)**2 / (2 * sigma**2)) +
    0.3 * np.exp(-(xg - 2.0)**2 / (2 * (0.6 * sigma)**2))
)

# Vertical rescaling for visual balance
pdf = 1.6 * pdf / pdf.max()

# Prepare plot
fig, ax = plt.subplots(figsize=(7, 4.5))

# Density with soft thickness
for offset in np.linspace(-0.03, 0.03, 5):
    ax.plot(xg, pdf + offset, color='black', lw=1.4, alpha=0.12)
ax.plot(xg, pdf, color='black', lw=1.7, alpha=0.35)

# Sample points (fewer crosses)
ax.scatter(sample[::2], np.zeros_like(sample[::2]),
           color='firebrick', marker='x', s=55, zorder=5)

# True parameter μ
ax.plot([mu, mu], [0, pdf.max()*1.05],
        color='black', lw=1.5)
ax.text(mu, -0.08, r"$\mu$", fontsize=13,
        ha='center', va='top')

# Sample mean x̄
ax.plot([xbar, xbar], [0, pdf.max()*1.05],
        color='firebrick', lw=1.5)
ax.text(xbar, -0.08, r"$\bar{x}$", fontsize=13,
        ha='center', va='top', color='firebrick')

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Axes arrows
ax.annotate("", xy=(3.1, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax.annotate("", xy=(0, 1.9), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Limits and labels
ax.set_xlim(0, 3.1)
ax.set_ylim(-0.2, 1.9)
ax.text(3.15, -0.22, r"$x$", fontsize=14, ha='right', va='top')
ax.text(-0.15, 1.9, r"$f(x)$", fontsize=14,
        ha='left', va='bottom')

# Grid and ticks
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='both', direction='in', length=4, width=1)
ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()

# Save figure
fig.savefig("estimators.png", dpi=300, bbox_inches='tight')
fig.savefig("estimators.pdf", bbox_inches='tight')
plt.show()
