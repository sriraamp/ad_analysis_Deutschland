import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/ads_germany_1000.csv")
sns.set(style="whitegrid")

def plot_platforms():
    platform_counts = df["Platform"].value_counts()
    platform_counts.plot(kind="barh", title="Top Advertising Platforms", figsize=(8,5))
    plt.tight_layout()
    plt.savefig("visuals/platforms.png")

if __name__ == "__main__":
    plot_platforms()
