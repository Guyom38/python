def GenereMat2D(xDim, yDim, valeurDefaut):
    return [[valeurDefaut for x in range(xDim)] for i in range(yDim)]

def iif(condition, vrai, faux):
    if condition:
        return vrai
    else:
        return faux



if __name__ == '__main__':
    plateau_de_jeu = GenereMat2D(10, 5, " ")
    
    plateau_de_jeu[0][1] = "X"
    for ligne in plateau_de_jeu:
        print(str(ligne))
