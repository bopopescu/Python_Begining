
# dictionary is the special structure of python
# which is used to store the data as a key value pair

dictionary_user = {
    "name": "Sanat Mondal",
    "email": "cse.sanat@gmail.com",
    "password": "12345",
    "mobile": "01712995265"
}

print(dictionary_user)
print(dictionary_user["name"])

dictionary_user["name"] = "Android"
print(dictionary_user["name"])
print(dictionary_user.get("name"))

# default value for a key
print(dictionary_user.get("address", "Not a valid key"))

print("=============All dictionary title with values print============== ")
for x in dictionary_user:
    print(x + "=" + dictionary_user[x])

print("==========All dictionary values print ========")
for x in dictionary_user.values():
    print(x)

print("==========All dictionary items print ========")
for x in dictionary_user.items():
    print(x)

print("========== dictionary with title and value in seperate variable print ========")
for x, y in dictionary_user.items():
    print(x, y)

print("==========Delete data from  Dictionary============")
del dictionary_user["name"]
print(dictionary_user)

