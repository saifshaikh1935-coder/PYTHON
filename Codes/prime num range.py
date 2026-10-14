n=int(input("Enter no"))
cnt=0
for i in range(1,n+1):
    if(n%1==0):
        cnt+=1
    if(cnt>2):
        break;    
print(cnt)   
if(cnt==2):
    print(n,"prime no")
else:   
    print(n,"not prime no")