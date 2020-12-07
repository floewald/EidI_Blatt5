# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
def swap(s,i,j):
    return s[0:i]+s[j]+s[i+1:j]+s[i]+s[j+1:len(s)]

def sort(s):
    return "".join((sorted(s)[::-1]))

def IntegerTest(n_inp):
    try:
        n = int(n_inp)
    except ValueError:
        print("Invalid Input!")
        print("Next time use an integer...")
        exit()

    if n <= 0:
        raise ValueError("That is a negative integer!")
        print("Program terminates")
        exit()
    return n

def maximize(x, k):
    if type(x) != str:
        raise TypeError("Input is not a string!")
        exit()
    else:
        for digit in s:
            if not(digit in "0123456789"):
                raise ValueError("Only positive integer numbers valid!", digit, " is not a valid value!")
    
    if (k == 0) or (len(x) == 1):
        return x
    else:
        i, j = 0, 0
        l = len(x)
        xsorted = sort(x)
        for m in range(l):
            if x[m] != xsorted[m]:
                i = m
                for n in range(i, l):
                    if x[n] == xsorted[m]:
                        j = n
                        break
                break
        xnew = swap(x, i, j)
        return maximize(xnew, k - 1)

s       = input("Please enter a big integer number (e.g. 223953):\n")
k_str   = input("Please enter a number positive integer for how many digits can be changed:\n")
k       = IntegerTest(k_str) 

print("Before function: \t", s)
print("After function: \t", maximize(s, k))