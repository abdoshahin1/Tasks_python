#the dictionary use this method copy and update and clear
#first method is keys and values
dic={"name":"ahmed"}
print(dic.keys())
print(dic.values())
#method number two is setdefault
dic={"name":"ahmed"}
print(dic)
print(dic.setdefault("name","ali"))
print(dic.setdefault("age",20))
print(dic)
#method number three is popitem() show the last item i add to dictionary
dic1={"name":"ahmed","age":20}
dic1["country"]="egypt"
print(dic1.popitem())
#method number four is items()
dic2={"name":"ali","age":18}
print(dic2.items())
allitem=dic2.items()
print(allitem)
#method number five is fromkeys()
tuple1=("name","age")
b="ahmed"
print(dict.fromkeys(tuple1,b))
#method number six is get() use to get the value of certain key it takes a argument is key
