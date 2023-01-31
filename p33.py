import re

def common_elements(str1, str2):
    return list(set(str1).intersection(set(str2)))


def fun_frac(nom, denom):
    nom = str(nom)
    denom = str(denom)
    common = common_elements(nom, denom)
    if len(common) == 1 and "0" not in common:
        
        nom = re.sub(common[0], "", nom, count = 1)
        denom = re.sub(common[0], "", denom, count = 1)
    
        return nom, denom
    else:
        return 0, 0
    
    
digit_frac1 = []
digit_frac2 = []

for i in range(10,100):
    for j in range(i+1, 100):
        nom, denom = fun_frac(i,j)
        nom = int(nom)
        denom = int(denom)

        if nom > 0 and denom > 0 and nom/denom == i/j:
            digit_frac1.append((nom, denom))
            digit_frac2.append((i, j))
            

total_nom = 1
total_denom = 1
for i in range(4):
    total_nom *= digit_frac1[i][0]
    total_denom *= digit_frac1[i][1]

print(total_denom/total_nom)