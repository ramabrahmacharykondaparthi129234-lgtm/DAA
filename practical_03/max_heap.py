heap = []

def insert(value):
    heap.append(value)
    
    i = len(heap) - 1
    
    while i > 0:
        parent = (i - 1) // 2
        
        if heap[i] > heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

insert(10)
insert(20)
insert(5)
insert(30)

print(heap)
