from math import log
import treePlotter
import DecisionTree
## 读取数据

fr = open('C:/Users/asus/Desktop/lenses.txt');
lists = []
labels = []
for line in fr.readlines():
    d = line.strip().split('\t')
    lists.append(d[:-1])
    labels.append(d[-1])
# print(lists)
# print(labels)
lensesTree = DecisionTree.createTree(lists,labels)
print(lensesTree)
treePlotter.createPlot(lensesTree)
DecisionTree.classify(lensesTree,labels,lists)
DecisionTree.storeTree(lensesTree,'store.txt')
