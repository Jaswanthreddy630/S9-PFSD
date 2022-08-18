x=int(input())
temp=x
sum=0
while x!=0:
    sum=sum*10+x%10
    x=x//10
if sum==temp:
    print("Palindrome:")
else:
    print("Not Palindrome :")