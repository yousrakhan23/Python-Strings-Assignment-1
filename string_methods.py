# .................... string methods ........................

name1: str = "yousra khan"   # original state

# capitalize() method: Converts the first character of a string to uppercase
print(name1.capitalize()) # output: Yousra khan

# lower() method: Converts all characters of a string to lowercase
print(name1.lower()) # output: yousra khan

# title() method: Converts the first character of each word to uppercase
print(name1.title()) # output: Yousra Khan

# swapcase() method: Swaps the case of all letters in a string(all lettersare in upper case)
print(name1.swapcase()) # output: YOUSRA KHAN

# count() method: Returns the number of occurrences of a substring in a string
print(name1.count("a")) # output: 2

# find() method: Returns the index of the first occurrence of a substring in a string(give us index number)
print(name1.find("a")) # output: 5

# rfind() method: Returns the index of the last occurrence of a substring in a string
print(name1.rfind("a")) # output: 9

# replace() method: Replaces a substring in a string with another substring
print(name1.replace("yousra", "hassan")) # output: hassan khan

# split() method: Splits a string into a list of substrings
print(name1.split()) # output: ['yousra', 'khan']

# join() method: Concatenates all elements of a list into a string 
fruits = ["mango", "banana", "cherry"]
print(", ".join(fruits))  # output: mango, banana, cherry

# lenth method:
print(len(name1)) # output: 11 (it is also count spaces)

# slice method:
print(name1[0:4]) # output: yous

# isalpha method:
phone = "iphone"
print(phone.isalpha()) # output: True

# f-string method:
my_self = "yousra khan"
my_edu = "bechalors"
my_goal = "AI agent"

summary = f"my name is {my_self}, my age is { 20+2 }, my education is {my_edu}, my goal is {my_goal}"
print (summary)

# f-string concatenation:
first_name = "learning"
last_name = "python"
print (f"{first_name} {last_name}")

words = "I am {name}"
# # .format() method:
# words = "my name is { } , my fav food is { } ".format("rapunzel","biryani")
# print(words)


# # input method:
# name = input("enter your name")
# print(name)