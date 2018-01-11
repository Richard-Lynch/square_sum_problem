#!/usr/local/bin/python3
from collections import defaultdict
from pprint import pprint
highest_val = 20
values = [i for i in range(1, highest_val + 1)]
squares = [v * v for v in values]

print('values:')
for v in values:
    print(v)

possible_pairs = defaultdict(lambda: defaultdict(int))
sums = defaultdict(lambda: defaultdict(list))
new_pairs = defaultdict(lambda: defaultdict(list))

v_list = defaultdict(int)
counts_ = {}

for i, v_out in enumerate(values):
    print('v_out', v_out)
    for k, v in sums[v_out].items():
        sums[v_out + 1][k] = v[:]
    for v1 in values[:v_out + 1]:
        for v2 in values[:v_out + 1]:
            sum_v = v1 + v2
            if sum_v in squares and v1 != v2:
                if (v1, v2) not in possible_pairs and (
                        v2, v1) not in possible_pairs:
                    possible_pairs[(v1, v2)] = True
                    sums[v_out + 1][sum_v].append((v1, v2))
                    # new_pairs[v_out + 1][sum_v].append()

# for i, v_out in enumerate(values):
#     for v1 in values[:i + 1]:
#         for v2 in values[:i + 1]:
#             if v1 != v2:
#                 sum_v = v1 + v2
#                 if sum_v in squares:
#                     print('adding to', v1)
#                     v_list[sum_v] += 1
#         possible_pairs[v1] = {k: v for k, v in v_list.items()}
#         # counts_[v1] = sum([v for k, v in v_list.items()])
#     count = 0
#     for k in v_list:
#         count += v_list[k]
#         v_list[k] = 0
# counts_[v_out] = count

for i, k in enumerate(sums):
    print(k)
    v_sq = sums[k].keys()
    v_pairs = sums[k].values()
    print(*[(v_sq_i, v_pairs_i) for v_sq_i, v_pairs_i in zip(v_sq, v_pairs)])
    # print(sums[k])
    # print()
    # print([ki, vi for ki, vi sums[k]])
    # print(*[(k1, v1) for k1, v1 in v.items()])
    # print(*[sums[k]])
    print()
    # pprint(v)
# for k, v in possible_pairs.items():
#     print(k)
#     # print(*[(k1, v1) for k1, v1 in v.items()])
#     print(v)
#     print()
#     # pprint(v)
