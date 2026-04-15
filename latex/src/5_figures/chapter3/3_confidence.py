import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm



# -------------------------------------------------
# Global styling (CLT / LLN consistent)
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
ci_fill_color = "#1f77b4"
figsize = (10, 4.5)

# -------------------------------------------------
# Parameters
# -------------------------------------------------
mu = 0
sigma = 1
alpha = 0.05
z = norm.ppf(1 - alpha / 2)

sample_sizes = [10, 50, 200]
titles = [r"$n=10$", r"$n=50$", r"$n=200$"]

M = 40  # number of intervals per panel
xlim = (-3, 3)
ylim = (-2, M + 2)

# -------------------------------------------------
# Figure
# -------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=figsize, sharex=True, sharey=True)

np.random.seed(0)

for ax, n, title in zip(axes, sample_sizes, titles):

    half_width = z * sigma / np.sqrt(n)

    # Critical (non-rejection) region for mu
    ax.axvspan(mu - half_width, mu + half_width,
               color=ci_fill_color, alpha=0.15)

    for i in range(M):
        sample = np.random.normal(mu, sigma, n)
        xbar = sample.mean()

        lower = xbar - half_width
        upper = xbar + half_width

        color = main_color if lower <= mu <= upper else highlight_color

        ax.plot([lower, upper], [i, i], color=color, lw=1.6)
        ax.plot(xbar, i, "o", color=color, markersize=4)

    # True mean
    ax.axvline(mu, color="black", linestyle="--", lw=1.5)

    # Box styling
    for spine in ax.spines.values():
        spine.set_linewidth(1)

    ax.set_title(title, fontsize=14)
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_yticks([])
    ax.tick_params(axis="both", direction="in", length=4, width=1)
    ax.grid(True, linestyle="--", alpha=0.3)

# Axis labels
axes[0].set_ylabel(r"$\mathrm{CI\ index}$", fontsize=14)
fig.supxlabel(r"$\mu$", fontsize=14)

plt.tight_layout()
fig.savefig("confidence_intervals.png", dpi=300, bbox_inches="tight")
fig.savefig("confidence_intervals.pdf", bbox_inches="tight")
plt.show()



# =================================================
# Sampling distribution of xbar with critical region
# =================================================
fig, axes = plt.subplots(1, 3, figsize=(10, 4.5), sharey=True)

np.random.seed(1)

for ax, n, title in zip(axes, sample_sizes, titles):

    # Sampling distribution of xbar
    M_hist = 10000
    xbar_samples = np.mean(
        np.random.normal(mu, sigma, size=(M_hist, n)),
        axis=1
    )

    # Histogram
    ax.hist(
        xbar_samples,
        bins=40,
        density=True,
        color=main_color,
        alpha=0.5
    )

    # True sampling density
    x_vals = np.linspace(mu - 4*sigma/np.sqrt(n),
                          mu + 4*sigma/np.sqrt(n), 1000)
    ax.plot(
        x_vals,
        norm.pdf(x_vals, mu, sigma / np.sqrt(n)),
        color="black",
        lw=1.5,
        alpha=0.8
    )

    # Critical (non-rejection) region for xbar
    hw = z * sigma / np.sqrt(n)
    ax.axvspan(mu - hw, mu + hw,
               color=main_color, alpha=0.15)

    # True mean
    ax.axvline(mu, color="black", linestyle="--", lw=1.5)

    # Styling
    for spine in ax.spines.values():
        spine.set_linewidth(1)

    ax.set_title(title, fontsize=14)
    ax.set_xlim(mu - 4*sigma/np.sqrt(n), mu + 4*sigma/np.sqrt(n))
    ax.tick_params(axis="both", direction="in", length=4, width=1)
    ax.grid(True, linestyle="--", alpha=0.3)

# Labels
axes[0].set_ylabel(r"$f_{\bar X}(x)$", fontsize=14)
fig.supxlabel(r"$\bar X$", fontsize=14)

plt.tight_layout()
fig.savefig("xbar_sampling_distribution.png", dpi=300, bbox_inches="tight")
fig.savefig("xbar_sampling_distribution.pdf", bbox_inches="tight")
plt.show()