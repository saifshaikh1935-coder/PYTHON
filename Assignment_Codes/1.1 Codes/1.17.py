n = int(input("Enter number: "))

cnt = 0

for i in range(2,n):
    if n%i == 0:
        cnt = cnt+1
        break

if cnt == 0 and n > 1:
    print(n, "prime no")
else:
    print(n, "not prime no")

print("Prime numbers from 2 to", n)

for num in range(2,n+1):
    for i in range(2,num):
        if num%i == 0:
            break
    else:
        print(num,end=" ")