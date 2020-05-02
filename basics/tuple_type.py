#if you want to show single number then always put a ',' after a single int so it wouldn't consider a int type `
tpl=(40,50,40,'xyz')
print(tpl)


#index
print(tpl[3])

print(tpl.count(40))

print(tpl.index('xyz'))

#conversion of list to tpl
lst=[10,20,50]
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))
