n=int(input("Enter a num:"))
count=0
arm=0
temp1=n
temp2=n
while(temp1):
    temp1=temp1//10
    count+=1
while(n):
    digit=n%10
    arm=arm+digit**count
    n=n//10
if(temp2==arm):
    print("Armstrong num")
else:
    print("Not a Armstrong")
