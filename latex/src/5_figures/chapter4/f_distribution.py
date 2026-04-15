# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f



# Parameters
df1 = 5
df2 = 10
F_obs = 2.5
x = np.linspace(0, 5, 1000)

# --- ONE-TAILED PLOT ---
x_fill_one = np.linspace(F_obs, 5, 500)
y_fill_one = f.pdf(x_fill_one, df1, df2)
y = f.pdf(x, df1, df2)

fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, y, color='black', lw=2, label=f"F-distribution ($\\nu_1={df1},\\ \\nu_2={df2}$)")
ax1.fill_between(x_fill_one, y_fill_one, color='crimson', alpha=0.4, label=r"p-value area ($F > F_{\mathrm{obs}}$)")
ax1.axvline(F_obs, color='crimson', linestyle='--', linewidth=2, label=fr"$F_{{obs}} = {F_obs}$")

ax1.set_xlabel("F", fontsize=12)
ax1.set_ylabel(r"$\mathcal{f}\; (F;\ \nu_1=5,\ \nu_2=10)$", fontsize=14)
ax1.legend(frameon=False, fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.3)
for spine in ax1.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig1.savefig("f_test_one_tailed.png", dpi=300, bbox_inches='tight')
fig1.savefig("f_test_one_tailed.pdf", bbox_inches='tight')
plt.show()



# --- TWO-TAILED PLOT ---
alpha = 0.05
F_lower = f.ppf(alpha / 2, df1, df2)
F_upper = f.ppf(1 - alpha / 2, df1, df2)

x_fill_two_left = np.linspace(0, F_lower, 500)
y_fill_two_left = f.pdf(x_fill_two_left, df1, df2)
x_fill_two_right = np.linspace(F_upper, 5, 500)
y_fill_two_right = f.pdf(x_fill_two_right, df1, df2)

fig2, ax2 = plt.subplots(figsize=(7, 4.5))
ax2.plot(x, y, color='black', lw=2, label=f"F-distribution ($\\nu_1={df1},\\ \\nu_2={df2}$)")
ax2.fill_between(x_fill_two_left, y_fill_two_left, color='crimson', alpha=0.4)
ax2.fill_between(x_fill_two_right, y_fill_two_right, color='crimson', alpha=0.4, label=r"two-tailed p-value area")
ax2.axvline(F_lower, color='crimson', linestyle='--', linewidth=2, label=fr"$F_{{lower}} = {F_lower:.2f}$")
ax2.axvline(F_upper, color='crimson', linestyle='--', linewidth=2, label=fr"$F_{{upper}} = {F_upper:.2f}$")

ax2.set_xlabel("F", fontsize=12)
ax2.set_ylabel(r"$\mathcal{f}\; (F;\ \nu_1=5,\ \nu_2=10)$", fontsize=14)
ax2.legend(frameon=False, fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.3)
for spine in ax2.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig2.savefig("f_test_two_tailed.png", dpi=300, bbox_inches='tight')
fig2.savefig("f_test_two_tailed.pdf", bbox_inches='tight')
plt.show()



# --- THIRD PLOT: F-distribution for varying degrees of freedom ---
dfs1 = [1, 5, 10]
dfs2 = [5, 10, 30]
x = np.linspace(0.01, 2.2, 1000)

fig3, ax3 = plt.subplots(figsize=(7, 4.5))

for num_df, den_df in zip(dfs1, dfs2):
    y = f.pdf(x, num_df, den_df)
    if num_df == 1:
        ax3.plot(
            x, y, lw=2, color='black', linestyle='-',
            label=fr"$\nu_1={num_df},\ \nu_2={den_df}$"
        )
    elif num_df == 5:
        ax3.plot(
            x, y, lw=2, color='crimson', linestyle='-',
            label=fr"$\nu_1={num_df},\ \nu_2={den_df}$"
        )
    else:  # num_df == 10
        ax3.plot(
            x, y, lw=2, color='black', linestyle='--',
            label=fr"$\nu_1={num_df},\ \nu_2={den_df}$"
        )

ax3.set_xlabel("F", fontsize=12)
ax3.set_ylabel(r"$\mathcal{f}\; (F;\ \nu_1, \nu_2)$", fontsize=14)
ax3.legend(frameon=True, fontsize=10, loc="upper right")
ax3.grid(True, linestyle='--', alpha=0.3)

for spine in ax3.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig3.savefig("f_distribution.png", dpi=300, bbox_inches='tight')
fig3.savefig("f_distribution.pdf", bbox_inches='tight')
plt.show()
