n = int(input())
arr = map(int, input().split())
l1 = [*arr]
print(max([i for i in l1 if i<max(l1)]))
