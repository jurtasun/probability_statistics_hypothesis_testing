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
figsize = (7, 4.5)



# Gaussian parameters
mu = 0     # mean
sigma = 1  # standard deviation
f = lambda x: (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# --- Plot: Gaussian PDF with vertical line on the mean ---
fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, f(x), color='black', lw=1.7, alpha=0.3)

# Vertical line at the mean
ax1.axvline(mu, color='firebrick', linestyle='--', linewidth=1.5)

# Hide spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# Arrows on axes
ax1.annotate("", xy=(x[-1] + 0.5, 0), xytext=(x[0], 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax1.annotate("", xy=(x[0], 0.45), xytext=(x[0], 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Axis labels and limits
ax1.set_xlim(x[0] - 0.5, x[-1] + 0.5)
ax1.set_ylim(-0.02, 0.45)
ax1.text(x[-1] + 0.4, -0.02, r"$x$", fontsize=14, ha='right', va='top')
ax1.text(x[0] - 0.4, 0.45, r"$f(x)$", fontsize=14, ha='left', va='bottom')

# Ticks and grid
ax1.tick_params(axis='both', direction='in', length=4, width=1)
ax1.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

fig1.savefig("gaussian_1.png", dpi=300, bbox_inches='tight')
fig1.savefig("gaussian_1.pdf", bbox_inches='tight')
plt.show()



# Gaussian parameters
mu = 0     # mean
sigma = 1  # standard deviation
f = lambda x: (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu)/sigma)**2)
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Integration limits
a, b = -1, 1
x_fill = np.linspace(a, b, 1000)
y_fill = f(x_fill)

# --- Plot: Gaussian PDF with area shaded between a and b ---
fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, f(x), color='black', lw=1.7, alpha=0.3)

# Fill area under the curve
ax1.fill_between(x_fill, y_fill, color='firebrick', alpha=0.3)

# Vertical lines at a and b
ax1.axvline(a, color='firebrick', linestyle='--', linewidth=1.5)
ax1.axvline(b, color='firebrick', linestyle='--', linewidth=1.5)

# Hide spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# Arrows on axes
ax1.annotate("", xy=(x[-1] + 0.5, 0), xytext=(x[0], 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax1.annotate("", xy=(x[0], 0.45), xytext=(x[0], 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Axis labels and limits
ax1.set_xlim(x[0] - 0.5, x[-1] + 0.5)
ax1.set_ylim(-0.02, 0.45)
ax1.text(x[-1] + 0.4, -0.02, r"$x$", fontsize=14, ha='right', va='top')
ax1.text(x[0] - 0.4, 0.45, r"$f(x)$", fontsize=14, ha='left', va='bottom')

# Ticks and grid
ax1.tick_params(axis='both', direction='in', length=4, width=1)
ax1.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

# Save and show
fig1.savefig("gaussian_2.png", dpi=300, bbox_inches='tight')
fig1.savefig("gaussian_2.pdf", bbox_inches='tight')
plt.show()



# Uniform distribution parameters
a, b = 1, 5
f = lambda x: np.where((x >= a) & (x <= b), 1/(b - a), 0)
x = np.linspace(0, 6, 1000)

# Mean value of the uniform distribution
mean = (a + b) / 2

# --- Plot: uniform PDF with vertical line on the mean ---
fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, f(x), color='black', lw=1.7, alpha=0.3)

# Vertical line at the mean
ax1.axvline(mean, color='firebrick', linestyle='--', linewidth=1.5)

# Hide spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# Arrows on axes
ax1.annotate("", xy=(6.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax1.annotate("", xy=(0, 0.35), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Labels and limits
ax1.set_xlim(-0.5, 6.5)
ax1.set_ylim(-0.02, 0.35)
ax1.text(6.3, -0.02, r"$x$", fontsize=14, ha='right', va='top')
ax1.text(-0.3, 0.35, r"$f(x)$", fontsize=14, ha='left', va='bottom')

ax1.tick_params(axis='both', direction='in', length=4, width=1)
ax1.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

# Save figure
fig1.savefig("uniform_1.png", dpi=300, bbox_inches='tight')
fig1.savefig("uniform_1.pdf", bbox_inches='tight')
plt.show()



# Uniform distribution parameters
a, b = 1, 5
f = lambda x: np.where((x >= a) & (x <= b), 1/(b - a), 0)
x = np.linspace(0, 6, 1000)

# Shading range
a_shade, b_shade = 3, 4
x_fill = np.linspace(a_shade, b_shade, 1000)
y_fill = f(x_fill)

# --- Plot: uniform PDF with shaded region from 3 to 4 ---
fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, f(x), color='black', lw=1.7, alpha=0.3)

# Fill area
ax1.fill_between(x_fill, y_fill, color='firebrick', alpha=0.3)

# Vertical lines at bounds
ax1.axvline(a_shade, color='firebrick', linestyle='--', linewidth=1.5)
ax1.axvline(b_shade, color='firebrick', linestyle='--', linewidth=1.5)

# Hide spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# Arrows on axes
ax1.annotate("", xy=(6.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax1.annotate("", xy=(0, 0.35), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Labels and limits
ax1.set_xlim(-0.5, 6.5)
ax1.set_ylim(-0.02, 0.35)
ax1.text(6.3, -0.02, r"$x$", fontsize=14, ha='right', va='top')
ax1.text(-0.3, 0.35, r"$f(x)$", fontsize=14, ha='left', va='bottom')

ax1.tick_params(axis='both', direction='in', length=4, width=1)
ax1.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

# Save figure
fig1.savefig("uniform_2.png", dpi=300, bbox_inches='tight')
fig1.savefig("uniform_2.pdf", bbox_inches='tight')
plt.show()



# Exponential PDF parameters
lambd = 1.0
f = lambda x: lambd * np.exp(-lambd * x)
x = np.linspace(0, 6, 1000)

# Mean value of the exponential distribution
mean = 1 / lambd

# --- Plot: exponential PDF with vertical line on the mean ---
fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, f(x), color='black', lw=1.7, alpha=0.3)

# Vertical line at the mean
ax1.axvline(mean, color='firebrick', linestyle='--', linewidth=1.5)

# Hide spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# Arrows on axes
ax1.annotate("", xy=(6.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax1.annotate("", xy=(0, 1.1), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Labels and limits
ax1.set_xlim(-0.5, 6.5)
ax1.set_ylim(-0.02, 1.1)
ax1.text(6.3, -0.02, r"$x$", fontsize=14, ha='right', va='top')
ax1.text(-0.3, 1.1, r"$f(x)$", fontsize=14, ha='left', va='bottom')

ax1.tick_params(axis='both', direction='in', length=4, width=1)
ax1.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

# Save figure
fig1.savefig("exponential_1.png", dpi=300, bbox_inches='tight')
fig1.savefig("exponential_1.pdf", bbox_inches='tight')
plt.show()


# Exponential PDF parameters
lambd = 1.0
f = lambda x: lambd * np.exp(-lambd * x)
x = np.linspace(0, 6, 1000)

# Shading range
a_shade, b_shade = 1, 3
x_fill = np.linspace(a_shade, b_shade, 1000)
y_fill = f(x_fill)

# --- Plot: exponential PDF with shaded region from 1 to 3 ---
fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, f(x), color='black', lw=1.7, alpha=0.3)

# Fill area
ax1.fill_between(x_fill, y_fill, color='firebrick', alpha=0.3)

# Vertical lines at bounds
ax1.axvline(a_shade, color='firebrick', linestyle='--', linewidth=1.5)
ax1.axvline(b_shade, color='firebrick', linestyle='--', linewidth=1.5)

# Hide spines
for spine in ax1.spines.values():
    spine.set_visible(False)

# Arrows on axes
ax1.annotate("", xy=(6.5, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))
ax1.annotate("", xy=(0, 1.1), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", lw=1.5, color='black'))

# Labels and limits
ax1.set_xlim(-0.5, 6.5)
ax1.set_ylim(-0.02, 1.1)
ax1.text(6.3, -0.02, r"$x$", fontsize=14, ha='right', va='top')
ax1.text(-0.3, 1.1, r"$f(x)$", fontsize=14, ha='left', va='bottom')

ax1.tick_params(axis='both', direction='in', length=4, width=1)
ax1.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()

# Save figure
fig1.savefig("exponential_2.png", dpi=300, bbox_inches='tight')
fig1.savefig("exponential_2.pdf", bbox_inches='tight')
plt.show()


