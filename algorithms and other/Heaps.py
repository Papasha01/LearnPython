class MinHeap:
    def __init__(self):
        """
        Initialize the MinHeap with an empty heap list and zero current size.
        """
        self.heap_list = [0]  # Initialize heap list with a dummy value
        self.current_size = 0  # Current size of the heap
 
    def sift_up(self, index):
        """
        Move the value up in the tree to maintain the heap property.
        """
        stop = False
        while (index // 2 > 0) and not stop:
            parent_index = index // 2
            if self.heap_list[index] < self.heap_list[parent_index]:
                # Swap the current element with its parent if it's smaller
                self.heap_list[index], self.heap_list[parent_index] = self.heap_list[parent_index], self.heap_list[index]
            else:
                stop = True
            index = parent_index
 
    def insert(self, value):
        """
        Insert a value into the heap.
        """
        self.heap_list.append(value)
        self.current_size += 1
        self.sift_up(self.current_size)  # Perform sift-up operation to maintain heap property
 
    def sift_down(self, index):
        """
        Move the value down in the tree to maintain the heap property.
        """
        while (index * 2) <= self.current_size:
            left_child_index = index * 2
            right_child_index = left_child_index + 1 if left_child_index + 1 <= self.current_size else None
            min_child_index = left_child_index
            
            if right_child_index is not None and self.heap_list[right_child_index] < self.heap_list[left_child_index]:
                min_child_index = right_child_index
            
            if self.heap_list[index] > self.heap_list[min_child_index]:
                # Swap the current element with its minimum child if it's greater
                self.heap_list[index], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[index]
            index = min_child_index
 
    def delete_min(self):
        """
        Remove and return the minimum value from the heap.
        """
        if len(self.heap_list) == 1:
            return 'Empty heap'
 
        root = self.heap_list[1]  # Minimum element is always at index 1
        self.heap_list[1] = self.heap_list[self.current_size]  # Move the last element to the root
        self.heap_list.pop()  # Remove the last element
        self.current_size -= 1
        self.sift_down(1)  # Perform sift-down operation to maintain heap property
        return root

# Create a MinHeap instance and insert some elements
my_heap = MinHeap()
my_heap.insert(5)
my_heap.insert(6)
my_heap.insert(7)
my_heap.insert(2)
my_heap.insert(13)
my_heap.insert(1)
my_heap.insert(10)

# Print the minimum element after deleting it
print(my_heap.delete_min())  # Output: 2
