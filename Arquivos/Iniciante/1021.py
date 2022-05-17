n = float(input())
if n >= 100:
    cem = n//100
    n -= cem*100
else:
    cem = 0

if n >= 50:
    cinquenta = n//50
    n -= cinquenta*50
else:
    cinquenta = 0

if n >= 20:
    vinte = n//20
    n -= vinte*20 
else:
    vinte = 0

if n >= 10:
    dez = n//10
    n -= dez*10
else:
    dez = 0

if n >= 5:
    cinco = n//5
    n -= cinco*5
else:
    cinco = 0

if n >= 2:
    dois = n//2
    n -= dois*2
else:
    dois = 0

if n >= 1:
    um = n//1
    n -= um*1
else:
    um = 0

if n >= 0.50:
    cinquenta_c = n//0.50
    n = (n - cinquenta_c*0.50) + 0.001
else:
    cinquenta_c = 0

if n >= 0.25:
    vinte_c = n//0.25
    n = (n - vinte_c*0.25) + 0.001
else:
    vinte_c = 0

if n >= 0.10:
    dez_c = n//0.10
    n = (n - dez_c*0.10) + 0.001
else:
    dez_c = 0

if n >= 0.05:
    cinco_c = n//0.05
    n = (n - cinco_c*0.05) + 0.001
else:
    cinco_c = 0

if n >= 0.01:
    um_c = n//0.01
    n -= um_c*0.01
else:
    um_c = 0

print("NOTAS:")
print("{:.0f} nota(s) de R$ 100.00\n{:.0f} nota(s) de R$ 50.00\n{:.0f} nota(s) de R$ 20.00\n{:.0f} nota(s) de R$ 10.00\n{:.0f} nota(s) de R$ 5.00\n{:.0f} nota(s) de R$ 2.00".format(cem, cinquenta, vinte, dez, cinco, dois))
print("MOEDAS:")
print("{:.0f} moeda(s) de R$ 1.00\n{:.0f} moeda(s) de R$ 0.50\n{:.0f} moeda(s) de R$ 0.25\n{:.0f} moeda(s) de R$ 0.10\n{:.0f} moeda(s) de R$ 0.05\n{:.0f} moeda(s) de R$ 0.01".format(um, cinquenta_c, vinte_c, dez_c, cinco_c, um_c))


