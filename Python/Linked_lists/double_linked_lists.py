class DLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.previous = None

class DList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = DLNode(val)
        current_head = self.head
        new_node.next = current_head
        new_node.previous = None
        self.head = new_node	# SET the list's head TO the node we created in the last step
        return self	                # return self to allow for chaining

    def add_to_back(self, val):
        if self.head == None:	# if the list is empty
            self.add_to_front(val)	# run the add_to_front method
            return self	# let's make sure the rest of this function doesn't happen if we add to the front
        new_node = DLNode(val)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = new_node	# increment the runner to the next node in the list
        return self                 # return self to allow for chaining

    def print_values(self):
        runner = self.head
        while (runner != None):	# iterating while runner is a node and not None
            print(runner.value)
            runner = runner.next 	# set the runner to its neighbor
        return self	                # once the loop is done, return self to allow for chaining

    def remove_from_front(self):
        print(f"Removing {self.head.value} from the list")
        self.head = self.head.next
        return self

    def remove_from_back(self):
        runner = self.head
        while (runner.next != None):	# iterating while runner is a node and not None
            previous_runner = runner
            runner = runner.next
        print(f"Removing {runner.value} from the list")
        previous_runner.next = None
        return self
    
    def remove_val(self, val):
        if self.head.value == val:
            self.remove_from_front()
            return self
        runner = self.head
        while (runner.next != None and runner.value != val):	# iterating while runner is a node and not None
            previous_runner = runner
            runner = runner.next
        if (runner.next == None and runner.value == val):
            self.remove_from_back()
            return self
        print(f"Removing {runner.value} from the list")
        previous_runner.next = runner.next
        return self

    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        runner = self.head    
        x = 0
        while (runner.next != None and x<n):
            previous_runner = runner
            runner = runner.next
            x+=1
        if runner.next == None:
            self.add_to_back(val)
            return self
        new_node = DLNode(val)
        new_node.next = runner
        previous_runner.next = new_node
        return self