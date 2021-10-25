string = 'X-DSPAM-Confidence:0.8475'
impos = string.find(":")
piece=string[impos+1:]
value=float(piece)
print(value)