class Queue:

    def __init__(self):
        """Constructor for Queue"""
        self.__capacity = 5
        self.__size = 0
        self.__front = 0
        self.__queue = [None for i in range(self.__capacity)]

    def __str__(self):
        """Converts queue into printable string"""
        out = "FRONT> "
        pointer = self.__front
        for i in range(self.__size):
            out += str(self.__queue[pointer]) + " "
            pointer = (pointer + 1) % self.__capacity

        return out + "<BACK"

    def __len__(self):
        """Returns the length of the queue"""
        return self.__size

    def first(self):
        """Returns the first element of the queue"""
        if self.__is_empty():
            raise IndexError("Queue is empty")
        else:
            return self.__queue[self.__front]

    def enqueue(self, item):
        """Adds item to the queue"""
        if self.__size == self.__capacity:
            self.__resize()
        self.__queue[(self.__front+self.__size)%self.__capacity] = item
        self.__size += 1

    def dequeue(self):
        """Removes and returns the first element of the queue"""
        if self.__is_empty():
            raise IndexError("Queue is empty")
        else:
            val = self.__queue[self.__front]
            self.__queue[self.__front] = None
            self.__front += 1
            self.__front %= self.__capacity
            self.__size -= 1
            return val

    def __is_empty(self):
        """Checks if the queue is empty"""
        if self.__size == 0:
            return True
        return False

    def __resize(self):
        """Resizes the queue when it reaches capacity"""
        cap = self.__capacity*2
        size = self.__size

        new = [None for i in range(cap)]
        for i in range(self.__size):
            new[i] = self.dequeue()

        self.__front = 0
        self.__size = size
        self.__capacity = cap
        self.__queue = new
