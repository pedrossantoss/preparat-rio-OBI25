x = int(input())
y = int(input())
z = int(input())

if x <= y and x >= z:
    print(x)

elif x >= y and x <= z:
    print(x)    

elif y >= x and y <= z:
    print(y)     

elif y <= x and y >= z:
    print(y)   

elif z >= y and z <= x:
    print(z)   

elif z <= y and z >= x:
    print(z)       