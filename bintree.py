class Node():
    def __init__(self, data):
        self.left= self.right = None
        self.data = data


class BinTree():
    def __init__(self):
        self.root = None


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is not None:
                self._insert(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._insert(data, node.right)
            else:
                node.right = Node(data)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)


    def _printTree(self, node):
        if node is not None:
            self._printTree(node.left)
            print(str(node.data))
            self._printTree(node.right)

    def printWrds(self,node):
        if self.root is not None:
            curr = self.root
            print(self.root.data)
        while True:
            if curr.left is not None:
                curr=curr.left
                print(curr.left.data)
                self.printWrds(curr)





    # def _printWrds(self,node):
    #     if node.left is not None:
    #         if node.left is None:
    #             print(""+ str(node.right.data))
    #             self._printWrds(node.right)
    #         print(""+ str(node.left.data))
    #         self._printWrds(node.left)

        # elif node.right is not None:
        #     print(node.right.data)
        #     self._printWrds(node.right)



