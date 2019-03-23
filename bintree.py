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
            print(str(node.data) + " ")
            self.printTree(node.left)
            self.printTree(node.right)

    def printWrds(self,node):
        if node.flag == 0 :
           if node == self.root and ((node.left is not None and node.left.flag == 0)
                                     or (node.right is not None and node.right.flag == 0)):
               if node.left is not None and node.left.flag==0:
                   self.printWrds(node.left)
               elif node.right is not None and node.right.flag==0:
                   self.printWrds(node.right)
           else:
               if (node.left is not None and node.left.flag == 0) \
                       or (node.right is not None and node.right.flag == 0):
                   if node.left is not None and node.left.flag == 0:
                       self.word = self.word + node.data
                       self.printWrds(node.left)
                   elif node.right is not None and node.right.flag == 0:
                        self.word = self.word + node.data
                        self.printWrds(node.right)

               elif ((node.left is not None and node.left.flag == 1)
                     or (node.right is not None and node.right.flag == 1)):
                   self.word = ""
                   node.flag=1
                   self.printWrds(self.root)
               else:
                   node.flag=1
                   self.word =self.word + node.data
                   self._wordout()
                   self.printWrds(self.root)



    def getRoot(self):
        return self.root


    def _wordout(self):
        print(self.root.data+self.word)
        self.word = "" 