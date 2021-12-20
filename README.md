# Estrella_Regular

Este es el enlace de mi repositorio: https://github.com/guerramorante/Estrella_Regular.git

![Ejercicio_EstrellaRegular](https://user-images.githubusercontent.com/91721714/146792341-34eea5e2-40c6-40e2-b082-590cb35946b8.PNG)


```
def dibujar_estrella(dimensión,color):
    contar = 0
    ángulo = 80

    while contar <= 9:
        turtle.forward(dimensión)
        turtle.right(ángulo)
        contar += 1
    return
dibujar_estrella(180, "red")    
