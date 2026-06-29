import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/patient.csv")

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

df["confirmed_date"] = pd.to_datetime(df["confirmed_date"])
df["released_date"] = pd.to_datetime(df["released_date"])

df["age"] = 2020 - df["birth_year"]

df["recovery_days"] = (
    df["released_date"] - df["confirmed_date"]
).dt.days

print("\nStatistics")
print(df.describe())

plt.figure(figsize=(6,4))
df["sex"].value_counts().plot(kind="bar", color=["skyblue","pink"])
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["age"].dropna(), bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Patients")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
df["country"].value_counts().plot(kind="bar")
plt.title("Country Distribution")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df["region"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Regions")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10,5))
df["infection_reason"].value_counts().plot(kind="bar")
plt.title("Infection Reasons")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,6))
df["state"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Patient State")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8,5))
plt.hist(df["recovery_days"].dropna(), bins=20)
plt.title("Recovery Time")
plt.xlabel("Days")
plt.ylabel("Patients")
plt.tight_layout()
plt.show()

numeric = df[
    [
        "birth_year",
        "age",
        "infection_order",
        "contact_number",
        "recovery_days",
    ]
]

plt.figure(figsize=(8,6))
sns.heatmap(
    numeric.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
