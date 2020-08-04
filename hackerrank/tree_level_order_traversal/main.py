class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def levelOrder(root: Node) -> None:
    nodes = [root]
    result = str()

    while len(nodes) >= 1:
        next_nodes = list()
        for node in nodes:
            result += str(node.info) + ' '
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        # next iteration over remaining nodes
        nodes = next_nodes

    # remove last space
    print(result[:-1])


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
