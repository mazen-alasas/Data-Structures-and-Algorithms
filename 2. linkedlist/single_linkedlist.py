

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end = " -> ")
            current_node = current_node.next
        print("None")
    
    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if not current_node:
            return
        prev_node.next = current_node.next
    
    def get_by_index(self, index):
        current_node = self.head
        idx = 0
        while current_node:
            if idx == index:
                return current_node.data
            idx += 1
            current_node = current_node.next
        return None
    
    def append_by_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        idx = 0
        while current_node and idx < index - 1:
            current_node = current_node.next
            idx += 1
        if not current_node:
            return
        new_node.next = current_node.next
        current_node.next = new_node

