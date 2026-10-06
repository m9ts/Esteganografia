# Esteganografia usando LSB

Projeto de esteganografia utilizando a técnica LSB (Least Significant Bit) para esconder uma mensagem de texto dentro de uma imagem.

A mensagem é convertida em bits e armazenada nos bits menos significativos dos canais RGB da imagem. Depois, o programa recupera esses bits e reconstrói a mensagem original.

## Como usar

### Biblioteca

Antes de executar os scripts, é necessário instalar a biblioteca Pillow, utilizada para manipular as imagens.

No terminal, execute:

```bash
py -m pip install Pillow
````

 ### Esconder uma mensagem

 Para esconder uma mensagem, coloque a imagem `original.png` na mesma pasta do arquivo `encrypt.py`.

 No arquivo `encrypt.py`, altere o texto da variável `mensagem`:

```
mensagem = "a random secret message"
```

 Depois, execute:

```
py encrypt.py
```

 O programa irá utilizar a imagem `original.png` e criar uma nova imagem chamada `nova_imagem.png`, contendo a mensagem escondida.

 ### Recuperar uma mensagem

 Depois de executar o `encrypt.py`, será criada a imagem `nova_imagem.png`.

 Para recuperar a mensagem escondida, execute:

```
py decrypt.py
```

 O programa irá ler os bits menos significativos da imagem e reconstruir a mensagem original.

 A saída será semelhante a:

```
Mensagem encontrada:
a random secret message
```

 ## Arquivos

 - `encrypt.py` — esconde a mensagem dentro da imagem.
- `decrypt.py` — recupera a mensagem escondida.
- `original.png` — imagem original utilizada para esconder a mensagem.
- `nova_imagem.png` — imagem resultante contendo a mensagem escondida.

