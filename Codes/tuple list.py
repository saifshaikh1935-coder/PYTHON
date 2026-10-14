A=[10,20,30,40,50,60,70,80,90]
print("Original :",A)

A.append(50)
print("append :",A)

A.insert(1,00)
print("insert :",A)

A.remove(50)
print("remove:",A)

print("----------------TUPLE----------------")
print("reverse without reverse():",A[::-1])
print("tup A[0:4] :",A[0:4])
print("tup A[1:4:1] :",A[1:4:1])
print("tup A[5:8] :",A[5:8])
print("tup A[5:7] :",A[5:7])

print("----------------MAXIMUM & MINIMUM NUMBER----------------")
print("Max Number :",max(A))
print("Min Number :",min(A))
print("Sum Number :",sum(A))
print("Index 5:",A[5])