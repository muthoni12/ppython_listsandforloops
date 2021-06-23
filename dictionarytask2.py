'''
given a list of dictionaries containing data such as product name and excl
passed to a function as parameters, together with tax rate.
calculate the incl of each product.
then return a list of dictionaries containing the incl and name.
'''

def calculateIncl(products, rate):
    incl = {}
    for product in products:
        vat = product["excl"] * rate
        incl = product["excl"] + vat

        return {product["name"], incl}

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

print(calculateIncl(p, 0.16))