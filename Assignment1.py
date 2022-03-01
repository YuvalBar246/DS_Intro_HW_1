#Yuval Bar
#206011355

##Task 1
def my_func (x1 = None, x2 = None, x3 = None):
    if ((type(x1) == float) and (type(x2) == float) and (type(x3) == float)):
        a = x1+x2+x3
        b = x2+x3
        if (a == 0):
            return "Not a number – denominator equals zero"
        else:    
            return float((a*b*x3)/a)
    else:
        return "Error: parameters should be double"
                
##Task 2
def convert(hours = None, minutes = 0):
    try:
        if ((hours >=0) and (minutes >=0)):
            Hs = hours*60*60
            Ms = minutes*60
            return Hs+Ms
        else:
            return "Input error!"
    except:
        return "Error - Enter a numbers"