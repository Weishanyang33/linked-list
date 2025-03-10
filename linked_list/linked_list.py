
# Defines a node in the singly linked list
class Node:

    def __init__(self, value, next_node = None):
        self.value = value
        self.next = next_node

# Defines the singly linked list
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0# keep the head private. Not accessible outside this class

    # returns the value in the first node
    # returns None if the list is empty
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def get_first(self):
        if not self.head:
            return None
        return self.head.value


    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def add_first(self, value):
        new_node = Node(value, next_node=self.head)
        self.head = new_node
        self.size += 1

    # method to find if the linked list contains a node with specified value
    # returns true if found, false otherwise
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def search(self, value):
        current_node = self.head
        while current_node != None:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    # method that returns the length of the singly linked list
    # Time Complexity: O(1)
    # Space Complexity: O(1)
    def length(self):
        return self.size

    # method that returns the value at a given index in the linked list
    # index count starts at 0
    # returns None if there are fewer nodes in the linked list than the index value
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_at_index(self, index):
        if self.size < index:
            return None
        current_node = self.head
        current_index = 0
        while current_index != index:
            current_node = current_node.next
            current_index += 1
        if not current_node:
            return None
        return current_node.value

    # method that returns the value of the last node in the linked list
    # returns None if the linked list is empty
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def get_last(self):
        if not self.head:
            return None
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        return current_node.value

    # method that inserts a given value as a new last node in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def add_last(self, value):
        last_node = Node(value, next_node=None)
        if not self.head:
            self.head = last_node
            self.size += 1
            return 
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = last_node
        self.size += 1

    # method to return the max value in the linked list
    # returns the data value and not the node
    def find_max(self):
        max_value = 0
        if not self.head:
            return None
        current_node = self.head
        while current_node != None:
            max_value = max(max_value, current_node.value)
            current_node = current_node.next
        return max_value

    # method to delete the first node found with specified value
    # Time Complexity: O(n)(have to find the node first)
    # Space Complexity: O(1)
    def delete(self, value):
        if not self.head:
            return None
        current_node = self.head
        pre_node = None
        self.size -= 1
        while current_node.value != value:
            pre_node = current_node
            current_node = current_node.next
        if pre_node == None:
            self.head = current_node.next
        else:
            pre_node.next = current_node.next
            
                

    # method to print all the values in the linked list
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def visit(self):
        helper_list = []
        current = self.head

        while current:
            helper_list.append(str(current.value))
            current = current.next
        
        print(", ".join(helper_list))

    # method to reverse the singly linked list
    # note: the nodes should be moved and not just the values in the nodes
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverse(self):
        current_node = self.head
        pre_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = pre_node
            pre_node = current_node
            current_node = next_node
        self.head = pre_node
  
    ## Advanced/ Exercises
    # returns the value at the middle element in the singly linked list
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_middle_value(self):
        index = self.size // 2
        return self.get_at_index(index)

    # find the nth node from the end and return its value
    # assume indexing starts at 0 while counting to n
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def find_nth_from_end(self, n):
        if not self.head:
            return None
        if n >= self.size:
            return None
        index = self.size - n - 1
        return self.get_at_index(index)

    # checks if the linked list has a cycle. A cycle exists if any node in the
    # linked list links to a node already visited.
    # returns true if a cycle is found, false otherwise.
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def has_cycle(self):
        seen = set()
        current_node = self.head
        while current_node != None:
            if current_node in seen:
                return True
            seen.add(current_node)
            current_node = current_node.next
        return False

    # Helper method for tests
    # Creates a cycle in the linked list for testing purposes
    # Assumes the linked list has at least one node
    def create_cycle(self):
        if self.head == None:
            return

        # navigate to last node
        current = self.head
        while current.next != None:
            current = current.next

        current.next = self.head # make the last node link to first node
