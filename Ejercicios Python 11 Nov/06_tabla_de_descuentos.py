def pinta_tabla():
    tabla = [
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],
        [1,2,3,4,5,6,7,8,9,0],
        [0,9,8,7,6,5,4,3,2,1],
    ]
    for f in tabla:
        for c in f:
            print(f"{c}\t", end="")
        print()

def pinta_tabla2(filas,cols):
    cadena = "<table>"
    for f in range(filas):
        cadena += "<tr>"
        for c in range(cols):
            cadena += f"<td>({f},{c})</td>"
        cadena += "</tr>"
    cadena += "</table>"
    return cadena

print(pinta_tabla2(10,10))
