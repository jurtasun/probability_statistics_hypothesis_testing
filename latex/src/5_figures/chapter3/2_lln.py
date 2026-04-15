import numpy as np
import matplotlib.pyplot as plt

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

main_color = "#1f77b4"
highlight_color = "firebrick"
figsize = (7, 4.5)

# -------------------------------------------------
# Parameters
# -------------------------------------------------
mu = 0
sigma = 1
size = 100

# Data
np.random.seed(42)
data = np.random.normal(mu, sigma, size)
running_mean = np.cumsum(data) / np.arange(1, size + 1)
trials = np.arange(1, size + 1)

# -------------------------------------------------
# Plot
# -------------------------------------------------
fig, ax = plt.subplots(figsize=figsize)

ax.plot(trials, running_mean, color=main_color, lw=1.7, alpha=0.8)
ax.axhline(mu, color=highlight_color, linestyle="--", lw=1.5)

# Box (square frame)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Limits
ax.set_xlim(0, 100)
# y_min = min(running_mean.min(), mu) - 0.5
# y_max = max(running_mean.max(), mu) + 0.5
y_min = 1
y_max = -1
ax.set_ylim(y_min, y_max)

# Labels (same typography as CLT)
ax.set_xlabel(r"$n$", fontsize=14)
ax.set_ylabel(r"$\bar{x}(n)$", fontsize=14)

# Ticks and grid
ax.tick_params(axis="both", direction="in", length=4, width=1)
ax.grid(True, linestyle="--", alpha=0.3)

plt.tight_layout()
fig.savefig("lln.png", dpi=300, bbox_inches="tight")
fig.savefig("lln.pdf", bbox_inches="tight")
plt.show()
