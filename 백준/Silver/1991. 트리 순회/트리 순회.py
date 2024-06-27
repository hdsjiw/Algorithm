class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def setRoot(self,node):
        self.root=node

    def getRoot(self):
        return self.root
    
    def makeNode(self,data,left,right):
        node=Node(data)
        node.left=left
        node.right=right
        return node

    def preorder(self,node):
        if node:
            print(node.data,end="")
            self.preorder(node.left)
            self.preorder(node.right)
            
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end="")
            self.inorder(node.right)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end="")
            
n = int(input())
tree = Tree()
nodes = {}

# 트리 노드 생성 및 연결
for i in range(n):
    key, left, right = input().split()
    if key not in nodes:
        nodes[key] = Node(key)
    if left != '.' and left not in nodes:
        nodes[left] = Node(left)
    if right != '.' and right not in nodes:
        nodes[right] = Node(right)
    
    nodes[key].left = nodes.get(left, None)
    nodes[key].right = nodes.get(right, None)

# print(nodes)

# 루트 노드 설정 (첫 번째 입력된 노드를 루트로 가정)
root_key = list(nodes.keys())[0]
tree.setRoot(nodes[root_key])

tree.preorder(tree.getRoot())
print()
tree.inorder(tree.getRoot())
print()
tree.postorder(tree.getRoot())