alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt (b_text, a_shift):  # definido uma função e um parametro
    texto_cod = ""              # esta variavel vai receber as letras formando um texto.
    for letra in b_text:        # loop = para cada letra e b_text:
        posisao = alphabet.index(letra)   # variavel posisao recebe da lista alpahet a posicao da (letra) no loop ques está na lista
        nova_posicao = posisao + a_shift  # a variavel nova posicao recebe a posicao adotada mais o numero escolhido. Ex. posicao 4 + 5 = nova posisao 9
        nova_letra = alphabet[nova_posicao]  # a variavel nova letra recebe a letra que está na posicao na lista alpahbet. Ex. lista alfabeto[posicao 9] = m
        texto_cod += nova_letra  # variavel texto_cod recebe a nova letra somando a string.
    print(texto_cod)

encrypt(b_text=text, a_shift=shift)   #CHAMAR A FUNÇÃO SEMPRE USANDO O PARAMETRO E O ARGUMENTO.