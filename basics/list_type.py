from audioop import reverse
lst=[10,20,55,'prajakta',13.5]
print(lst)

#index
print(lst[3]) 

#slicing
print(lst[3:5])

#repetition
print(lst*2)

#length
print(len(lst))

#add and removed element from list
lst.append(50)
lst.remove('prajakta')
del(lst[1])
print(lst)

print(max(lst))
print(min(lst))

lst.insert(3,50)
print(lst)

lst.sort(reverse=True)
print(lst)

lst.clear()
print(lst)

lst=["India","UAS","UK"]

lst.append("Rus")
print(lst)

del(lst[2])
print(lst)

lst.insert(2,"China")
print(lst)