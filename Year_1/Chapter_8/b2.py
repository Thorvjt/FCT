
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        impos = line.find(":")
        piece=line[impos+1:]
        value=float(piece)
        print(value)