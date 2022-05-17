#Que4:

def convertToF(c):
    return round(9/5)* c + 32, 1)

k= convertToF(36)

k = (lambda  c : round(9/5)* c+32, 1)(36)



degreeInCelsius= {12, 21, 15, 32}

degreeInFah =[ round((9/5)*c + 32, 1)    for c in degreeInCelsius]

print(degreeInFah)