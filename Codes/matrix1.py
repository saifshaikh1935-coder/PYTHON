rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of colums:"))

print("Enter elements of matrix A:")
A=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("Enter value: ")))
    A.append(row)

for i in A:
    for j in i:
        print(j,end=" ")
    print("")