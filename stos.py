class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return(self.items.pop(0))

    def peek(self):
        return(self.items[0])

    def isEmpty(self):
        return (len(self.items) <= 0)

    def size(self):
        return( len(self.items) )

    def __str__(self):
        return str(self.items)
