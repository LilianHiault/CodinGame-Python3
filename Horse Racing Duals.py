n = int(input())
li = []
for i in range(n):
    pi = int(input())
    li.append(pi)

li.sort()
diff = li[1] - li[0]
for i in range(1, n):
    if li[i] - li[i-1] < diff:
        diff = li[i] - li[i-1]
print(diff)
