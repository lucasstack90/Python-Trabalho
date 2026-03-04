
import random / estamos adicionando a Biblioteca 

numero = random.randint(1, 10) / escolher um n° entre 1 e 10.

chute = int(input("Adivinhe um n° de 1 a 10: ")) / o int reconhece o n°, input possibilita que o jogador digite o n°.

if chute == numero: / se for verdadeiro vai mandar para o jogador uma mensagem "Você acertou".
    print("Você acertou!!") 

else:  / se errar, vai mandar a mensagem "Você Errou!!!" e mostrar o n° correto.
    print("Você Errou!!!") 
    print("O n° era:", numero)








