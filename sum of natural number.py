'''

# find the sum of sqare of given range of number
n=int(input('enter the number up to which you want to sum'))
i=1
sum=0
while (i<=n):
    sum = sum + (i*i)
    i= i+1

print(sum)

#n=int(input('enter the no to range'))
j = range(1,51)
print(sum(j))

n= int(input('enter the number'))
sum=0
for i in range(1,n+1):
    sum = sum + i
print(sum)

def str1(n):
    return sum(range(n+1))
print(str1(50))
'''
