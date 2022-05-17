dias = int(input())
anos = dias // 365
meses = (dias % 365) // 30
dia = dias - (anos * 365) - (meses * 30)
print(anos, "ano(s)")
print(meses, "mes(es)")
print(dia, "dia(s)")