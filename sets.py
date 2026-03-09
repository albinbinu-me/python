"""
set - unordered and unindexed,no duplications
"""

utils = {
    "fork","spoon","knife","knife"
}
dishes = {
    "bowl","plate","cup","knife"
}
# for i in utils:
#     print(i)

# utils.add("napkin")
# utils.remove("fork")
# utils.clear()

# utils.update(dishes)
dinner_table = utils.union(dishes)
print(dinner_table)

