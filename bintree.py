class Node():
    def __init__(self, data, flag):
        self.left= self.right = None
        self.data = data
        self.flag = flag


class BinTree():
    def __init__(self):
        self.root = None
        self.word=""
        self.root_flag=0


    def insert(self, data):
        if self.root is None:
            self.root = Node(data, 0)
        else:
            self._insert(data,self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is not None:
                self._insert(data, node.left)
            else:
                node.left = Node(data, 0)
        else:
            if node.right is not None:
                self._insert(data, node.right)
            else:
                node.right = Node(data, 0)


    def printTree(self, node):
        if node is not None:
            print(str(node.data) + " " + str(node.flag))
            self.printTree(node.left)
            self.printTree(node.right)

    def printWrds(self,node):
        self.root_flag=0
        while self.root_flag==0:
            if self.root_flag == 0:
                if node.left is not None or node.right is not None:
                    if node.left is not None and node.flag == 0:
                        self.word=self.word+node.left.data
                        self.printWrds(node.left)
                        print("func called")
                    else:
                        if node.right is not None and node.flag == 0:
                            self.word=self.word+node.right.data
                            self.printWrds(node.right)
                            print("func called")
                else:

                    print(node.data)
                    node.flag = 1
                    print(node.flag)
                    node=self.root
                    self.printWrds(node)
            else:
                self.root_flag=1
        self.wordout()

    def getRoot(self):
        return self.root


    def wordout(self):
        # if self.root.flag!=0:
        #     self.word = "clear"
        # else:
            print(self.root.data + self.word)

        # if self.root is not None:
        #     self._printTree(self.root)


    # def _printWrds(self,node):
        # if node.left is not None:
        #     # print(node.left)
        #     self.word=self.word+node.left
        #     if (node.left is not None) or (node.right is not None):
        #         # self._printWrds(node.left)
        #         pass



