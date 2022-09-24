# ---
str = "Hello world"
print(type(str))
print(id(str))
str +=  " from twuaiq!"
print(id(str))

print("observations: \n The string has changed the the value and it is because of the memory ")

# ---
list = [1,2,3]
print(type(list))
print(id(list))
list[0] = 5
print(id(list))

print("observations: \n It will change the index number 0 to 5")


# ---
my_dict ={"Name":"Ahmed","Age":43}
print(type(my_dict))
print(id(my_dict))
print(my_dict["Age"])
my_dict["Age"] = 19
print(my_dict["Age"])
print(id(my_dict))

print("observations: \n The age will be 19)

# --- 
tuple = 1,2,3
print(type(tuple))
print(id(tuple))

print("observations: \n It will printed the type of ID")

# # Uncomment the below code and run it, can u explain what happened?
# tuple[0] = 2
#print("observations: \n tuple immutable")