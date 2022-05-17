def printTriangle(height):
    #control the number of rows
    for i in range(height):
    #control the number of spaces
        for j in range (height -i-1):
             print(' ', end='')
     #print the number of stars
        for j in range(i+1):
            print('*', end='')
        print()

def main():
    height = int(input('Enter the height of the triangle: '))
    printTriangle(height)

main()
