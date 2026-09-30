import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Marks": [75, 35, 65, 90]
}

df = pd.DataFrame(data)

df["Result"] = df["Marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

print(df)