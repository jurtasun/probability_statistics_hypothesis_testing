# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2



# Parameters
df = 10
chi2_obs = 20
x = np.linspace(0, 30, 1000)



# --- ONE-TAILED PLOT ---
x_fill_one = np.linspace(chi2_obs, 30, 500)
y_fill_one = chi2.pdf(x_fill_one, df)
y = chi2.pdf(x, df)

fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, y, color='black', lw=2, label=f"Chi-square distribution ($\\nu={df}$)")
ax1.fill_between(x_fill_one, y_fill_one, color='crimson', alpha=0.4, label=r"p-value area ($\chi^2 > \chi^2_{\mathrm{obs}}$)")
ax1.axvline(chi2_obs, color='crimson', linestyle='--', linewidth=2, label=fr"$\chi^2_{{obs}} = {chi2_obs}$")

ax1.set_xlabel(r"$\chi^2$", fontsize=12)
ax1.set_ylabel(r"$\mathcal{f}\; (\chi^2;\ \nu=10)$", fontsize=14)
ax1.legend(frameon=False, fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.3)
for spine in ax1.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig1.savefig("chi2_test_one_tailed.png", dpi=300, bbox_inches='tight')
fig1.savefig("chi2_test_one_tailed.pdf", bbox_inches='tight')
plt.show()



# --- TWO-TAILED PLOT ---
alpha = 0.05
chi2_lower = chi2.ppf(alpha / 2, df)
chi2_upper = chi2.ppf(1 - alpha / 2, df)

x_fill_two_left = np.linspace(0, chi2_lower, 500)
y_fill_two_left = chi2.pdf(x_fill_two_left, df)
x_fill_two_right = np.linspace(chi2_upper, 30, 500)
y_fill_two_right = chi2.pdf(x_fill_two_right, df)

fig2, ax2 = plt.subplots(figsize=(7, 4.5))
ax2.plot(x, y, color='black', lw=2, label=f"Chi-square distribution ($\\nu={df}$)")
ax2.fill_between(x_fill_two_left, y_fill_two_left, color='crimson', alpha=0.4)
ax2.fill_between(x_fill_two_right, y_fill_two_right, color='crimson', alpha=0.4, label=r"two-tailed p-value area")
ax2.axvline(chi2_lower, color='crimson', linestyle='--', linewidth=2, label=fr"$\chi^2_{{lower}} = {chi2_lower:.2f}$")
ax2.axvline(chi2_upper, color='crimson', linestyle='--', linewidth=2, label=fr"$\chi^2_{{upper}} = {chi2_upper:.2f}$")

ax2.set_xlabel(r"$\chi^2$", fontsize=12)
ax2.set_ylabel(r"$\mathcal{f}\; (\chi^2;\ \nu=10)$", fontsize=14)
ax2.legend(frameon=False, fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.3)
for spine in ax2.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig2.savefig("chi2_test_two_tailed.png", dpi=300, bbox_inches='tight')
fig2.savefig("chi2_test_two_tailed.pdf", bbox_inches='tight')
plt.show()



# --- THIRD PLOT: Chi-square distribution for varying degrees of freedom ---
dfs = [1, 5, 10]
x = np.linspace(0.15, 20, 1000)

fig3, ax3 = plt.subplots(figsize=(7, 4.5))

for df in dfs:
    y = chi2.pdf(x, df)
    if df == 1:
        ax3.plot(x, y, lw=2, color='black', linestyle='-', label=fr"$\nu = {df}$")
    elif df == 5:
        ax3.plot(x, y, lw=2, color='crimson', linestyle='-', label=fr"$\nu = {df}$")
    else:  # df == 10
        ax3.plot(x, y, lw=2, color='black', linestyle='--', label=fr"$\nu = {df}$")

ax3.set_xlabel(r"$\chi^2$", fontsize=12)
ax3.set_ylabel(r"$\mathcal{f}\; (\chi^2;\ \nu)$", fontsize=14)
ax3.legend(frameon=True, fontsize=10, loc="upper right")
ax3.grid(True, linestyle='--', alpha=0.3)

for spine in ax3.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig3.savefig("chi2_distribution.png", dpi=300, bbox_inches='tight')
fig3.savefig("chi2_distribution.pdf", bbox_inches='tight')
plt.show()
