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
# Original normal sample
data_1 = np.random.normal(loc=0, scale=1, size=100)
mean_1 = np.mean(data_1)
std_1 = np.std(data_1)

# Skewed sample with outliers
data_2 = np.random.lognormal(mean=0.2, sigma=0.9, size=100) - 1.5
data_2 = np.append(data_2, [12])  # add a large outlier
mean_2 = np.mean(data_2)
std_2 = np.std(data_2)

# --- Color palette ---
light_blue = "#4a90e2"
highlight_color = "#d62728"
x_label_1 = r"$\mathcal{X}_1$"
x_label_2 = r"$\mathcal{X}_2$"

# Bin edges for smaller and larger bins
bins_large = np.linspace(-4, 6, 15)   # fewer, larger bins
bins_small = np.linspace(-4, 6, 60)   # more, smaller bins



# =========================
# 1. Violin Plots
# =========================



# Plot 1
fig, ax = plt.subplots(figsize=(7, 4.5))
parts = ax.violinplot([data_1], positions=[1], showmeans=False,
                      showextrema=False, showmedians=False)
for pc in parts['bodies']:
    pc.set_facecolor(light_blue)
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)
    pc.set_linewidth(1)
ax.fill_betweenx([mean_1 - std_1, mean_1 + std_1], 0.7, 1.3,
                 color='black', alpha=0.1)
ax.hlines(mean_1, 0.7, 1.3, color='black', linestyle='-', linewidth=2, zorder=3)
ax.set_xticks([1])
ax.set_xticklabels([x_label_1], fontsize=13)
ax.set_ylabel("Observation", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("violin_1.png", dpi=300, bbox_inches='tight')
fig.savefig("violin_1.pdf", bbox_inches='tight')
plt.show()
plt.close()



# Plot 2 (skewed)
fig, ax = plt.subplots(figsize=(7, 4.5))
parts = ax.violinplot([data_2], positions=[1], showmeans=False,
                      showextrema=False, showmedians=False)
for pc in parts['bodies']:
    pc.set_facecolor("mediumseagreen")
    pc.set_edgecolor('black')
    pc.set_alpha(0.7)
    pc.set_linewidth(1)
ax.fill_betweenx([mean_2 - std_2, mean_2 + std_2], 0.7, 1.3,
                 color='black', alpha=0.1)
ax.hlines(mean_2, 0.7, 1.3, color='black', linestyle='-', linewidth=2, zorder=3)
ax.set_xticks([1])
ax.set_xticklabels([x_label_2], fontsize=13)
ax.set_ylabel("Observation", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("violin_2.png", dpi=300, bbox_inches='tight')
fig.savefig("violin_2.pdf", bbox_inches='tight')
plt.show()
plt.close()



# =========================
# 2. Box Plots
# =========================



# Plot 1
fig, ax = plt.subplots(figsize=(7, 4.5))
bp = ax.boxplot([data_1], patch_artist=True, positions=[1], widths=0.6,
                medianprops=dict(color='black', linewidth=1.5))
for box in bp['boxes']:
    box.set(facecolor=light_blue, edgecolor='black', linewidth=1, alpha=0.6)
ax.fill_betweenx([mean_1 - std_1, mean_1 + std_1], 0.7, 1.3,
                 color='black', alpha=0.1)
ax.set_xticks([1])
ax.set_xticklabels([x_label_1], fontsize=13)
ax.set_ylabel("Observation", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("box_1.png", dpi=300, bbox_inches='tight')
fig.savefig("box_1.pdf", bbox_inches='tight')
plt.show()
plt.close()



# Plot 2 (skewed)
fig, ax = plt.subplots(figsize=(7, 4.5))
bp = ax.boxplot([data_2], patch_artist=True, positions=[1], widths=0.6,
                medianprops=dict(color='black', linewidth=1.5))
for box in bp['boxes']:
    box.set(facecolor="mediumseagreen", edgecolor='black', linewidth=1, alpha=0.6)
ax.fill_betweenx([mean_2 - std_2, mean_2 + std_2], 0.7, 1.3,
                 color='black', alpha=0.1)
ax.set_xticks([1])
ax.set_xticklabels([x_label_2], fontsize=13)
ax.set_ylabel("Observation", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("box_2.png", dpi=300, bbox_inches='tight')
fig.savefig("box_2.pdf", bbox_inches='tight')
plt.show()
plt.close()



# =========================
# 3. Histograms
# =========================



# Plot 1 (symmetric)
fig, ax = plt.subplots(figsize=(7, 4.5))
bins = np.linspace(-4, 6, 30)
ax.hist(data_1, bins=bins, alpha=0.7, color=light_blue, edgecolor='black')
ax.set_xlabel("Observation", fontsize=13)
ax.set_ylabel("Frequency", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("histogram_1.png", dpi=300, bbox_inches='tight')
fig.savefig("histogram_1.pdf", bbox_inches='tight')
plt.show()
plt.close()



# Plot 1 (symmetric) - large bins
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(data_1, bins=bins_large, alpha=0.7, color=light_blue, edgecolor='black')
ax.set_xlabel("Observation", fontsize=13)
ax.set_ylabel("Frequency", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("histogram_1_bins_large.png", dpi=300, bbox_inches='tight')
fig.savefig("histogram_1_bins_large.pdf", bbox_inches='tight')
plt.show()
plt.close()



# Plot 1 (symmetric) - small bins
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(data_1, bins=bins_small, alpha=0.7, color=light_blue, edgecolor='black')
ax.set_xlabel("Observation", fontsize=13)
ax.set_ylabel("Frequency", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("histogram_1_bins_small.png", dpi=300, bbox_inches='tight')
fig.savefig("histogram_1_bins_small.pdf", bbox_inches='tight')
plt.show()
plt.close()



# Plot 2 (skewed)
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(data_2, bins=bins, alpha=0.7, color="mediumseagreen", edgecolor='black')
ax.set_xlabel("Observation", fontsize=13)
ax.set_ylabel("Frequency", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("histogram_2.png", dpi=300, bbox_inches='tight')
fig.savefig("histogram_2.pdf", bbox_inches='tight')
plt.show()
plt.close()



# Plot 2 (skewed) - large bins
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(data_2, bins=bins_large, alpha=0.7, color="mediumseagreen", edgecolor='black')
ax.set_xlabel("Observation", fontsize=13)
ax.set_ylabel("Frequency", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("histogram_2_bins_large.png", dpi=300, bbox_inches='tight')
fig.savefig("histogram_2_bins_large.pdf", bbox_inches='tight')
plt.show()
plt.close()



# Plot 2 (skewed) - small bins
fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(data_2, bins=bins_small, alpha=0.7, color="mediumseagreen", edgecolor='black')
ax.set_xlabel("Observation", fontsize=13)
ax.set_ylabel("Frequency", fontsize=13)
ax.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
fig.savefig("histogram_2_bins_small.png", dpi=300, bbox_inches='tight')
fig.savefig("histogram_2_bins_small.pdf", bbox_inches='tight')
plt.show()
plt.close()