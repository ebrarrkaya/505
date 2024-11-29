toplampoz=0
toplamneg=0
liste=[-1,-3,-10,-18,-20,22,40,7]
for x in liste:
    if x>0:
        toplampoz+=x
    elif x<0:
        toplamneg+=x
print("Pozitif sayilarin toplami:{}".format(toplampoz))
print("Negatif sayilarin toplami:{}".format(toplamneg))
