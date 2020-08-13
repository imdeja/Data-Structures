class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next_node = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, data):
        # 1. create the Node from the value 
        new_node = Node(data)
        # So, what do we do if tail is None? 
        # What's the rule we want to set to indicate that the linked
        # list is empty? 
        # Would it be better to check the head? 
        # Let's check them both: an empty linked list has an empty 
        # head and an empty tail 
        if not self.head and not self.tail:
            # in a one-element linked list, what should head and tail 
            # be referring to? 
            # have both head and tail referring to the single node 
            self.head = new_node
            # set the new node to be the tail 
            self.tail = new_node
        else:
            # These steps assume that the tail is already referring
            # to a Node 
            # 2. set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node 
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        # set self.head to the Node after the head 
        data = self.head.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list 
        if self.head is self.tail:
            # delete the linked list's head + tail reference 
            self.head = None
            self.tail = None
        else:
            # we have more than one Node in the linked list 
            # delete the head Node 
            # update `self.head` to refer to the Node after the Node we just deleted
            self.head = self.head.get_next()

        return data

    def remove_tail(self):
        if self.tail is None:
            return None
        # save the tail Node's data
        data = self.tail.get_value()
        # both head and tail refer to the same Node
        # there's only one Node in the linked list
        if self.head is self.tail:
            # delete the linked list's head + tail reference 
            self.head = None
            self.tail = None
        else:
            # in order to update `self.tail` to point to the
            # the Node _before_ the tail, we need to traverse
            # the whole linked list starting from the head,
            # because we cannot move backwards from any one
            # Node, so we have to start from the beginning
            current = self.head

            # traverse until we get to the Node right
            # before the tail Node
            while current.get_next() != self.tail:
                current = current.get_next()

            # `current` is now pointing at the Node right
            # before the tail Node
            self.tail = current
            self.tail.set_next(None) 

        return data

    def contains(self, data):
        if not self.head:
            return False

        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head 

        # check to see if we're at a valid node 
        while current is not None:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == data:
                return True
            # update our current node to the current node's next node
            current = current.get_next()

        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if self.head is None:
            return None
        # reference to the largest value we've seen so far
        max_so_far = self.head.get_value()
        # check to see if we're still at a valid list node
        current = self.head.get_next()

        while current is not None:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_so_far:
                # if so, update our max_value variable
                max_so_far = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()

        return max_so_far