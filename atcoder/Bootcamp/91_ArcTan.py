"""
2 2 4
"""
import math

def main():
    a,b,x = map(int,input().split())

    """
    Equation
    tan(theta) = 2*(b-x/(a**2))/2
    """
    
    def theta(a,b,x):
        half = b*(a**2)/2
        if  half >= x:
            y = 2*(b-x/(a**2))/2
            return math.degrees(math.atan(y))
        else:
            y = (a*(b**2))/2*x
            return math.degrees(math.atan(y))
    print(theta(a,b,x))

if __name__=="__main__":
    main()
