'''
given a list of three exclusive prices and the tax rate,
write a function that takes the excls and rate as parameters.
then calculate the VAT amount and inclusive price for each excl.
return a list of incls and VATs

'''

def calculateVAT(excl, rate):
    incl = []
    VAT = []

    breadVAT = excl[0] * rate
    VAT.append(breadVAT)
    breadincl = excl[0] + breadVAT
    incl.append(breadincl)

    riceVAT = excl[1] * rate
    VAT.append(riceVAT)
    riceincl = excl[1] + riceVAT
    incl.append(riceincl)

    milkVAT = excl[2] * rate
    VAT.append(milkVAT)
    milkincl = excl[2] + milkVAT
    incl.append(milkincl)

    return [incl, VAT]

print(calculateVAT([23, 24, 25], 0.16))

"""
so, the above way is right, however, to shorten the part for calculating the inclusive price for each item, write:
    breadVAT = excl[0] * rate
    VAT.append(breadVAT)
    incl.append(breadVAT + excl[0]) --> this avoids having to write the inclusive price formula
                                        then on the next line adding it.
                                        so, you'd just be writting the formula
                                        within the adding of the inclusive price.

and, to shorten even further,
    VAT.append(excl[1] * rate)
    incl.append((excl[1] * rate) + excl[1]) --> this puts the formulas\
                                                into the adding of the VAT and incls
                                                immediately.


"""

def calculateVAT(excl, rate):
    incl = []
    VAT = []

    breadVAT = excl[0] * rate
    VAT.append(breadVAT)
    incl.append(breadVAT + excl[0])

    VAT.append(excl[1] * rate)
    incl.append((excl[1] * rate) + excl[1])

    VAT.append(excl[2] * rate)
    incl.append((excl[2] * rate) + excl[2])

    return [incl, VAT]

print(calculateVAT([23, 24, 25], 0.16))

'''
given a list of three exclusive prices and the tax rate,
write a function that takes the excls and rate as parameters.
then calculate the VAT amount and inclusive price for each excl.
return a list of incls and VATs

Use FOR LOOPS

'''

def calculateVAT(excl, rate):
    incl = []
    VAT = []
    for price in excl:
        vat = price * rate
        VAT.append(price * rate)
        incl.append(price + vat)

    return [incl, VAT]

print(calculateVAT([100, 200, 50], 0.16))

'''
write a function that takes a list of yob and the cy as parameters,
then calculate and return a list containing the ages of each yob provided in the parameter.
'''

def calculateage(cy, yob):
    age = []
    for year in yob:
        AGE = cy - year
        age.append(AGE)

    return [age]

print(calculateage(2021, [2002, 1994, 1974]))

'''
Loops + Lists + Prompts

def calculateage(cy, yob):
    age = []
    for year in yob:
        AGE = cy - year
        age.append(AGE)

    return [age]

def userInputs():
    cy = int(input("Enter the cy"))
    yob = int(input("Enter your yob"))
    age = calculateage(cy, yob)

    print(age)

userInputs()
'''
