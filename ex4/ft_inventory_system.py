#!/usr/bin/env python3

import sys


def simple_lookup(item: str, items: dict) -> bool:
    for it in items:
        if it == item:
            return True
    return False


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    argc: int = len(sys.argv)
    i: int = 1
    items: dict = dict()

    while i < argc:
        res: str = ""
        j: int = 0
        num: str = ""
        while j < len(sys.argv[i]):
            if sys.argv[i][j] == ":":
                j += 1
                if j == len(sys.argv[i]) - 1:
                    items[res] = int(sys.argv[i][j])
                else:
                    while j < len(sys.argv[i]):
                        num += sys.argv[i][j]
                        j += 1
                        items[res] = int(num)
            else:
                res += sys.argv[i][j]
            j += 1
        i += 1

    total_items: int = 0

    for val in items.values():
        total_items += val

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(items)}")
    print()

    print("=== Current Inventory ===")
    sorted_item = dict()
    while len(sorted_item) < len(items):
        max_item = ""
        max_value = -1

        for item in items.keys():
            if item not in sorted_item and items[item] > max_value:
                max_value = items[item]
                max_item = item
        print(f"{max_item}: {items[max_item]} units "
              f"({(items[max_item] / total_items) * 100: .1f}%)")
        sorted_item[max_item] = True
    print()

    print("=== Inventory Statistics ===")
    most: int = 0
    it: str = ""
    for item in items.keys():
        if items[item] > most:
            most = items[item]
            it = item
    print(f"Most abundant: {it} ({most} units)")
    for item in items.keys():
        if items[item] < most:
            most = items[item]
            it = item
    print(f"Least abundant: {it} ({most} units)")
    print()

    print("=== Item Categories ===")
    categories: dict = {
            "Moderate": dict(),
            "Scarce": dict()
            }
    for item in items.keys():
        if items[item] >= 5:
            categories["Moderate"][item] = items[item]
        else:
            categories["Scarce"][item] = items[item]
    print(f"Moderate: {categories["Moderate"]}")
    print(f"Scarce: {categories["Scarce"]}")
    print()

    print("=== Management Suggestions ===")
    restock: list = []
    for item in items.keys():
        if items[item] <= 1:
            restock.append(item)
    print(f"• Restock needed: {restock}")
    print()

    print("=== Dictionary Properties Demo ===")
    list_of_items = []
    list_of_val = []
    for item in items.keys():
        list_of_items.append(item)
        list_of_val.append(items[item])
    print(f"Dictionary keys: {list_of_items}")
    print(f"Dictionary values: {list_of_val}")
    print(f"Sample lookup - ’sword’ in inventory: "
          f"{simple_lookup('sword', items)}")
