#!/usr/bin/env python3

import sys


def simple_lookup(item: str, items: dict) -> bool:
    for it in items:
        if it == item:
            return True
    return False


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
i = 0
for item in items.keys():
    print(f"{item}: {items[item]} units "
          f"({(items[item] / total_items) * 100: .1f}%)")
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
items['moderate']: dict = dict()
items['scare']: dict = dict()
for item in items.keys():
    if items[item] >= 5:
        moderate[item] = items[item]
    else:
        scare[item] = items[item]
print(f"Moderate: {moderate}")
print(f"Scarce: {scare}")
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
print(f"Sample lookup - ’sword’ in inventory: {simple_lookup('sword', items)}")
