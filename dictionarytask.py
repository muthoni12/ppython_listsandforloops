'''
given a list of dictionaries containing data such as product name and excl
passed to a function as parameters, together with tax rate.
calculate the incl of each product.
then print thier values.

vat = excl * rate
incl = excl + vat

p = [
    {
    "name" = milk,
    "excl" = 50
    },
    {
    "name" = bread,
    "excl" = 40
    },
]

'''

def calculateIncl(products, rate):
    incl = []
    for product in products:
        vat = product["excl"] * rate
        incl = product["excl"] + vat

        print(product["name"] +" "+ str(incl))

p = [
    {
    "name" : "milk",
    "excl" : 50
    },
    {
    "name" : "bread",
    "excl" : 40
    }
]

calculateIncl(p, 0.16)