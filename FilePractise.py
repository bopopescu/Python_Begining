# File Read example

f = open("example.txt", "r")

# Read the example.txt file
# print(f.read())

# print("=======Write first 5 latter====")
# print(f.read(5))

print("=======Write only first line====")
print(f.readline()) #print
print(f.readline())

print("Hi this is sanat. Testing the git pass change")

# File Write example
f = open("example_write.txt", "w")
f.write("Hello World. \nThis is my first write file program.")

