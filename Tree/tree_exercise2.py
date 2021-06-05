class TreeNode():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        p = self.parent
        level = 0
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self, level):
        if level < self.get_level():
            return
        prefix = (' ' * (self.get_level()) * 3) + '|___'
        print(prefix, self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(level)


def location_tree():
    india = TreeNode('india')
    gujrat = TreeNode('gujrat')
    gujrat.add_child(TreeNode('baroda'))
    gujrat.add_child(TreeNode('surat'))
    india.add_child(gujrat)
    karnataka = TreeNode('karnataka')
    karnataka.add_child(TreeNode('banglore'))
    karnataka.add_child(TreeNode('mysor'))
    india.add_child(karnataka)

    usa = TreeNode('usa')
    new_jercy = TreeNode('new jercy')
    new_jercy.add_child(TreeNode('princton'))
    new_jercy.add_child(TreeNode('trnton'))
    usa.add_child(new_jercy)

    california = TreeNode('california')
    california.add_child(TreeNode('sanfrancsiso'))
    california.add_child(TreeNode('motuntain view'))
    california.add_child(TreeNode('paulo alot'))
    usa.add_child(california)

    glob = TreeNode('global')
    glob.add_child(india)
    glob.add_child(usa)
    return glob

if __name__ == '__main__':
    root_node = location_tree()
    root_node.print_tree(3)