import os
s = []
with open("file/1056785657_.txt", "r") as file:
    for line in file:
        s.append(line.split())
for k in s:
    print(k)
