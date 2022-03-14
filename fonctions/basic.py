def GenereMat2D(dimX, dimY, valeurDefaut):
    return [[valeurDefaut for x in range(dimY)] for i in range(dimX)]

def iif(condition, vrai, faux):
    if condition:
        return vrai
    else:
        return faux



if __name__ == '__main__':
    plateau_de_jeu = GenereMat2D(10, 5, ".")
    
    plateau_de_jeu[0][1] = "*"
    dimX = len(plateau_de_jeu)
    dimY = len(plateau_de_jeu[0])
    
    for y in range(0, dimY):
        ligne = ""
        for x in range(0, dimX):
            ligne += plateau_de_jeu[x][y]
        print(ligne)
