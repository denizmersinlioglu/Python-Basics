coordinates = (3, 5)
print(coordinates[0])


def say_hi(name):
    return name * name * name


print(say_hi(4))

is_male = True
is_tall = False

if is_male and is_tall:
    print("male")
elif is_male and not(is_tall):
    print("hey")
else:
    print("female")


months = {
    "jan": "january",
    "feb": "february"
}
# Commets
'''
asdasdasd
'''
print(months["jan"])
print(months.get("fasd", "default"))

word = "deniz"

for letter in range(10):
    print(letter)

print(2**3)

try:
    value = 10/0
except ZeroDivisionError as err:
    print("Division Error")
    print(err)

file = open("employees.txt", "r")

for line in file.readlines():
    print(line)
file.close()
