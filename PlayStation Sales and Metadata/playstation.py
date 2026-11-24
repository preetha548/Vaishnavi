
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print(" PLAYSTATION SALES DATA ANALYSIS")
print("=" * 60)

# 1. Load Dataset
df = pd.read_csv(
    "PlayStation Sales and Metadata (PS3PS4PS5) (Oct 2025).csv"
)

sns.set_theme(style="whitegrid")

# Convert columns
sales_cols = [
    "Total Shipped", "Total Sales", "NA Sales",
    "PAL Sales", "Japan Sales", "Other Sales"
]

for col in sales_cols + ["rating", "ratings_count", "metacritic"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Release Date"] = pd.to_datetime(
    df["Release Date"], errors="coerce"
)

df["Release Year"] = df["Release Date"].dt.year

# Clean text columns
for col in ["Console", "Publisher", "Developer", "genres"]:
    df[col] = df[col].fillna("Unknown")

print("\nDataset Shape:", df.shape)
print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nConsole Distribution:")
print(df["Console"].value_counts())

print("\nTop 10 Best-Selling Games:")
print(
    df.nlargest(10, "Total Sales")[
        ["Name", "Console", "Total Sales"]
    ]
)

# Chart 1: Console Distribution
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Console")
plt.title("1. PlayStation Console Distribution")
plt.savefig("chart_01_console_distribution.png")
plt.show()

# Chart 2: Total Sales by Console
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Console", y="Total Sales", estimator="sum")
plt.title("2. Total Sales by Console")
plt.savefig("chart_02_sales_by_console.png")
plt.show()

# Chart 3: Top 10 Games
top_games = df.nlargest(10, "Total Sales")
plt.figure(figsize=(12, 6))
sns.barplot(data=top_games, x="Total Sales", y="Name")
plt.title("3. Top 10 Best-Selling PlayStation Games")
plt.savefig("chart_03_top_games.png")
plt.show()

# Chart 4: Regional Sales
regional = df[
    ["NA Sales", "PAL Sales", "Japan Sales", "Other Sales"]
].sum()

plt.figure(figsize=(8, 5))
regional.plot(kind="bar")
plt.title("4. Regional Sales Comparison")
plt.ylabel("Sales")
plt.savefig("chart_04_regional_sales.png")
plt.show()

# Chart 5: Regional Sales Pie Chart
plt.figure(figsize=(7, 7))
regional.plot(kind="pie", autopct="%1.1f%%")
plt.title("5. Regional Sales Distribution")
plt.ylabel("")
plt.savefig("chart_05_regional_pie.png")
plt.show()

# Chart 6: Publisher Distribution
plt.figure(figsize=(12, 6))
df["Publisher"].value_counts().head(10).plot(kind="bar")
plt.title("6. Top 10 Game Publishers")
plt.ylabel("Number of Games")
plt.savefig("chart_06_publishers.png")
plt.show()

# Chart 7: Developer Distribution
plt.figure(figsize=(12, 6))
df["Developer"].value_counts().head(10).plot(kind="bar")
plt.title("7. Top 10 Game Developers")
plt.savefig("chart_07_developers.png")
plt.show()

# Chart 8: Game Ratings Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["rating"].dropna(), bins=20, kde=True)
plt.title("8. Game Ratings Distribution")
plt.savefig("chart_08_ratings.png")
plt.show()

# Chart 9: Metacritic Score Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["metacritic"].dropna(), bins=20, kde=True)
plt.title("9. Metacritic Score Distribution")
plt.savefig("chart_09_metacritic.png")
plt.show()

# Chart 10: Ratings vs Metacritic
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="rating", y="metacritic", alpha=0.6)
plt.title("10. User Ratings vs Metacritic Scores")
plt.savefig("chart_10_rating_metacritic.png")
plt.show()

# Chart 11: Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Total Sales"].dropna(), bins=30, kde=True)
plt.title("11. Total Game Sales Distribution")
plt.savefig("chart_11_sales_distribution.png")
plt.show()

# Chart 12: Sales Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["Total Sales"])
plt.title("12. Total Sales Boxplot")
plt.savefig("chart_12_sales_boxplot.png")
plt.show()

# Chart 13: Sales by Genre
genre_sales = df.assign(
    Genre=df["genres"].str.split(", ")
).explode("Genre")

plt.figure(figsize=(12, 6))
genre_sales.groupby("Genre")["Total Sales"].sum().nlargest(10).sort_values().plot(kind="barh")
plt.title("13. Top Genres by Total Sales")
plt.savefig("chart_13_genre_sales.png")
plt.show()

# Chart 14: Game Count by Genre
plt.figure(figsize=(12, 6))
genre_sales["Genre"].value_counts().head(10).plot(kind="bar")
plt.title("14. Top 10 Popular Game Genres")
plt.savefig("chart_14_genre_count.png")
plt.show()

