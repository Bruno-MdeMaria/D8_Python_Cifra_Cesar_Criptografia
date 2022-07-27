alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def cesar (b_text, a_shift, c_direction):
    new_text = ""
    if direction == "encode":
        for letra in b_text:
            posisao = alphabet.index(letra)   # variavel posisao recebe da lista alpahet a posicao da (letra) no loop ques está na lista
            nova_posicao = posisao + a_shift  # a variavel nova posicao recebe a posicao adotada mais o numero escolhido. Ex. posicao 4 + 5 = nova posisao 9
            nova_letra = alphabet[nova_posicao]  # a variavel nova letra recebe a letra que está na posicao na lista alpahbet. Ex. lista alfabeto[posicao 9] = m
            new_text += nova_letra  # variavel new_text recebe a nova letra somando a string.
        print(f"The encode text is {new_text}")
    elif direction == "decode":
         for letra in b_text:
            nova_lista = list(reversed(alphabet))  #utilizando a função colocar a lista organizada de traz para frente.
            posisao = nova_lista.index(letra)
            nova_posicao = posisao + a_shift
            nova_letra = nova_lista[nova_posicao]
            new_text += nova_letra
    print(f"The encode text is {new_text}")
    
cesar (b_text=text, a_shift=shift, c_direction=direction)   #CHAMAR A FUNÇÃO SEMPRE USANDO O PARAMETRO E O ARGUMENTO.
 
