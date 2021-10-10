def computescore(Scr):
    if Scr < 0.6:
        print("F")
    elif Scr >= 0.6 and Scr < 0.7:
        print("D")
    elif Scr >= 0.7 and Scr < 0.8:
        print("C")
    elif Scr >= 0.8 and Scr < 0.9:
        print("B")
    elif Scr >= 0.9 and Scr < 1:
        print(A)
    else:
        print("bad score")
computescore(12) # in ra bad score
