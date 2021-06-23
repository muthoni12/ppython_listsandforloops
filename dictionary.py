#student = {
#    "name" : "pal",
#    "age" : 19,
#    "gender" : "F"
#}
#
#student["name"] = "val"
#print(student["name"])

'''
combined list with dictionary to have all that same data but for more than one item.
'''

users = [
    {
    "name" : "hal",
    "age" : 19,
    "gender" : "F"
    },
    {
    "name" : "mal",
    "age" : 9,
    "gender" : "M"
    },
    {
    "name" : "sal",
    "age" : 10,
    "gender" : "F"
    }
]

for user in users:
    print(user["name"])

for user in users:
    if user["name"] == "sal":
        print(user["name"])
        print(user["age"])
        print(user["gender"])

