with open("input.txt", "r") as f:
    code = [line.strip() for line in f]


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

def create_circular_doubly_linked_list(start=0, end=99):

    head = Node(50)
    prev = head

    for value in range(start + 1, end + 1):
        if value+50 <= 99:
            node = Node(value+50)
            node.prev = prev
            prev.next = node
            prev = node
        else:
            node = Node(value-50)
            node.prev = prev
            prev.next = node
            prev = node

    prev.next = head
    head.prev = prev

    return head

def move_forward(current, steps):
    steps =  steps % 100
    for _ in range(steps):
        current = current.next
    return current

def move_backwards(current, steps):
    steps =  steps % 100
    for _ in range(steps):
        current = current.prev
    return current


example = create_circular_doubly_linked_list()


count = 0
print(example.value)
print(len(code))
for i in code:
    if i[0] == "L":
        n = int(i[1:])
        example = move_backwards(example, n)
    else:
        n = int(i[1:])
        example = move_forward(example, n)
    if example.value == 0:
        count += 1

print("pointed at 0 ", count, " times")
