class BinaryTree:
    
    def __init__(self, value = None):
        self.__left = None
        self.__right = None
        self.__value = value
    
    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self, value):
        self.__left = value

    @property
    def right(self):
        return self.__right
    @right.setter
    def right(self, value):
        self.__right = value

    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = value

    def isLeaf(self):
        return self != None and not self.__left and not self.__right
