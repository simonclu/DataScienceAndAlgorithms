class Node(object):
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
class LinkedList(object):
    """A linked list of Nodes containing several methods for modifying itself. The last node must point to None."""
    def __init__(self, root=None):
        self.root = root
        self.size = 0
    def get_size(self):
        return self.size
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
                return this_node
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
        self.size += 1 # TODO debug
    def __list__(self):
        """Overrides the list(LinkedList) function so that it will work properly."""
        out = []
        this_node = self.root
        while this_node != None:
            out.append(this_node.get_data())
        return out
    @classmethod
    def toLinkedList(cls, lst):
        """Turns a regular list into a linked list."""
        out = LinkedList(Node(lst.pop(0)))
        for i in lst:
            out.addToEnd(Node(i))
        return out