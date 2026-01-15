p = input("Introduzca la fecha en formato 'dd/mm/aaaa': ")
dia = p.split("/")[0]
mes = p.split("/")[1]
anio = p.split("/")[2]

mes_txt = {
    '01':'enero',
    '02':'febrero',
    '03':'marzo',
    '04':'abril',
    '05':'mayo',
    '06':'junio',
    '07':'julio',
    '08':'agosto',
    '09':'septiembre',
    '10':'octubre',
    '11':'noviembre',
    '12':'diciembre'
}

print (dia + " de "  + mes_txt[mes] + " de " + anio)