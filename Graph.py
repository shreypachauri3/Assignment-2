import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Import result
data = pd.read_csv("result.csv")


# Display the table
print("Model Ranking Table:")
print(
    data[["Model", "Accuracy", "F1_Score", "Precision", "Recall", "Rank"]].sort_values(
        by="Rank"
    )
)

# Bar chart
labels = data["Model"]
num_models = len(labels)

# Parameters for bar chart
accuracy = data["Accuracy"]
f1_score = data["F1_Score"]
precision = data["Precision"]
recall = data["Recall"]
ranks = data["Rank"]

# Normalize ranks to a scale of 0 to 1 for better comparison
normalized_ranks = ranks / np.max(ranks)

# Plot the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

bar_width = 0.2
index = range(num_models)

ax.bar(index, accuracy, width=bar_width, label="Accuracy")
ax.bar(
    index,
    f1_score,
    width=bar_width,
    label="f1_score",
    bottom=accuracy,
)
ax.bar(
    index,
    precision,
    width=bar_width,
    label="Training Time",
    bottom=accuracy + f1_score,
)
ax.bar(
    index,
    recall,
    width=bar_width,
    label="Recall",
    bottom=accuracy + f1_score + precision,
)
ax.bar(
    index,
    normalized_ranks,
    width=bar_width,
    label="Normalized Rank",
    color="black",
    alpha=0.5,
)

ax.set_xticks(index)
ax.set_xticklabels(labels)
ax.set_ylabel("Metrics")
ax.set_title("Text Conversational Model Comparison")

ax.legend()
plt.savefig("BarChart.png")
plt.show()