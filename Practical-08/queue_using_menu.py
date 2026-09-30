queue = []

while True:
    print("\n1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        queue.append(value)

    elif choice == 2:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Deleted:", queue.pop(0))

    elif choice == 3:
        print("Queue:", queue)

    elif choice == 4:
        break

    else:
        print("Invalid choice")