# @Time    : 2019/4/28 14:35
# @Author  : Noah
# @File    : tree_sort.py
# @Software: PyCharm
# @description: 树排序

class Node():
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val


def inOrder(root, res):
    if root:
        inOrder(root.left, res)
        res.append(root.val)
        inOrder(root.right, res)


def treeSort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = Node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order. 
    res = []
    inOrder(root, res)
    return res


if __name__ == "__main__":
    print(treeSort([10, 1, 3, 2, 9, 14, 13]))
