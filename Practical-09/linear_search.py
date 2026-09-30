numbers = [10, 20, 30, 40, 50]

search = int(input("Enter number: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == search:
        print("Element found at position", i)
        found = True
        break

if not found:
    print("Element not found")