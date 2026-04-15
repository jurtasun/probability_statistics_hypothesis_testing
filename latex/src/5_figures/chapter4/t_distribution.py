# Import libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, norm



# Parameters
df = 10
t_obs = 2.2
x = np.linspace(-4, 4, 1000)
y = t.pdf(x, df)



# --- ONE-TAILED PLOT ---
x_fill_one = np.linspace(t_obs, 4, 500)
y_fill_one = t.pdf(x_fill_one, df)

fig1, ax1 = plt.subplots(figsize=(7, 4.5))
ax1.plot(x, y, color='black', lw=2, label=f"$t$-distribution ($\\nu = {df}$)")
ax1.fill_between(x_fill_one, y_fill_one, color='crimson', alpha=0.4, label=r"p-value area ($t > t_{\mathrm{obs}}$)")
ax1.axvline(t_obs, color='crimson', linestyle='--', linewidth=2, label=fr"$t_{{obs}} = {t_obs}$")

ax1.set_xlabel("t", fontsize=12)
ax1.set_ylabel(r"$\mathcal{f}\; (t;\ \nu=10)$", fontsize=14)
ax1.legend(frameon=True, fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.3)
for spine in ax1.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig1.savefig("t_test_1_sample_p_one_tailed.png", dpi=300, bbox_inches='tight')
fig1.savefig("t_test_1_sample_p_one_tailed.pdf", bbox_inches='tight')
plt.show()



# --- TWO-TAILED PLOT ---
x_fill_two_left = np.linspace(-4, -t_obs, 500)
y_fill_two_left = t.pdf(x_fill_two_left, df)
x_fill_two_right = np.linspace(t_obs, 4, 500)
y_fill_two_right = t.pdf(x_fill_two_right, df)

fig2, ax2 = plt.subplots(figsize=(7, 4.5))
ax2.plot(x, y, color='black', lw=2, label=f"$t$-distribution ($\\nu = {df}$)")
ax2.fill_between(x_fill_two_left, y_fill_two_left, color='crimson', alpha=0.4)
ax2.fill_between(x_fill_two_right, y_fill_two_right, color='crimson', alpha=0.4, label=r"two-tailed p-value area")
ax2.axvline(t_obs, color='crimson', linestyle='--', linewidth=2)
ax2.axvline(-t_obs, color='crimson', linestyle='--', linewidth=2, label=fr"$\pm t_{{obs}} = \pm {t_obs}$")

ax2.set_xlabel("t", fontsize=12)
ax2.set_ylabel(r"$\mathcal{f}\; (t;\ \nu=10)$", fontsize=14)
ax2.legend(frameon=False, fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.3)
for spine in ax2.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig2.savefig("t_test_1_sample_p_two_tailed.png", dpi=300, bbox_inches='tight')
fig2.savefig("t_test_1_sample_p_two_tailed.pdf", bbox_inches='tight')
plt.show()



# --- THIRD PLOT: t-distribution for varying degrees of freedom ---
dfs = [1, 5, 100]
x = np.linspace(-5, 5, 1000)

fig3, ax3 = plt.subplots(figsize=(7, 4.5))

# Plot each t-distribution
for df_i in dfs:
    y = t.pdf(x, df_i)
    if df_i == 1:
        ax3.plot(x, y, lw=2, color='black', linestyle='-', label=fr"$\nu = {df_i}$")
    elif df_i == 5:
        ax3.plot(x, y, lw=2, color='crimson', linestyle='-', label=fr"$\nu = {df_i}$")
    else:  # df_i == 100
        ax3.plot(x, y, lw=2, color='black', linestyle='--', label=fr"$\nu = {df_i}$")

ax3.set_xlabel("t", fontsize=12)
ax3.set_ylabel(r"$\mathcal{f}\; (t;\ \nu)$", fontsize=14)
ax3.legend(frameon=False, fontsize=10)
ax3.grid(True, linestyle='--', alpha=0.3)

for spine in ax3.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

plt.tight_layout()
fig3.savefig("t_distribution.png", dpi=300, bbox_inches='tight')
fig3.savefig("t_distribution.pdf", bbox_inches='tight')
plt.show()
