degreeInCelsius= {12, 21, 15, 32}

degreeInFah =[ round((9/5)*c + 32, 1) for c in degreeInCelsius]

print(degreeInFah)