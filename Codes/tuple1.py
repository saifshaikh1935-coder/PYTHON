A=[10,20,30,40]
print(A)

A.append(50)
print("append :",A)

A.insert(1,100)
print("insert :",A)

A.remove(50)
print("remove:",A)

print("----------------TUPLE----------------")
print("reverse without reverse():",A[::-1])
print(A[0:4])
print(A[1:4:1])