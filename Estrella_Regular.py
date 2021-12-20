def dibujar_estrella(dimensión,color):
    contar = 0
    ángulo = 80

    while contar <= 9:
        turtle.forward(dimensión)
        turtle.right(ángulo)
        contar += 1
    return
dibujar_estrella(180, "red")    