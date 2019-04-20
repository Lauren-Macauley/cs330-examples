import copy


class LinkedList(object):
    """
    The LinkedList (LL) is a wrapper for three items.
     - Head pointer
     - Tail pointer
     - Node counter (cardinality)

    Only the head pointer is necessary, the latter three items are
    included for convenience.

    In this version, the LinkedList has been converted to a proper class
    """

    class Node(object):
        """
        The Node class is the atom--smallest base component--of a Linked List.
        An array element can viewed as its analog.

        For simplicity in this example, the Node will store an integers as
        data. In a later example, methods for generalizing this--through use of
        templates--will be utilized.
        """

        def __init__(self, data=0, next=None):
            self.__data = data
            self.__next = next

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, data):
            self.__data = data

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, nxt):
            self.__next = nxt

    class Iterator(object):
        """
        A special purpose Linked List Iterator
        """

        def __init__(self, node):
            self.__current_node = node

        def __next__(self):
            if self.__current_node is None:
                raise StopIteration

            next_val = (self.__current_node).data

            self.__current_node = (self.current_node).next

            return next_val

        @property
        def current_node(self):
            return self.__current_node

    def __init__(self):
        """
        Construct an empty Linked List
        """

        self.__head = None
        self.__tail = None
        self.__nodes = 0

    def append(self, to_add):
        """
        Add a Node at the end of the list
        """

        new_node = None

        # Store the "to_add" data within the node
        new_node = LinkedList.Node(data=to_add)

        # Handle the case where the first node is added
        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node

        else:
            # Add the new node to the this
            # What happens on the following two lines
            (self.__tail).next = new_node
            self.__tail = new_node

        # Increase the number of nodes
        self.__nodes += 1

        # Do not allow access to the node except
        # through the linked list
        # Is this line necessary?
        new_node = None

    def __len__(self):
        return self.__nodes

    def __iter__(self):
        return LinkedList.Iterator(self.__head)

    def __str__(self):
        """
        Iterate through the LinkedList and print each individual Node
        with an index.
        """

        return "\n".join(["Node # {:>4} - {:>4}".format(index, data)
                          for index, data in enumerate(self)])