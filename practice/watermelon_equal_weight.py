w=int(input("Enter a watermelan weight : "))
if(w%2!=0 or w==2):
    print("no")
else:
    x=w//2
    if(x%2==0):
        print(x,x)
    else:
        print(x-1,x+1)