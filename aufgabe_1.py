import random
import timeit

def sum_possible_aux(l, i, s):
    if s == 0 or i == 0:
        return []
    else:
        lsum = []
        for m in l:
            if m == s:
                return [m]
        
        if sum(l) == s:
            lsum = l[:]
        else:
            for m in range(i+1):
                lcopy = l[:]
                if sum(lcopy[:m]) + sum(lcopy[(m+1):]) != s:
                    del lcopy[m]
                    lsum = sum_possible_aux(lcopy, len(lcopy)-1, s)
        return lsum

def sum_possible(l, s):
    return None

l = [10, 45, 2, 63, 7, 2, 4]
i = len(l)-1
s = 62
print(sum_possible_aux(l, i, s))

# def main():
#     n = int(input("Geben Sie die Länge der Liste ein: "))
#     k = int(input("Geben Sie eine Höchstzahl ein: "))
#     l = []
#     for i in range(n):
#         l.append(random.randint(1, k))
#     print(l)

#     print()
#     s = int(input("Geben Sie eine Zahl ein: "))
#     print("*** Programm rechnet ***")
#     g = globals()
#     g["l"] = l
#     g["s"] = s
#     t = timeit.timeit('print("Ergebnis: " + str(sum_possible(l, s)))', number = 1, globals = g)
#     print("Zeit: " + str(t) + " s")


# main()
