N = int(input())
Ti = list(map(int, input().split()))
P = int(input())
M = int(input())

pequenas = Ti.count(1)
medias = Ti.count(2)

if pequenas <= P and medias <= M:
    print("S")

else:
    print("N")