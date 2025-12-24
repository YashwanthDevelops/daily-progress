set1 = {"History", "Math", "Physics", "Science","Math"}
print(set1)

print("Math" in set1)

set2 = {"History", "Math", "Art", "Design"}
print(set1.intersection(set2))

print(set1.difference(set2))

print(set1.union(set2))

# empty_set = {} -> error (its a dictionary)
empty_set = set()