import random


class Node:
    def __init__(self):
        self.child_list = None

    def gen_node_rank(self, depth, rank):
        if depth - 1 == 0:
            return
        if random.randint(0, 1) == 0:
            return
        self.child_list = []
        for _ in range(rank):
            new_node = Node()
            new_node.gen_node_rank(depth - 1, rank)
            # if new_node is not None:
            self.child_list.append(new_node)

    def gen_node_depth(self, depth, rank_threshold):
        if depth - 1 == 0:
            return

        self.child_list = []
        rank = random.randint(2, rank_threshold)
        for _ in range(rank):
            new_node = Node()
            new_node.gen_node_depth(depth - 1, rank)
            # if new_node is not None:
            self.child_list.append(new_node)

    def print_tabs(self, depth):
        if depth >= 2:
            for i in range(depth):
                print("|   ", end="")
        if depth >= 1:
            print("|---", end="")

    def print_node(self, depth):
        self.print_tabs(depth)

        if self.child_list is not None:
            print(f"[Node]({len(self.child_list)})")
            for child in self.child_list:
                child.print_node(depth + 1)
        else:
            print(f"[Node](0)")
