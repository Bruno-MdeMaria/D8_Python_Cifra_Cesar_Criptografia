from imagem import logo
print(logo)
print("BEM VINDO AO PROGRAMA DE CODIFICAÇÃQO E DECODIFICAÇÃO CAESAR CIPHER!\n")

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(a_text, b_shift, c_direction):   # FUNÇÃO SIMPLIFICADA:
  texto_cifr = ""                                     # variavel recebe dentro de uma string letra por letra do loop
  if c_direction == "decode":                         # escolha entre decode e encode 
      b_shift *= -1                                   # decode é a posição da letra meno (-) o numero shift. Neste caso a variavel b_hift recebe o valor e multiplica por menos(-) 1. Ex: 5 * - 1 = (-)5.
  for letra in a_text:
    if letra in alfabeto:                              #se a letra estiver na lista alfabeto
        posicao = alfabeto.index(letra)                  # variavel posicao recebe da lista alfabeto a posicao da (letra) no loop que está na lista
        nova_posicao = posicao + b_shift                 # a variavel nova_posicao recebe a posição + o numero sfift defino acima com menos se for decode e com mais passadno direto pela função if e caindo aqui.
        texto_cifr += alfabeto[nova_posicao]             # a variavel texto_cifr recebe a letra que está na lista alfabeto na posição[] definida pela variavel nova_posicao.
    else: texto_cifr += letra
  print(f"Here's the {direction}d result: {texto_cifr}\n")


stop = False
while not stop:    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26                                  #para qualquer numero que colocar além da quanitdade que tem na lista a funcoa vai dividir e retornar um resto e este vai caber dentro da lista.
    caesar(a_text=text, b_shift=shift, c_direction=direction)
    nov = input("Quer tentar novamente? Digite sim ou não \n").lower()
    if nov == "não":
        stop = True
        print("\nOk, Goodbye!")
