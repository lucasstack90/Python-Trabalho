
import random

numero = random.randint(1, 10)

chute = int(input("Adivinhe um n° de 1 a 10: "))

if chute == numero:
    print("Você acertou!!") 
else: 
    print("Você Errou!!!") 
    print("O n° era:", numero)








