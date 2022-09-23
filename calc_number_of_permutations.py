import numpy as np
import itertools
import argparse


def calc_num_of_permutations(l, d):
    n_dist = d
    total_l = l

    for dis in np.arange(1, n_dist + 1):
        list_l = list(np.arange(1, total_l + 1))
        tot_com = 0

        for l in np.arange(1, total_l + 1):
            perm = itertools.combinations(list_l, l)
            for p in perm:
                tot_com = tot_com + 1

    print("Total number of permutations: ", tot_com * n_dist)

    return tot_com


parser = argparse.ArgumentParser(
    description="Script to  calculate number of possible permutations LIPMIX input file. "
    "Example: python calc_num_of_permutations.py -l 1 -d 1"
)
parser.add_argument(
    "-l", default=1, required=True, type=int, help="Total expected number of layers."
)
parser.add_argument(
    "-d",
    default=1,
    required=True,
    type=int,
    help="Total expected number of distributions.",
)

args = parser.parse_args()

# Main function
calc_num_of_permutations(args.l, args.d)
