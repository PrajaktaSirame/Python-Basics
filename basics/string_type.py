s='       you are fool   '
print(s)

s1=""" you are the 
creator of your destiny"""
print (s1)

#indexing
print(s[0])

#repetition
print(s*2)

# length
print(len(s1))

#slicing 
print(s[0:5])
print(s[:8])
print(s[-3:-1])

#steps in slicing
print(s[0:9:2])
print(s[15::-1])

#strip function
print(s.strip())
print(s.rstrip())   

#location in string 
print(s.find("ool"))
print(s.find("ool",0,len(s))) 
print(s1.count("a"))
print(s.replace("fool","super"))
print(s.upper())
print(s.title())
  