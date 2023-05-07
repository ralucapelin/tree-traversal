import pytest
from tree import Tree 
class TestTree:

    def test_find_existing_node(self):
        bst = Tree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(9)

        node = bst._find(3, bst.root)
        assert node is not None
        assert node.data == 3

    def test_find_nonexisting_node(self):
        bst = Tree()
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(1)
        bst.add(9)

        node = bst._find(4, bst.root)
        assert node is None
