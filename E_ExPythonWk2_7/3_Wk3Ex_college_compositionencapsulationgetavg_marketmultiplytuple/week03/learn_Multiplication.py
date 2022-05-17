def main():
    print("The Market Test Program")
    print()
def multiply(x,y):
    sx= input"Enter number x "
    sx= str(x)
    sx= input"Enter number y "
    sy= str(y)
    if x < 10 and y < 10:
        return x*y
    import random
    a= [str(random.randrange(0,10,1))]
    a = int(''.join(a))
    m = max(len(sx), len(sy))
    sx ='0'*(m-len(sx))+sx
    sy = '0'*(m -len(sy))+sy
    value=0
    for n in range(len(sx)):
        for m in range(len(sy)):
            prod=eval(sx[n]+"*"+ sy[m])
            return prod

        if 





    if __name__ == "__main__":
        main()