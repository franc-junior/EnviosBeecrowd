numero = int(input())
restoCem = numero % 100
restoCinquen = restoCem % 50
restoVinte = restoCinquen % 20
restoDez = restoVinte % 10
restoCinco = restoDez % 5
restoDois = restoCinco % 2
restoUm = restoDois % 1

print(numero)
if numero >= 100:
    cem = (numero - restoCem) / 100
    print("{:.0f}".format(cem), "nota(s) de R$ 100,00")
else:
    print(0, "nota(s) de R$ 100,00") 

if restoCem >= 50:
    cinquen = (restoCem - restoCinquen) / 50
    print("{:.0f}".format(cinquen), "nota(s) de R$ 50,00")
else:
    print(0, "nota(s) de R$ 50,00")

if restoCinquen >= 20:
    vinte = (restoCinquen - restoVinte) / 20
    print("{:.0f}".format(vinte), "nota(s) de R$ 20,00")
else:
    print(0, "nota(s) de R$ 20,00")

if restoVinte >= 10:
    dez = (restoVinte - restoDez) / 10
    print("{:.0f}".format(dez), "nota(s) de R$ 10,00")
else:
    print(0, "nota(s) de R$ 10,00") 

if restoDez >= 5:
    cinco = (restoDez - restoCinco) / 5
    print("{:.0f}".format(cinco), "nota(s) de R$ 5,00")
else:
    print(0, "nota(s) de R$ 5,00")

if restoCinco >= 2:
    dois = (restoCinco - restoDois) / 2
    print("{:.0f}".format(dois), "nota(s) de R$ 2,00")
else:
    print(0, "nota(s) de R$ 2,00")

if restoDois >= 1:
    um = (restoDois - restoUm) / 1
    print("{:.0f}".format(um), "nota(s) de R$ 1,00")
else:
    print(0, "nota(s) de R$ 1,00")    


#valor = 1
#x = range(1,10)
#while(valor < x):
#    print("valor ainda menor que 10 igual a:", valor)
#    valor += 1