from bintree import BinTree


new_tree=BinTree()
while True:
    choose = int(input("1. Ввести дерево \n"
          "2. Вывести дерево\n"
          "3. Вывести все возможные слова\n"
          "0. Выход\n"
          "Выберите пункт: "))
    if choose == 1:
        val=""
        while val !=" ":
            val=input("Введите узел: ")
            if val == " ":
                break
            else:
                new_tree.insert(val)
    elif choose == 2:
        new_tree.printTree(new_tree.getRoot())
    elif choose == 3:
        new_tree.printWrds(new_tree.getRoot())
        new_tree.nullFlag(new_tree.getRoot())
    elif choose == 0:
        break
new_tree.printTree(new_tree.getRoot())

# a=["f","w","b","e","a","t","u","l","d","z","s","q"]
# b=["ф","а","в","б","е","ц","с"]



