class Node():
    """A node class that stores a value and a pointer."""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def get_next(self):
        return self.next
    def set_next(self, next):
        self.next = next
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = data
class LinkedList():
    """A linked list of Nodes containing several methods for modifying itself. The last node must point to None."""
    def __init__(self, root=None):
        self.root = root
        self.size = 0 # TODO ADD SPECIFIC CODE TO SEPERATELY FIND LENGTH, AND ALSO ADD TO FUNCTIONS ADD, ADDTOEND
    def __getitem__(self, index):
        """This allows len(LinkedList) and iter(LinkedList), as well as list(LinkedList) to work. This also allows a LinkedList to be accessed in the form LinkedList[n]. Note: This will throw an IndexError if given a negative value."""
        if index >= self.size or index < 0:
            raise IndexError
        this_node = self.root
        for i in range(index):
            this_node = this_node.get_next()
        return this_node.get_data()
    @classmethod
    def toLinkedList(cls, lst):
        """Turns a regular list into a linked list."""
        out = LinkedList(root=Node(lst.pop(0)))
        for i in lst:
            out.addToEnd(Node(i))
        return out
    def add(self, data):
        """Adds a Node containing the input data to the start of the linked list."""
        self.root = Node(data, next=self.root)
        self.size += 1
    def remove(self, data):
        """Finds the first Node containing the input data, and removes it, but not any other Nodes."""
        this_node = self.root
        prev_node = None
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False
    def find(self, data):
        """Finds the first instance of the data in the linked list, and returns the full Node where the data is found."""
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return list(LinkedList(root=this_node))
            else:
                this_node = this_node.get_next()
        return None
    def addToEnd(self, data):
        """Adds a node containing the data to the end of the linked list."""
        this_node = self.root
        while this_node.get_next() != None:
            this_node = this_node.get_next()
        this_node.set_next(Node(data, None))
        self.size += 1
    def insert(self, data, index):
        """Inserts a Node at a specific index. Using an index equal to self.size inserts at the end of the list."""
        if index > self.size:
            raise IndexError
        this_node = self.root
        if index == 0:
            self.root = Node(data, self.root)
        else:
            for i in range(index - 1):
                this_node = this_node.get_next()
            this_node.set_next(Node(data, this_node.get_next()))
        self.size += 1
    def reverse(self):
        this_as_list = list(self)
        this_as_list.reverse()
        return LinkedList.toLinkedList(this_as_list)
    def rotate(self, k):
        this_as_list = list(self)
        temp1 = this_as_list[:-(k + 1)]
        temp2 = this_as_list[-(k + 1):]
        temp1.reverse()
        temp2.reverse()
        rotated = temp1 + temp2
        rotated.reverse()
        return rotated