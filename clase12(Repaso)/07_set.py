materiasPendientes = {"Historia", "Geografia", "Matematica"}

if "Matematica" in materiasPendientes:
    print("esta dentro del set")

materiasPendientes.add("Programaciom")
materiasPendientes.remove("Geografia")

print(materiasPendientes)

#en el set si tratamos de agregar un valor que ya estaba previamente ene l set, no sucede nada
materiasPendientes.add("Historia")
print(materiasPendientes)
