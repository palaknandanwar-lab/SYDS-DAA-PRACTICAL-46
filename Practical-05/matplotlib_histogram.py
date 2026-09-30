import matplotlib.pyplot as plt

marks = [50, 60, 65, 70, 70, 75, 80, 85, 90, 95]

plt.hist(marks)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")

plt.show()