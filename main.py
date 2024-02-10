from fractions import *

def turnintofrac(arr,lins,cols):
    for l in range(lins):
        for e in range(cols):
            arr[l][e] = Fraction(arr[l][e])

def swaplines(arr, len, ind1, ind2):
    #copy = [0,]*len
    copy = [0 for x in range(len)]
    for i in range(len):
        copy[i] = arr[ind1][i]
        arr[ind1][i] = arr[ind2][i]
    for j in range(len):
        arr[ind2][j] = copy[j]

def loadinv(arr, n):
    for l in range(n):
        for e in range(n):
            if(l == e):
                arr[l][n + e] = 1
            else:
                arr[l][n + e] = 0

def normal(arr, cols, line):
    dt = arr[line][line]
    value = Fraction(1,1)/dt
    for e in range(0, cols):
        arr[line][e] = value * arr[line][e]
    return dt

def zerobelow(arr, lines, cols, col):
    for l in range(col+1, lines):
        coef = -arr[l][col]
        for c in range(col, cols):
            arr[l][c] = coef*arr[col][c] + arr[l][c]

def zeroabove(arr, lines, cols, col):
    for l in range(col-1,-1,-1):
        coef = -arr[l][col]
        for c in range(col, cols):
            arr[l][c] = coef*arr[col][c] + arr[l][c]

def nonzero(arr, lines, cols, col):
    zero = False
    c = 1
    d = Fraction(1,1)
    if(arr[col][col] == Fraction(0)):
        zero = True
    while(zero):
        #if c fora throw exception
        swaplines(arr, cols, col, col+c)
        d *= -1
        c += 1
        if(arr[col][col] != Fraction(0)):
            zero = False
    return d

def solvesystem(arr, n):
    turnintofrac(arr,n,n+1)
    for col in range(n):
        nonzero(arr, n, n+1, col)
        normal(arr,n+1,col)
        zerobelow(arr,n,n+1,col)
    for abv in range(n-1,0,-1):
        zeroabove(arr,n,n+1,abv)
    ans = [0 for x in range(n)]
    for a in range(n):
        ans[a] = str(arr[a][n])
    print(ans)

def finddet(arr,n):
    turnintofrac(arr,n,n)
    det = Fraction(1,1)
    for col in range(n):
        det *= nonzero(arr, n, n, col)
        det *= normal(arr, n, col)
        zerobelow(arr, n, n, col)
    print(str(det))

def findinv(arr,n):
    loadinv(arr, n)
    turnintofrac(arr, n, 2*n)
    for col in range(n):
        nonzero(arr, n, 2*n, col)
        normal(arr, 2*n, col)
        zerobelow(arr, n, 2*n, col)
    for abv in range(n-1, 0, -1):
        zeroabove(arr, n, 2*n, abv)
    ans = [[0 for x in range(n)] for y in range(n)]
    for l in range(n):
        for e in range(n):
            ans[l][e] = str(arr[l][n+e])
        print(ans[l])

#-----------------------DEBUGGING TOOLS---------------------------
#arrs = [[0,]*(n+1)]*n
#arrd = [[0,]*n]*n
#arrinv = [[5,]*(2*n)]*n
#arr = [[0,1,2,0],[1,0,4,1],[2,3,2,8]]
#arr = [[0,1,2,0,0,0],[1,0,4,0,0,0],[2,3,2,0,0,0]]
#-----------------------------------------------------------------
print("\n O programa calcula determinante, matriz inversa e resolve sistema linear.")
n = int(input(" Digite a ordem da matriz ou numero de equacoes: "))
if (n < 2 or n > 100):
    print(" Erro, o valor deve estar entre 2 e 100")
    exit()
print("\n 1 - Sistema \n 2 - Determinante \n 3 - Inversa\n")
o = int(input(" Digite o numero referente a operacao que deseja realizar: "))
if ((o != 1) and ( o != 2) and ( o != 3)):
    print(" Erro, o valor deve ser 1, 2 ou 3")
    exit()
else:
    if(o == 1):
        arrs = [[0 for x in range(n + 1)] for y in range(n)]
        print("\n Digite agora as entradas separadas por virgula")
        print(" Exemplo: para x - (1/2)y + 0.4y = 0 digite \'1,-1/2,0.4,0\'")
        instr = ["0" for z in range(n)]
        for i in range(n):
            instr[i] = input("\n ")
            arrs[i] = instr[i].split(",")
        print("\n")
        solvesystem(arrs, n)
    elif(o == 2):
        arrd = [[0 for x in range(n)] for y in range(n)]
        print("\n Digite agora as entradas separadas por virgula")
        print(" Exemplo: para uma linha = (-1.2 t0 7/5)  digite \"-1.2,0,7/5\"")
        instr = ["0" for z in range(n)]
        for i in range(n):
            instr[i] = input("\n ")
            arrd[i] = instr[i].split(',')
        print("\n")
        finddet(arrd, n)
    else:
        arri = [[0 for x in range(2 * n)] for y in range(n)]
        print("\n Digite agora as entradas separadas por virgula")
        print(" Exemplo: para uma linha = (-1.2 0 7/5)  digite \'-1.2,0,7/5\'")
        instr = ["0" for z in range(n)]
        for i in range(n):
            instr[i] = input("\n ")
            for j in range(n):
                print(instr[i])#
                instr[i] += ',0'
            arri[i] = instr[i].split(',')
        print("\n")
        findinv(arri, n)
    w = input("")
