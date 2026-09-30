class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


stack = None

# Push 10
new_node = Node(10)
new_node.next = stack
stack = new_node

# Push 20
new_node = Node(20)
new_node.next = stack
stack = new_node

# Display
current = stack

while current:
    print(current.data)
    current = current.next