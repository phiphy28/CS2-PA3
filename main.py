# def print_tree(root):
#     stack = [(0, root)]  # (tabs, node)
#
#     while stack:
#
#         tup = stack.pop()
#
#         print("\t" * tup[0], end="")
#         print(f"->{tup[1].get_vertex_info()}")
#
#         for ele in tup[1].get_children():
#             stack.append((tup[0] + 1, ele))

class Parser:
    def __init__(self):
        self.cases = self.number_of_cases()
        self.num_vertices = self.number_of_vertices()

    # def read_from_console(self):
    #     t = Tree()
    #
    #     for i in range(self.number_of_cases()):
    #
    #         t.setup_tree(self.num_vertices)
    #         combo = []
    #         for j in range(self.num_vertices - 1):
    #             parent, child = input("enter parent child ex: 1 2\n").split(" ")
    #             t.add(int(parent), int(child))
    #             combo.append((int(parent), int(child)))
    #         print(combo)
    # v = Vertex(t)
    # print(v.calculate_point_value(t))
    # print(t)

    def number_of_vertices(self):
        self.num_vertices = int(input("the number of vertices in the tree/test case\n"))
        return self.num_vertices

    def number_of_cases(self):
        self.cases = int(input("the total number of trees/test cases\n"))
        return self.cases


class Tree:
    def __init__(self, cases, num_vert):
        self.cases = cases
        self.num_vert = num_vert

    def search(self, u):
        return

    # def setup_tree(self):
    #     for i in range(self.cases):
    #         v = Vertex()
    #         v.setup()
    #         for j in range(self.num_vert - 1):
    #             parent, child = input("enter parent child ex: 1 2\n").split(" ")
    #             v.parent = int(parent)
    #             v.add_child(int(child))
    #
    #         print(v)

    # def add(self, u, v):
    #     self.full_tree[u].append(v)
    #
    # def __str__(self):
    #     return "Tree: {}".format(self.full_tree)


class Vertex:
    def __init__(self):
        self.vert = {}
        self.weights = {}

    # def __getitem__(self, item):
    #     return self.vert[item]

    def setup(self, n):
        for i in range(1, n + 1):
            self.vert[i] = []
            self.weights[i] = 0

    def __str__(self):
        return f"Vertex: {self.vert}"

    def add_child(self, parent, value):
        self.vert[parent].append(value)

        
    # def calculate_point_value(self, i, tot=0):
    #     if len(self.tree[i]) == 0:
    #         tot += 1
    #     else:
    #         for i in self.tree[i]:
    #             return self.calculate_point_value(i, tot)
    #     return tot
    def calc_weight(self, index):
        if len(self.vert[index]) == 0:
            return 1
        else:
            for i in index:
                return self.calc_weight(i)

        # for i, v in self.vert:
        #     if len(v) == 0:
        #         self.weights[i] = 1
        #     for value in v:
        #         if len(self.vert[value]) == 0:
        #             self.weights[i] += 1
        #         else:
        #             self.weights[i] += self.weights[value]
        # for i, v in self.vert:
        #     if len(v) == 0:
        #         return 1
        #     else:
        #         for j in v:
        #             caself.weights[i]
        #         return

    def calculate_num_vertices(self, parent):
        return len(self.vert[parent]) + 1


# Python3 code to find the maximum path sum
dp = [0] * 100


# Function for dfs traversal and
# to store the maximum value in
# dp[] for every node till the leaves
def dfs(a, v, u, parent):
    # Initially dp[u] is always a[u]
    dp[u] = a[u - 1]

    # Stores the maximum value from nodes
    maximum = 0

    # Traverse the tree
    for child in v[u]:

        # If child is parent, then we continue
        # without recursing further
        if child == parent:
            continue

        # Call dfs for further traversal
        dfs(a, v, child, u)

        # Store the maximum of previous visited
        # node and present visited node
        maximum = max(maximum, dp[child])
    # Add the maximum value
    # returned to the parent node
    dp[u] += maximum


# Function that returns the maximum value
def maximumValue(a, v):
    dfs(a, v, 1, 0)
    return dp[1]


# Driver Code
def main():
    p = Parser()

    # Number of nodes
    n = p.num_vertices
    # t = Tree(p.cases, p.num_vertices)
    v = Vertex()
    v.setup(n)

    for i in range(p.cases):
        v.setup(p.num_vertices)
        for j in range(p.num_vertices - 1):
            parent, child = input("enter parent child ex: 1 2\n").split(" ")
            v.add_child(int(parent), int(child))

    print(v)
    weights = {}
    for i in range(1, n + 1):
        weights[i] = 0
    for i, j in v:
        weights[i] += v.calc_weight(j)
    # Adjacency list as a dictionary
    # v = {}
    # for i in range(n + 1):
    #     v[i] = []
    # Create undirected edges
    # initialize the tree given in the diagram
    # v[1].append(2), v[2].append(1)
    # v[1].append(3), v[3].append(1)
    # v[1].append(4), v[4].append(1)
    # v[2].append(5), v[5].append(2)
    # v[2].append(6), v[6].append(2)
    # v[3].append(7), v[7].append(3)
    # v[4].append(8), v[8].append(4)
    # v[4].append(9), v[9].append(4)
    # v[4].append(10), v[10].append(4)
    # v[5].append(11), v[11].append(5)
    # v[5].append(12), v[12].append(5)
    # v[7].append(13), v[13].append(7)
    # v[7].append(14), v[14].append(7)

    # Values of node 1, 2, 3....14
    a = [3, 2, 1, 10, 1, 3, 9,
         1, 5, 3, 4, 5, 9, 8]

    # Function call
    print(maximumValue(a, v))


main()
