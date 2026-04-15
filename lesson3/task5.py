from typing import Any

fruit = ["apple", "banana", "cherry"]
fruit.append("orange")
fruit[1] = "blueberry"
print(fruit)

def replace_el(lst: list, old_val: Any, new_val: Any):
    idx = lst.index(old_val)
    lst[idx] = new_val
    
replace_el(fruit, 'any', 'fruit')
    