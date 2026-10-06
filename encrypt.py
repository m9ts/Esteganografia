from PIL import Image

imagem = Image.open("original.png").convert("RGB")

mensagem = "a random secret message"

# Marca o fim da mensagem
mensagem += "\0"


# Transformar a mensagem em bits
bits = []

for caractere in mensagem:
    numero = ord(caractere)
    binario = format(numero, "08b")

    for bit in binario:
        bits.append(int(bit))


pixels = list(imagem.get_flattened_data())

novos_pixels = []

indice = 0

for r, g, b in pixels:

    if indice < len(bits):
        # r % 2 -> verifica se r é par (0) ou ímpar (1)
        # r - (r % 2) -> deixa r sempre par
        # bits[indice] -> coloca 0 ou 1 no final
        r = r - (r % 2) + bits[indice]
        indice += 1

    if indice < len(bits):
        g = g - (g % 2) + bits[indice]
        indice += 1

    if indice < len(bits):
        b = b - (b % 2) + bits[indice]
        indice += 1

    novos_pixels.append((r, g, b))


nova_imagem = Image.new("RGB", imagem.size)

nova_imagem.putdata(novos_pixels)

nova_imagem.save("nova_imagem.png")

print("A mensagem escondida")