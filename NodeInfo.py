class NodeInfo:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.is_left_visited = False
        self.is_right_visited = False

    def set_left_child(self,node):
        self.left = node

    def set_right_child(self,node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_is_left_visited(self,value):
        self.is_left_visited= value

    def set_is_right_visited(self,value):
        self.is_right_visited = value

    def get_is_left_visited(self):
        return self.is_left_visited

    def get_is_right_visited(self):
        return self.is_right_visited
