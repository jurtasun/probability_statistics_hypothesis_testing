# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm, uniform, expon



# Plot styling
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



# Bernoulli distribution parameters
p = 0.5
x_vals = [0, 1]
y_vals = [1 - p, p]

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_vals, y_vals, width=0.4, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)
bars[1].set_color(highlight_color)
bars[1].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; p)$", fontsize=14)
ax.set_xticks([0, 1])
ax.set_xticklabels([r"$0$", r"$1$"], fontsize=13)
ax.set_yticks([p])
ax.set_yticklabels([fr"${p}$"], fontsize=13)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Square style
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(0, 1.0)
plt.tight_layout()

# Save and show
fig.savefig("bernoulli_1.png", dpi=300, bbox_inches='tight')
fig.savefig("bernoulli_1.pdf", bbox_inches='tight')
plt.show()



# Bernoulli distribution parameters
p = 0.166
x_vals = [0, 1]
y_vals = [1 - p, p]

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_vals, y_vals, width=0.4, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)
bars[1].set_color(highlight_color)
bars[1].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; p)$", fontsize=14)
ax.set_xticks([0, 1])
ax.set_xticklabels([r"$0$", r"$1$"], fontsize=13)
ax.set_yticks([p])
ax.set_yticklabels([fr"${p}$"], fontsize=13)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Square style
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(0, 1.0)
plt.tight_layout()

# Save and show
fig.savefig("bernoulli_2.png", dpi=300, bbox_inches='tight')
fig.savefig("bernoulli_2.pdf", bbox_inches='tight')
plt.show()



# Binomial distribution parameters
n, p = 10, 0.5
x_binom = np.arange(0, n + 1)
y_binom = binom.pmf(x_binom, n, p)

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_binom, y_binom, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Optionally highlight the mean value bar
mean_x = int(n * p)
bars[mean_x].set_color(highlight_color)
bars[mean_x].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; n, p)$", fontsize=14)
ax.set_xticks(np.arange(0, n + 1, 2))
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square style box
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-1, n + 1)
ax.set_ylim(0, max(y_binom) * 1.15)
plt.tight_layout()

# Save and show
fig.savefig("binomial_1.png", dpi=300, bbox_inches='tight')
fig.savefig("binomial_1.pdf", bbox_inches='tight')
plt.show()



# Binomial distribution parameters
n, p = 10, 0.5
x_binom = np.arange(0, n + 1)
y_binom = binom.pmf(x_binom, n, p)

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_binom, y_binom, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Highlight all bars from the mean and onward
mean_x = int(n * p)
for i in range(mean_x, n + 1):
    bars[i].set_color(highlight_color)
    bars[i].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; n, p)$", fontsize=14)
ax.set_xticks(np.arange(0, n + 1, 2))
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square style box
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-1, n + 1)
ax.set_ylim(0, max(y_binom) * 1.15)
plt.tight_layout()

# Save and show
fig.savefig("binomial_1_cum.png", dpi=300, bbox_inches='tight')
fig.savefig("binomial_1_cum.pdf", bbox_inches='tight')
plt.show()



# Binomial distribution parameters
n, p = 10, 0.166
x_binom = np.arange(0, n + 1)
y_binom = binom.pmf(x_binom, n, p)

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_binom, y_binom, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Optionally highlight the mean value bar
mean_x = int(n * p)
bars[mean_x].set_color(highlight_color)
bars[mean_x].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; n, p)$", fontsize=14)
ax.set_xticks(np.arange(0, n + 1, 2))
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square style box
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-1, n + 1)
ax.set_ylim(0, max(y_binom) * 1.15)
plt.tight_layout()

# Save and show
fig.savefig("binomial_2.png", dpi=300, bbox_inches='tight')
fig.savefig("binomial_2.pdf", bbox_inches='tight')
plt.show()



# Binomial distribution parameters
n, p = 10, 0.166
x_binom = np.arange(0, n + 1)
y_binom = binom.pmf(x_binom, n, p)

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_binom, y_binom, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Highlight all bars from the mean and onward
mean_x = int(n * p)
for i in range(mean_x, n + 1):
    bars[i].set_color(highlight_color)
    bars[i].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; n, p)$", fontsize=14)
