# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
import random
import timeit

def terminate(err):
    print("Script terminates due to ", err, "!")

def inputTest_aux(l, i, s):
    if l == []:
        raise ValueError("No empty list allowed!")
        terminate("ValueError")
    if s < 0:
        raise ValueError("No negative integer values for s!")
        terminate("ValueError")
    if (type(i) != int) :
        raise ValueError("i is not an integer!")
        terminate("ValueError")
    elif i < 0 :
        raise ValueError("i is not a positive integer!")
        terminate("ValueError")


def sum_possible_aux(l, i, s):
    """
    Quit ugly code....
    What could be improved and how?s
    """
    inputTest_aux(l, i, s)
    if ( s == 0 ) or ( i == 0 ):
        return []
    elif sum(l[:i+1]) == s:
        return l[:]
    elif sum(l[:i+1]) < s:
        return None
    elif sum(l[:i+1]) > s:
        # for m in l[:i+1]:
        #     if m == s:
        #         return [m]
        
        lcopy = l[:i+1]
        for m in range(len(l[:i+1])):
            lnew = lcopy[:m]+lcopy[m+1:]
            if len(lnew) >= 1:
                res = sum_possible_aux(lnew, len(lnew), s)
                if (type(res) == list) and (len(res) > 0):
                    return res 

        return None

def sum_possible(l, s):
    return sum_possible_aux(l, len(l)-1, s)


# l = [10, 45, 2, 63, 7, 2, 4]
# i = len(l)-1
# s = 8
# print(sum_possible_aux(l, i, s))

def main():
    n = int(input("Geben Sie die Länge der Liste ein: "))
    k = int(input("Geben Sie eine Höchstzahl ein: "))
    l = []
    for i in range(n):
        l.append(random.randint(1, k))
    print(l)

    print()
    s = int(input("Geben Sie eine Zahl ein: "))
    print("*** Programm rechnet ***")
    g = globals()
    g["l"] = l
    g["s"] = s
    t = timeit.timeit('print("Ergebnis: " + str(sum_possible(l, s)))', number = 1, globals = g)
    print("Zeit: " + str(t) + " s")


main()
