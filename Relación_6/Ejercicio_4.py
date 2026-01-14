p = input("Introduzca la fecha en formato 'dd/mm/aaaa': ")
dia = p.split("/")[0]
mes = p.split("/")[1]
anio = p.split("/")[2]

thisdict = {
    "dia": dia,
    "mes": mes,
    "anio": anio
}


print (thisdict["dia"] + " de "  + thisdict["mes"] + " de " + thisdict["anio"])