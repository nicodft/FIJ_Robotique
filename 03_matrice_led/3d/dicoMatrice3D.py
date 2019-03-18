dico3D={"a":[[[0,1,0],[1,1,1],[0,1,0]],
             [[1,0,1],[0,0,0],[1,0,1]],
             [[1,1,1],[1,1,1],[1,1,1]],
             [[1,0,1],[0,0,0],[1,0,1]],
             [[1,0,1],[0,0,0],[1,0,1]]],
        "b":[[[1,1,0],[1,1,0],[1,1,0]],
             [[1,0,1],[1,0,1],[1,0,1]],
             [[1,1,0],[1,1,0],[1,1,0]],
             [[1,0,1],[1,0,1],[1,0,1]],
             [[1,1,0],[1,1,0],[1,1,0]]]
}


def testMatrice3D(lettre="a", face=1):
    i=0
    #face1 ou 3
    if face==1 or face ==3:
        j=face-1
        while i < 5:
            ligne =""
            for led in dico3D[lettre][i][j]:
                ligne += str(led)
            ligne =ligne.replace("1","[*]")
            print(ligne.replace("0","[ ]"))
            i+=1
    #face 2 ou 4
    elif face==2 or face==4:
        if face==2:
            l=2
        else:
            l=0
        while i < 5:
            j=0
            ligne =""
            while j < 3:
                ligne+= str(dico3D[lettre][i][j][l])
                j+=1
            ligne =ligne.replace("1","[*]")
            print(ligne.replace("0","[ ]"))
            i+=1

def testFacesMatrice3D(lettre="a"):
    face = 1
    while face <=4:
        print("\nface",face)
        testMatrice3D(lettre,face)
        face+=1

testFacesMatrice3D("a")
