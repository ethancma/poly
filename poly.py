from math import sqrt


def main():
    quad = userInput()
    while (len(quad) != 3):
        print("\nRemember to add a 0 if any of the terms are missing!\n")
        quad = userInput()
    print(quad)
    print(isQuad(quad))

# end

def userInput():
    print("Given a quadratic equation in the form of Ax^2+Bx+C")
    print("For example, for 2x^2+3x+4, enter 2 3 4")
    print("Enter your A, B, and C values separated by one space:")
    quadratic = input()

    termList = quadratic.split()
    for i in termList:
        if not i.isnumeric(): return []
        
    intTermList = list(map(int,termList))
    return intTermList

def isQuad(quadratic:list):
    # check discriminant
    val = True
    try:  val = (sqrt(quadratic[1]**2-4*quadratic[0]*quadratic[2])).is_integer() 
    except ValueError: val = False
    return val

if __name__=='__main__':
    main()
# end
