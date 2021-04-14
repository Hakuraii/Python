#CPO
#Triangle de pascale

def TriangleDePascale(maximum):
    triangle = [[1], [1, 1]]
    triangleTemp = []
    while(len(triangle) < maximum):
        n = 0
        while(n < len(triangle[len(triangle) - 1]) - 1):
            triangleTemp.append(triangle[len(triangle) - 1][n] + triangle[len(triangle) - 1][n + 1])
            n += 1
        triangleTemp.insert(0, 1)
        triangleTemp.append(1)
        triangle.append(list(triangleTemp))
        triangleTemp.clear()
    return triangle

TrianglePascale = TriangleDePascale(10000)

space = ' '

for i in range(0, len(TrianglePascale)):
    Ligne = TrianglePascale[i]
    LigneStr = ' '.join(map(str, Ligne))
    print(LigneStr)