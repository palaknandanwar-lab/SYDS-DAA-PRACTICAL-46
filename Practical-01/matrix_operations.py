# Matrix Addition and Multiplication

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

A = []
B = []

print("\nEnter elements of Matrix A:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

print("\nEnter elements of Matrix B:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)

# --- Matrix Addition ---
print("\nAddition of Matrices (A + B):")
for i in range(rows):
    for j in range(cols):
        print(A[i][j] + B[i][j], end=" ")
    print()

# --- Matrix Multiplication ---
# Note: For A * B where both are (rows x cols), multiplication is valid ONLY if rows == cols
if rows != cols:
    print("\nMatrix multiplication requires a square matrix when using same dimensions.")
else:
    print("\nMultiplication of Matrices (A * B):")
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            total = 0
            for k in range(rows):  # k iterates through columns of A / rows of B
                total += A[i][k] * B[k][j]
            row.append(total)
        result.append(row)

    for i in range(rows):
        for j in range(cols):
            print(result[i][j], end=" ")
        print()