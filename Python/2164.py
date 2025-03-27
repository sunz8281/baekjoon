from queue import Queue
q = Queue()

for i in range(1, int(input())+1):
    q.put(i)

while q.qsize() > 1:
    q.get()
    q.put(q.get())
print(q.get())