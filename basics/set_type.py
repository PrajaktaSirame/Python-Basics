s={10,20,30,'xyz',10,20}
print(s)
print(type(s))

#update
s.update([88.99])
print(s)

#we can't perform slicing ,index,repetition on set

#remove
s.remove(20)
print(s)


#frozen set then we can't perform update and remove operation on set

f=frozenset(s)
f.update([20])# get error