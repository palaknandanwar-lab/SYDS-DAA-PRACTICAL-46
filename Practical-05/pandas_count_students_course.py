import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Course": ["BSc", "BCA", "BSc", "BCA"]
}

df = pd.DataFrame(data)

print(df["Course"].value_counts())