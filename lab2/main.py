import random
import sys

from Node import Node

THRESHOLD = 5


def gen_tree_rank(rank):
    depth = random.randint(2, THRESHOLD)
    print('Gen rank')
    print(f'Tree with depth={depth}, rank={rank}:')
    root = Node()
    root.gen_node_rank(depth, rank)
    root.print_node(0)
    # for _ in range(depth):


def gen_tree_depth(depth):
    print('Gen depth')
    print(f'Tree with depth={depth}, rank={THRESHOLD}:')
    root = Node()
    root.gen_node_depth(depth, THRESHOLD)
    root.print_node(0)
    # for _ in range(depth):


if __name__ == "__main__":
    if len(sys.argv) == 3:
        mod = sys.argv[1]
        size = int(sys.argv[2])
    else:
        print("Error, Usage:prog type size")
        sys.exit(1)

    if mod == '0':
        gen_tree_rank(size)
    elif mod == '1':
        gen_tree_depth(size)

