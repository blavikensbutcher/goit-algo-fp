class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: 'Node | None' = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur:
            prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev       
            prev = current         
            current = next_node       
        self.head = prev

    def sort_insertion(self):
        sorted_head = None
        current = self.head

        while current:
            next_node = current.next
            if sorted_head is None or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node

        self.head = sorted_head

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")



def merge_sorted_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    merged = LinkedList()
    dummy = Node()
    tail = dummy

    p1 = list1.head
    p2 = list2.head

    while p1 and p2:
        if p1.data < p2.data:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    tail.next = p1 if p1 else p2
    merged.head = dummy.next
    return merged



llist = LinkedList()
for value in [15, 10, 5, 20, 25]:
    llist.insert_at_end(value)

print("🔹 Початковий список:")
llist.print_list()

llist.reverse()
print("\n🔁 Після реверсу:")
llist.print_list()

llist.sort_insertion()
print("\n🔃 Після сортування вставками:")
llist.print_list()

# Другий список
llist2 = LinkedList()
for value in [7, 12, 30]:
    llist2.insert_at_end(value)
llist2.sort_insertion()

# Злиття
merged = merge_sorted_lists(llist, llist2)
print("\n🔗 Злиття двох відсортованих списків:")
merged.print_list()