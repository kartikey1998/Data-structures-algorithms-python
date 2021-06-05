class TreeNode:
    def __init__(self, name, desig):
        self.name = name
        self.desig = desig
        self.children = []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level

    def print_tree(self, property):
        if property == 'both':
            val = self.name + ' (' + self.desig + ')'
        elif property == 'name':
            val = self.name
        else:
            val = self.desig

        prefix = (' ' * (self.get_level()) * 3) + '|___'
        print(prefix + val)
        if self.children:
            for child in self.children:
                child.print_tree(property)


def build_management_tree():
    ceo = TreeNode('nilupl', 'ceo')
    cto = TreeNode('chinmay', 'cto')
    infra = TreeNode('vishwas', 'infra HEad')
    infra.add_child(TreeNode('dhaval', 'cloud Manager'))
    infra.add_child(TreeNode('abhijet', 'app manager'))

    hr_head = TreeNode('gels', 'hrHead')
    hr_head.add_child(TreeNode('peter', 'recurit manaeger'))
    hr_head.add_child(TreeNode('waqas', 'policy manager'))

    ceo.add_child(cto)
    ceo.add_child(hr_head)
    return ceo


if __name__ == '__main__':
    root = build_management_tree()
    root.print_tree("name")  # prints only name hierarchy
    root.print_tree("designation")  # prints only designation hierarchy
    root.print_tree("both")  # prints both (name and designation) hierarchy
