from bintree import BinTree


new_tree=BinTree()
# a=[17,45,2,1,5,11,22]
a=["f","w","b","e","a","t","u","l"]
for x in a:
    new_tree.insert(x)
new_tree.printTree(new_tree.getRoot())
print("-"*20)
new_tree.printWrds(new_tree.getRoot())
