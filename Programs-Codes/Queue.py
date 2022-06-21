class Queue:
    def __init__(self,qty):
        self.queue = [0]*qty
        self.head = 0
        self.tail = 0

    def insert(self,ele):
        if self.full():
            print("Queue is full")
            return
        self.queue[self.tail] = ele
        self.tail += 1
        if self.tail == len(self.queue):
            self.tail = 0

    def remove(self):
        if self.empty():
            print("Queue is empty")
            return
        self.head += 1
        if self.head == len(self.queue):
            self.head = 0

    def full(self):
        if (self.tail+1)%(len(self.queue)) == self.head:
            return True
        else:
            return False

    def empty(self):
        if self.head == self.tail:
            return True
        else:
            return False

    def print(self):
        i = self.head
        if self.empty():
            print("Queue is empty or destroyed")
        while self.queue[i] != 0:
            print(self.queue[i],end=" ")
            i += 1
            if i == len(self.queue):
                i = 0

    def destroy(self):
        self.head = self.tail = 0
        for i in range(len(self.queue)):
            self.queue[i] = 0
        
