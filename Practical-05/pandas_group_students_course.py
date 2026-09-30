import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha"],
    "Course": ["BSc", "BCA", "BSc", "BCA"],
    "Marks": [80, 90, 70, 85]
}

df = pd.DataFrame(data)

result = df.groupby("Course")["Marks"].mean()

print(result)