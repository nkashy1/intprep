class MyStack(object):
    def __init__(self):
        self.base = []

    def isEmpty(self):
        return len(self.base) == 0

    def peek(self):
        if not self.isEmpty():
            return self.base[-1]
        return None

    def push(self, item):
        self.base.append(item)

    def pop(self):
        return self.base.pop()