ax.set_xticks(np.arange(0, n + 1, 2))
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square style box
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-1, n + 1)
ax.set_ylim(0, max(y_binom) * 1.15)
plt.tight_layout()

# Save and show
fig.savefig("binomial_2_cum.png", dpi=300, bbox_inches='tight')
fig.savefig("binomial_2_cum.pdf", bbox_inches='tight')
plt.show()



# Poisson distribution parameters
lambda_ = 5
x_poisson = np.arange(0, 20)
y_poisson = poisson.pmf(x_poisson, lambda_)

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_poisson, y_poisson, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Highlight the bar at the mean (λ)
mean_x = int(lambda_)
bars[mean_x].set_color(highlight_color)
bars[mean_x].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; \lambda)$", fontsize=14)
ax.set_xticks(np.arange(0, 20, 2))
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square frame
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-1, 20)
ax.set_ylim(0, max(y_poisson) * 1.15)
plt.tight_layout()

# Save and show
fig.savefig("poisson_1.png", dpi=300, bbox_inches='tight')
fig.savefig("poisson_1.pdf", bbox_inches='tight')
plt.show()



# Poisson distribution parameters
lambda_ = 5
x_poisson = np.arange(0, 20)
y_poisson = poisson.pmf(x_poisson, lambda_)

# Create plot
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_poisson, y_poisson, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Highlight all bars from the mean (λ) onward
mean_x = int(lambda_)
for i in range(mean_x, len(bars)):
    bars[i].set_color(highlight_color)
    bars[i].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; \lambda)$", fontsize=14)
ax.set_xticks(np.arange(0, 20, 2))
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square frame
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(-1, 20)
ax.set_ylim(0, max(y_poisson) * 1.15)
plt.tight_layout()

# Save and show
fig.savefig("poisson_1_cum.png", dpi=300, bbox_inches='tight')
fig.savefig("poisson_1_cum.pdf", bbox_inches='tight')
plt.show()



# Discrete Uniform distribution parameters
x_uniform = np.arange(1, 11)
y_uniform = np.ones_like(x_uniform) / len(x_uniform)

# Create plot (highlight one bin)
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_uniform, y_uniform, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Highlight the middle bar (mean location)
mean_x = len(x_uniform) // 2
bars[mean_x].set_color(highlight_color)
bars[mean_x].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; n)$", fontsize=14)
ax.set_xticks(x_uniform)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square style
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(0, len(x_uniform) + 1)
ax.set_ylim(0, 0.2)   # bars take half the axis height
plt.tight_layout()

# Save and show
fig.savefig("duniform_1.png", dpi=300, bbox_inches='tight')
fig.savefig("duniform_1.pdf", bbox_inches='tight')
plt.show()



# Discrete Uniform distribution parameters
x_uniform = np.arange(1, 11)
y_uniform = np.ones_like(x_uniform) / len(x_uniform)

# Create plot (highlight from mean onward)
fig, ax = plt.subplots(figsize=(7, 4.5))
bars = ax.bar(x_uniform, y_uniform, color=main_color, edgecolor='black', linewidth=1.0, alpha=0.7)

# Highlight from mean_x onward
mean_x = len(x_uniform) // 2
for i in range(mean_x, len(x_uniform)):
    bars[i].set_color(highlight_color)
    bars[i].set_alpha(0.8)

# Axis labels and ticks
ax.set_xlabel(r"$x$", fontsize=14)
ax.set_ylabel(r"$\mathbb{P}(X; \; n)$", fontsize=14)
ax.set_xticks(x_uniform)
ax.tick_params(axis='both', direction='in', length=4, width=1)

# Grid and formatting
ax.grid(True, linestyle='--', alpha=0.3)

# Square style
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1)

# Set limits and layout
ax.set_xlim(0, len(x_uniform) + 1)
ax.set_ylim(0, 0.2)   # bars take half the axis height
plt.tight_layout()

# Save and show
fig.savefig("duniform_1_cum.png", dpi=300, bbox_inches='tight')
fig.savefig("duniform_1_cum.pdf", bbox_inches='tight')
plt.show()