

#number = int(input("Enter any integer number up tp and including 100: "))
#numList= numList.append(num)


#multiples=[      x  for x in range(1, 101) if x % number == 0 ]
#print(multiples)

#multiples1 =[      x  for x in range(number, 101, number) if x % number == 0 ]
#print(multiples1)


#que3:make list nums divisible by 5
nums =[2,4,5,10,12,15,30]
nums2 =(lambda numList : [x for x in numList if x % 5 == 0])(nums)
print(nums2)