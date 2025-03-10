P = int(input())
D1 = int(input())
D2 = int(input())

if P == 0 and (D1 + D2)%2 == 0:
    print(0)

elif P == 0 and (D1 + D2)%2 != 0:
    print(1)   

if P == 1 and (D1 + D2)%2 == 0:
    print(1)

elif P == 1 and (D1 + D2)%2 != 0:
    print(0) 
