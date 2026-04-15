import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib as mpl

# Elegant serif font
mpl.rcParams['font.family'] = 'serif'

# Figure and axis
fig, ax = plt.subplots(figsize=(9.5, 3.5))
ax.axis("off")

# Arrow parameters
arrow_y_top = 0.62
arrow_y_bottom = 0.38
arrow_x_start = 0.28
arrow_x_end = 0.72
label_y_center = 0.5

# Text labels
ax.text(0.5, 0.83, "prediction (probability)", fontsize=13, ha='center', va='bottom')
ax.text(0.5, 0.17, "inference (statistics)", fontsize=13, ha='center', va='top')

# Arrows
ax.annotate("",
            xy=(arrow_x_end, arrow_y_top), xytext=(arrow_x_start, arrow_y_top),
            arrowprops=dict(arrowstyle="->", lw=2, color='black'))

ax.annotate("",
            xy=(arrow_x_start, arrow_y_bottom), xytext=(arrow_x_end, arrow_y_bottom),
            arrowprops=dict(arrowstyle="->", lw=2, color='black'))

# Theory and Experiment
ax.text(arrow_x_start - 0.05, label_y_center, "theory", fontsize=14, ha='right', va='center')
ax.text(arrow_x_end + 0.05, label_y_center, "experiment", fontsize=14, ha='left', va='center')

# Black square border
border = patches.Rectangle((0, 0), 1, 1,
                           linewidth=2, edgecolor='black', facecolor='none',
                           transform=ax.transAxes, clip_on=False)
ax.add_patch(border)

# Subtle margins—closer to the original version
plt.subplots_adjust(left=0.14, right=0.86, top=0.90, bottom=0.10)

# Save the figure
plt.savefig("probability_vs_statistics.png", dpi=300, bbox_inches='tight')
plt.savefig("probability_vs_statistics.pdf", bbox_inches='tight')
plt.show()
