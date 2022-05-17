from functools import reduce

fruits= [" apple", "orange", "pear", "banana"]
fruits2 = reduce(lambda x, y : y.capitalize() if x== '' else x +','+y.capitalize(), fruits,'')
print(fruits2)

#list2 = reduce(lambada concatName, x: concatName+','+x.capitalize(),list1,).lstrip(',')
#print(list2)

#fruits2=reduce(lambada x, y:x.replace(x[0],x[0].upper())+''+ y.replace(y[0]))



