import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 创建画布
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# 左侧：认知偏差
cognitive_biases = ["Authority Bias", "Urgency Effect", "Familiarity Heuristic", "Commitment Bias"]
for i, bias in enumerate(cognitive_biases):
    rect = patches.Rectangle((0.1, 0.6 - i*0.15), 0.3, 0.1, linewidth=1, edgecolor='black', facecolor='lightblue')
    ax.add_patch(rect)
    plt.text(0.25, 0.65 - i*0.15, bias, ha='center', va='center')

# 右侧：情境诱因
triggers = ["Fake Authority", "Time Pressure", "Spoofed UI", "Social Proof"]
for i, trigger in enumerate(triggers):
    rounded_rect = patches.FancyBboxPatch((0.6, 0.6 - i*0.15), 0.3, 0.1, boxstyle="round,pad=0.02", linewidth=1, edgecolor='black', facecolor='lightgreen')
    ax.add_patch(rounded_rect)
    plt.text(0.75, 0.65 - i*0.15, trigger, ha='center', va='center')

# 连接箭头
for i in range(4):
    plt.arrow(0.4, 0.65 - i*0.15, 0.15, 0, head_width=0.02, head_length=0.02, fc='gray', ec='gray')
    plt.arrow(0.6, 0.65 - i*0.15, -0.15, 0, head_width=0.02, head_length=0.02, fc='gray', ec='gray')
    plt.text(0.5, 0.62 - i*0.15, "Activates", fontsize=8, ha='center')
    plt.text(0.5, 0.58 - i*0.15, "Amplifies", fontsize=8, ha='center')

# 标题与注释
plt.text(0.5, 0.9, "Preliminary 'Cognitive-Context' Model", fontsize=12, ha='center')

plt.show()