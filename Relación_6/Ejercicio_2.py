nombre = input ("Introduzca su nombre ")
edad = int(input("introduzca su edad "))
direccion = input("ponga su direccion ")
telefono = int(input("ponga su telefono "))

thisdict =	{
  "nombre": nombre,
  "edad": edad,
  "direccion": direccion,
  "telefono": telefono
}


print (thisdict["nombre"] + " tiene " + str(thisdict["edad"]) + " años ", "vive en " + thisdict["direccion"] + " y su número de teléfono es " + str(thisdict["telefono"]) )