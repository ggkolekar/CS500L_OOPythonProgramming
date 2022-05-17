#!/usr/bin/env python3
# getaverages.py

def getAverageWhile(list):
	sum = 0
	i = 0
	while i < len(list):
		sum += list[i]
		i += 1
	return sum
	
def getAverageFor(list):
	sum = 0
	i = 0
	for item in list:
		sum += item
	return sum
	
def main():
	scores = [10, 7, 8, 9, 6]
	print("getAverageWhile(scores) = ", getAverageWhile(scores))
	print("getAverageFor(scores) = ", getAverageFor(scores))
	
	
if __name__ == "__main__":
	main()