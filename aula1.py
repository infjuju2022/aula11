peso=58
altura=1.61
imc=peso/(altura**2)
if imc < 18.49:
    print("voce esta abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("voce esta com peso normal")
elif imc >=25 and imc < 30:
    print(" voce esta acima do peso")
elif imc >= 30:
    print ("acima do peso")

