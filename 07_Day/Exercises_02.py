#LEVEL 2

# Let's create two sets A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1. Join A and B (Union)
c = B.union(A)
print(c)
#2.
print(A.intersection(B))
#3.
print(A.issubset(B))
#4.
print(A.isdisjoint(B))
#5.
print(B.union(A))
print(A.union(B))
#6.
print(A.symmetric_difference(B))
#7.
del A
del B