lst=[20,30,40,234]
print(type(lst))
b=bytes(lst)
print(type(b))

#we can't perform indexing and modify bytes 

b1=bytearray(lst)
print(type(b1))
b1[2]=33

