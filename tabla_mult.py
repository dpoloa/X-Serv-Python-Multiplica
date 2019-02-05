# Multiplication tables

print("")

for firstnum in range(1, 11):
    print("Tabla de multiplicar del " + str(firstnum))
    print("---------------------------")
    for secondnum in range(1, 11):
        print(str(firstnum) + " por " + str(secondnum) + " es " + str(firstnum * secondnum))

    print("")