# Chart 15: Sales by Release Year
year_sales = df.groupby("Release Year")["Total Sales"].sum()
plt.figure(figsize=(12, 5))
year_sales.plot(kind="line", marker="o")
plt.title("15. Sales Trends by Release Year")
plt.savefig("chart_15_year_sales.png")
plt.show()

# Chart 16: Game Releases by Year
plt.figure(figsize=(12, 5))
df["Release Year"].value_counts().sort_index().plot(kind="line", marker="o")
plt.title("16. Games Released by Year")
plt.savefig("chart_16_releases_year.png")
plt.show()

# Chart 17: Console vs Regional Sales
console_region = df.groupby("Console")[
    ["NA Sales", "PAL Sales", "Japan Sales", "Other Sales"]
].sum()

console_region.plot(kind="bar", figsize=(11, 6))
plt.title("17. Console-wise Regional Sales")
plt.savefig("chart_17_console_region.png")
plt.show()

# Chart 18: Sales Correlation Heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(
    df[sales_cols + ["rating", "metacritic"]].corr(),
    annot=True, cmap="coolwarm", fmt=".2f"
)
plt.title("18. Sales and Rating Correlation")
plt.savefig("chart_18_correlation.png")
plt.show()

# Chart 19: Rating by Console
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Console", y="rating")
plt.title("19. Ratings by Console")
plt.savefig("chart_19_rating_console.png")
plt.show()

# Chart 20: Metacritic by Console
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Console", y="metacritic")
plt.title("20. Metacritic Scores by Console")
plt.savefig("chart_20_metacritic_console.png")
plt.show()

# Chart 21: Top 10 Games by Rating
top_rating = df.nlargest(10, "rating")
plt.figure(figsize=(12, 6))
sns.barplot(data=top_rating, x="rating", y="Name")
plt.title("21. Top 10 Highest-Rated Games")
plt.savefig("chart_21_top_ratings.png")
plt.show()

# Chart 22: Top 10 Games by Metacritic
top_meta = df.nlargest(10, "metacritic")
plt.figure(figsize=(12, 6))
sns.barplot(data=top_meta, x="metacritic", y="Name")
plt.title("22. Top 10 Metacritic Games")
plt.savefig("chart_22_top_metacritic.png")
plt.show()

# Chart 23: Ratings Count Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["ratings_count"].dropna(), bins=30)
plt.title("23. Number of User Ratings")
plt.savefig("chart_23_ratings_count.png")
plt.show()

# Chart 24: Ratings Count vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="ratings_count", y="Total Sales")
plt.title("24. Ratings Count vs Total Sales")
plt.savefig("chart_24_ratings_sales.png")
plt.show()

# Chart 25: Top Publishers by Sales
plt.figure(figsize=(12, 6))
df.groupby("Publisher")["Total Sales"].sum().nlargest(10).sort_values().plot(kind="barh")
plt.title("25. Top Publishers by Sales")
plt.savefig("chart_25_publisher_sales.png")
plt.show()

# Chart 26: Top Developers by Sales
plt.figure(figsize=(12, 6))
df.groupby("Developer")["Total Sales"].sum().nlargest(10).sort_values().plot(kind="barh")
plt.title("26. Top Developers by Sales")
plt.savefig("chart_26_developer_sales.png")
plt.show()

# Chart 27: Total Shipped vs Total Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Total Shipped", y="Total Sales")
plt.title("27. Total Shipped vs Total Sales")
plt.savefig("chart_27_shipped_sales.png")
plt.show()

# Chart 28: Regional Sales Distribution
plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df[["NA Sales", "PAL Sales", "Japan Sales", "Other Sales"]]
)
plt.title("28. Regional Sales Boxplot")
plt.savefig("chart_28_region_boxplot.png")
plt.show()

# Chart 29: Average Rating by Genre
genre_rating = genre_sales.groupby("Genre")["rating"].mean().nlargest(10)

plt.figure(figsize=(12, 6))
genre_rating.sort_values().plot(kind="barh")
plt.title("29. Average Ratings by Genre")
plt.savefig("chart_29_genre_rating.png")
plt.show()

# Chart 30: Console Sales Share
console_sales = df.groupby("Console")["Total Sales"].sum()

plt.figure(figsize=(7, 7))
console_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("30. PlayStation Console Sales Share")
plt.ylabel("")
plt.savefig("chart_30_console_share.png")
plt.show()

# Export Cleaned Dataset
df.to_csv("playstation_cleaned_data.csv", index=False)

print("\n" + "=" * 60)
print("PLAYSTATION DATA ANALYSIS COMPLETED")
print("Total Charts Generated: 30")
print("Cleaned Dataset Exported Successfully")
print("=" * 60)
