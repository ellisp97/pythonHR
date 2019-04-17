class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(self.size(),item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    
n = int(input())
q = Queue()
for i in range(n):
    query = list(map(int,input().split()))

    if int(query[0])==1:
        q.enqueue(query[1])
    elif int(query[0])==2:
        q.dequeue()
    elif int(query[0])==3:
        print(q[0])
