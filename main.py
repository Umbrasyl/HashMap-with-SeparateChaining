class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for n in range(0, self.array_size)]

    def hash(self, key):
        hash_code = key.encode()
        return sum(hash_code)

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, node):
        array_index = self.compress(self.hash(node.key))
        # There are 2 possibilities: 1) Index is empty 2) Index has a linked list.
        if not self.array[array_index]:
            self.array[array_index] = LinkedList()
            self.array[array_index].add_head(node)
        else:
            self.array[array_index].push(node)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        # There are 3 possibilities: 1) Index is empty 2) Index has a list that contains the key
        #                            3) The list doesn't have the key
        if not self.array[array_index]:
            print("Sorry. That information doesn't exist.")
        else:
            target = self.array[array_index].retrieve_by_key(key)
            if not target:
                return None
            else:
                return target.value

    def print_map(self):
        holder_list = []
        for k in range(0, self.array_size):
            holder_list.append(self.array[k])
        for m in range(0, len(holder_list)):
            if holder_list[m]:
                holder_list[m] = holder_list[m].print_list()
        return holder_list


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, node):
        node.next_node = self.head
        self.head = node

    def push(self, node):
        pointer = self.head
        while pointer:
            if pointer.key == node.key:
                break
            pointer = pointer.next_node
        if not pointer:
            self.add_head(node)
        else:
            pointer.value = node.value

    def retrieve_by_key(self, key):
        pointer = self.head
        target = None
        if self.head.key == key:
            return self.head
        while pointer.next_node:
            if pointer.next_node.key == key:
                target = pointer.next_node
                pointer.next_node = target.next_node
        return target

    def print_list(self):
        holder_list = []
        pointer = self.head
        while pointer:
            holder_list.append([pointer.key, pointer.value])
            pointer = pointer.next_node
        return holder_list


flower_definitions = [['begonia', 'cautiousness'], ['chrysanthemum', 'cheerfulness'], ['carnation', 'memories'],
 ['daisy', 'innocence'], ['hyacinth', 'playfulness'], ['lavender', 'devotion'], ['magnolia', 'dignity'],
 ['morning glory', 'unrequited love'], ['periwinkle', 'new friendship'], ['poppy', 'rest'], ['rose', 'love'],
 ['snapdragon', 'grace'], ['sunflower', 'longevity'], ['wisteria', 'good luck']]
blossom = HashMap(len(flower_definitions))
for item in flower_definitions:
    blossom.assign(Node(item[0], item[1]))
print(blossom.print_map())
print(blossom.retrieve("daisy"))
