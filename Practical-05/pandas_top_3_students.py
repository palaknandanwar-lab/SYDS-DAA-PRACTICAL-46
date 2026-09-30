import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Kiran"],
    "Marks": [75, 95, 65, 90, 85]
}

df = pd.DataFrame(data)

result = df.sort_values("Marks", ascending=False)

print(result.head(3))