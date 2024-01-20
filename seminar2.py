#Задача 1
#n = 123

s = n%10
n=n//10
s1 =n%10
n=n//10 
s2 = n%10

res = s+s1+s2

#Задача 2

#n = 6

s =  n//6

s2 = n//6

s1 = (s + s2)*2



print (s, s1, s2)

#Задача 3

#n = 385916

s = n%10
n = n//10

s1 = n%10
n = n//10

s2 = n%10
n = n//10

s3 = n%10
n = n//10

s4 = n%10
n = n//10

s5 = n%10
n = n//10

a = s+s1+s2
b = s3+s4+s5

if a==b:
    print("yes")
else:
    print("no")
    
#Задача 4

#a = 3
#b = 2
#c = 4

if a*b>c:
    print("yes")
else:
    print("no")