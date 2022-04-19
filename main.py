class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"<Node: {self.value}>"


class BinaryTree:
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def add(self, element, node=None):
        if self.root is None:
            self.root = Node(element)
            return

        node = node or self.root
        if element < node.value:
            if node.left_child is None:
                node.left_child = Node(element)
            else:
                self.add(element, node.left_child)
        elif element >= node.value:
            if node.right_child is None:
                node.right_child = Node(element)
            else:
                self.add(element, node.right_child)

    def delete(self, element, node=None):
        if self.root is None:
            raise Exception
        else:
            node = node or self.root
            if node.value == element:
                node.value = None
                return
            else:
                if node.left_child:
                    self.delete(element, node.left_child)
                if node.right_child:
                    self.delete(element, node.right_child)

    def search(self, element, node=None):
        if self.root is None:
            raise Exception

        node = node or self.root
        if node.value == element:
            return True
        else:
            if node.left_child.value == element:
                return True
            elif node.right_child.value == element:
                return True
            else:
                self.search(element, node.left_child)
                self.search(element, node.right_child)
        return False

    def get_nodes_by(self, depth):
        if depth > self.get_length():
            raise Exception

        nodes = [self.root]
        current_depth = 1
        while current_depth < depth:
            new_nodes = []
            for node in nodes:
                if node.left_child:
                    new_nodes.append(node.left_child)
                else:
                    new_nodes.append(Node(None))
                if node.right_child:
                    new_nodes.append(node.right_child)
                else:
                    new_nodes.append(Node(None))
            current_depth += 1
            nodes = new_nodes
        return nodes

    def print(self):
        if self.root is None:
            print("Empty tree")
        else:
            start_width = 6 * self.get_width()
            print()
            print(f"Tree ({self.get_width()}, {self.get_length()})".center(start_width))
            print()
            print(f"{str(self.root.value).center(start_width)}")

            current_depth = 2
            while current_depth < self.get_length() + 1:
                current_nodes = self.get_nodes_by(current_depth)
                width = start_width // 2**(current_depth-1)
                for i, node in enumerate(current_nodes):
                    char = '/' if not i % 2 else '\\'
                    if node.value is not None:
                        print(char.center(width), end="")
                    else:
                        print("".center(width), end="")
                print()
                for node in current_nodes:
                    if node.value is not None:
                        print(f"{str(node.value).center(width)}", end="")
                    else:
                        print(f"{''.center(width)}", end="")
                print()
                current_depth += 1
            print()

    def get_length(self, node=None, current_length=0, max_length=0):
        if self.root is None:
            return 0
        else:
            node = node or self.root
            current_length += 1
            if current_length > max_length:
                max_length = current_length

            if node.left_child:
                max_length = self.get_length(node.left_child, current_length, max_length)

            if node.right_child:
                max_length = self.get_length(node.right_child, current_length, max_length)

            return max_length

    def get_width(self, node=None, current_width=0, max_width=0):
        if self.root is None:
            return 0
        else:
            node = node or self.root

            if node.left_child:
                current_width += 1
            if node.right_child:
                current_width += 1

            if current_width > max_width:
                max_width = current_width

            if node.left_child:
                max_width = self.get_length(node.left_child, current_width, max_width)

            if node.right_child:
                max_width = self.get_length(node.right_child, current_width, max_width)

            return max_width


class TrinaryTree(BinaryTree):
    pass


if __name__ == "__main__":
    bt = BinaryTree()
    bt.add(12)
    bt.add(5)
    bt.add(52)
    bt.add(4)
    bt.add(7)
    bt.print()
    # print(f"Tree length: {bt.get_length()}")
    # print(f"Tree width: {bt.get_width()}")
    # print(f"Nodes on depth 2: ", bt.get_nodes_by(2))
    # bt.add(63)
    # bt.add(11)
    # bt.print()
    while True:
        command, element = input("$ ").split()
        element = int(element)
        if command == "add":
            bt.add(element)
        elif command == "remove":
            bt.delete(element)
        else:
            print("Command not found.")
        bt.print()
