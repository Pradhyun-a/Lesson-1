import array

box1 = {"apple", "chips", "apple", "cookie"}
box2 = {"cookie", "banana", "popcorn"}

box1.add("banana")
common = box1.intersection(box2)

counts = array.array("i", [5, 12, 8])

counts.insert(0, 3)
counts.append(15)

print("Times 12 appears:", counts.count(12))
counts.reverse()

print("Box 1:", box1)
print("Box 2:", box2)
print("Shared snacks:", common)
print("Final snack counts:", counts.tolist())
