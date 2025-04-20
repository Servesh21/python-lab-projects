import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# 1. Number of independent and dependent variables
independent_vars = df.drop(columns=['math score'])  # Treat 'math score' as dependent
dependent_var = 'math score'

print("Columns:", df.columns.tolist())
print(f"Number of independent variables: {independent_vars.shape[1]}")
print("Number of dependent variables: 1 (math score)\n")

# 2. Display top 5 and last 5 rows
print("Top 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())

# 3. Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe(include='all'))

# 4. Independent variable with minimum average value (numeric only)
numeric_cols = df.select_dtypes(include=np.number).drop(columns=[dependent_var])
min_avg_col = numeric_cols.mean().idxmin()
print(f"\nIndependent variable with minimum average value: {min_avg_col}")

# 5. Independent variable with highest standard deviation
std_col = numeric_cols.std().idxmax()
print(f"Independent variable with highest std deviation: {std_col}")

# 6. Total count of missing values in each column
missing_vals = independent_vars.isnull().sum()
print("\nMissing values in each independent column:")
print(missing_vals)

# Visualize missing values
plt.figure(figsize=(10, 6))
sns.heatmap(independent_vars.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

# Identify column with maximum missing values
if missing_vals.sum() > 0:
    max_missing_col = missing_vals.idxmax()
    print(f"Independent variable with max missing values: {max_missing_col}")
else:
    print("✅ No missing values found in any independent variable.")

# 7. Replace missing values in one numeric column with mean
if 'reading score' in df.columns and df['reading score'].isnull().sum() > 0:
    df['reading score'].fillna(df['reading score'].mean(), inplace=True)
    print("Missing values in 'reading score' filled with column mean.\n")
else:
    print("✅ No missing values found in 'reading score'.\n")

# 8. Histogram for one independent variable
plt.figure(figsize=(8, 5))
sns.histplot(df['writing score'], bins=20, kde=True)
plt.title("Histogram: Writing Score")
plt.xlabel("Writing Score")
plt.ylabel("Frequency")
plt.show()

# 9. Boxplot to visualize outliers
plt.figure(figsize=(8, 5))
sns.boxplot(x=df['reading score'])
plt.title("Boxplot: Reading Score")
plt.show()

# 10. Line chart for correlation (e.g., reading score vs writing score)
plt.figure(figsize=(10, 5))
plt.plot(df['reading score'], df['writing score'], 'o-', alpha=0.5)
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.title("Line Chart: Reading vs Writing Score")
plt.show()

# 11. Correlation Matrix
corr_matrix = df.select_dtypes(include=np.number).corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

# Strongest positive and negative correlations
corr_pairs = corr_matrix.unstack().drop_duplicates()
corr_pairs = corr_pairs[corr_pairs.index.get_level_values(0) != corr_pairs.index.get_level_values(1)]

strong_pos = corr_pairs[corr_pairs < 1].idxmax()
neg_corrs = corr_pairs[corr_pairs < 0]
if not neg_corrs.empty:
    strong_neg = neg_corrs.idxmin()
else:
    strong_neg = None

print(f"\nStrongest positive correlation: {strong_pos}")
if strong_neg:
    print(f"Strongest negative correlation: {strong_neg}")
else:
    print("⚠️ No negative correlation found.")

# 12. Scatter plots for correlation
plt.figure(figsize=(12, 5))

# Positive correlation
plt.subplot(1, 2, 1)
sns.scatterplot(x=df[strong_pos[0]], y=df[strong_pos[1]])
plt.title(f"Positive Correlation: {strong_pos[0]} vs {strong_pos[1]}")

# Negative correlation (if exists)
if strong_neg:
    plt.subplot(1, 2, 2)
    sns.scatterplot(x=df[strong_neg[0]], y=df[strong_neg[1]])
    plt.title(f"Negative Correlation: {strong_neg[0]} vs {strong_neg[1]}")
else:
    plt.subplot(1, 2, 2)
    plt.text(0.5, 0.5, "No negative correlation found", fontsize=14, ha='center')
    plt.axis('off')

plt.tight_layout()
plt.show()
