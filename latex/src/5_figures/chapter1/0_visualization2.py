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



# Generate datasets
np.random.seed(0)
data_1 = np.random.normal(loc=-1, scale=1, size=100)
data_2 = np.random.normal(loc=0, scale=0.7, size=100)
data_3 = np.random.normal(loc=2, scale=1.2, size=100)
datasets = [data_1, data_2, data_3]
means = [np.mean(d) for d in datasets]
stds = [np.std(d) for d in datasets]

# --- Color palette consistent with histogram ---
colors = [ "#4a90e2", "mediumseagreen", "#d62728" ]  # same as histogram
x_labels = [r"$\mathcal{X}_1$", r"$\mathcal{X}_2$", r"$\mathcal{X}_3$"]

# --- 1. Violin Plot ---
fig, ax = plt.subplots(figsize=(7, 4.5))
parts = ax.violinplot(datasets, positions=[1, 2, 3], showmeans=False,
                      showextrema=False, showmedians=False)
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)
    pc.set_linewidth(1)

# Add mean line and std fill
for i, (mean, std) in enumerate(zip(means, stds), start=1):
    ax.fill_betweenx([mean - std, mean + std], i - 0.3, i + 0.3,
                     color='black', alpha=0.1)
    ax.hlines(mean, i - 0.3, i + 0.3, color='black', linestyle='-', linewidth=2, zorder=3)

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(x_labels, fontsize=13)
ax.set_ylabel("Observation", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)
ax.tick_params(axis='both', direction='in', length=4, width=1)
plt.tight_layout()
fig.savefig("mean_std_violin.png", dpi=300, bbox_inches='tight')
fig.savefig("mean_std_violin.pdf", bbox_inches='tight')
plt.show()
plt.close()

# --- 2. Box Plot ---
fig, ax = plt.subplots(figsize=(7, 4.5))
bp = ax.boxplot(datasets, patch_artist=True, positions=[1, 2, 3], widths=0.6,
                medianprops=dict(color='black', linewidth=1.5))
for i, box in enumerate(bp['boxes']):
    box.set(facecolor=colors[i], edgecolor='black', linewidth=1, alpha=0.6)
    ax.fill_betweenx([means[i] - stds[i], means[i] + stds[i]], i + 0.7, i + 1.3,
                     color='black', alpha=0.1)

ax.set_xticks([1, 2, 3])
ax.set_xticklabels(x_labels, fontsize=13)
ax.set_ylabel("Observation", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)
ax.tick_params(axis='both', direction='in', length=4, width=1)
plt.tight_layout()
fig.savefig("mean_std_box.png", dpi=300, bbox_inches='tight')
fig.savefig("mean_std_box.pdf", bbox_inches='tight')
plt.show()
plt.close()

# --- 3. Histogram ---
fig, ax = plt.subplots(figsize=(7, 4.5))
bins = np.linspace(-4, 4, 30)
for i, data in enumerate(datasets):
    ax.hist(data, bins=bins, alpha=0.5, label=x_labels[i], color=colors[i], edgecolor='black')

ax.legend(frameon=False, fontsize=11)
ax.set_xlabel("Observation", fontsize=13)
ax.set_ylabel("Frequency", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)
ax.tick_params(axis='both', direction='in', length=4, width=1)
plt.tight_layout()
fig.savefig("mean_std_hist.png", dpi=300, bbox_inches='tight')
fig.savefig("mean_std_hist.pdf", bbox_inches='tight')
plt.show()
plt.close()
