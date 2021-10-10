def computepay(Hours, Rate):
    k1 = Hours*Rate
    k2 = 5+10.5*1.5
    if Hours > 40:
        print(k2 + k1)
    else:
        print(k1)
computepay(45, 10.5)