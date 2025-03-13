#LEVEL 2

# Let's create two sets A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B (Union)
c = B.union(A)
print(c)
#2.Find A intersection B
print(A.intersection(B))
#3.Is A subset of B
print(A.issubset(B))
#4.Are A and B disjoint sets
print(A.isdisjoint(B))
#5.Join A with B and B with A
print(B.union(A))
print(A.union(B))
#6.What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#7.Delete the sets completely
del A
del B