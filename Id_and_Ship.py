# https://www.codechef.com/LP0TO101/problems/FLOW010

import sys, collections
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    _id = input().rstrip().lower()

    get_class_default_dict = collections.defaultdict(
        lambda: "I am the default value",
        [
            ("b", "BattleShip"),
            ("c", "Cruiser"),
            ("d", "Destroyer"),
            ("f", "Frigate")
        ]
    )

    print(get_class_default_dict[_id])
