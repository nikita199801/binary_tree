from bintree import BinTree


new_tree=BinTree()
new_treee=BinTree()
a=["f","w","b","e","a","t","u","l","d","z","s","q"]
b=["ф","а","в","б","е","ц","с"]
for x in b:
    new_tree.insert(x)
for x in a:
    new_treee.insert(x)
new_tree.printTree(new_tree.getRoot())
print("-"*20)
new_tree.printWrds(new_tree.getRoot())
print("-"*20)
new_treee.printTree(new_treee.getRoot())
print("-"*20)
new_treee.printWrds(new_treee.getRoot())



