import matplotlib.pyplot as plt

names = ["Rahul", "Priya", "Amit", "Sneha"]
marks = [75, 90, 65, 85]

plt.bar(names, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()