from PIL import Image

imagem_secreta = "nova_imagem.png"

imagem = Image.open(imagem_secreta).convert("RGB")

pixels = imagem.get_flattened_data()

bits = []

for r, g, b in pixels:

    # Pegamos somente o último bit de cada canal

    bits.append(r & 1)
    bits.append(g & 1)
    bits.append(b & 1)


mensagem = ""

for i in range(0, len(bits), 8):

    # pega 8 bits para formar um caractere
    grupo = bits[i:i + 8]

    if len(grupo) < 8:
        break

    numero = 0

    # Transformamos os 8 bits em um número
    for bit in grupo:
        # << 1 desloca os bits uma posição para a esquerda (multiplica por 2)
        # | bit adiciona o novo bit ao final do número
        # Equivale a: numero = numero * 2 + bit
        numero = (numero << 1) | bit

    if numero == 0:
        break

    # chr(numero) transforma o número em um caractere 
    # += adiciona esse cractere ao final da mensagem
    mensagem += chr(numero)


print("Mensagem encontrada:")
print(mensagem)
