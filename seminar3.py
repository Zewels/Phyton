#Задача 1
# coins = [0, 1, 0, 1, 1, 0]

i = 0
n = len(coins)
p = 0
z = 0

while i<n:
    if coins[i] == 0:
        z+=1
    else:
        p+=1
    i+=1

if z>p:
    print (p)
else:
    print (z)

#Задача 2

# s = 12
# p = 27

x = 0
y = s
n = 0
   
while x<=y:
    if (s==x+y and p==x*y):
        print (x, y)
        break
    else:
        x+=1
        y-=1

#Задача 3

# n=15

x = 0
res = 1
while res < n+1:
    print(res)
    x += 1
    res = 2 ** x