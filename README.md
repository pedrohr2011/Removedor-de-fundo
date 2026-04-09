# Removedor-de-fundo

[English](#english) | [Português](#português)

---

## English

A simple Python script I put together to automate removing backgrounds from images. It uses the `rembg` library to do the heavy lifting with AI, saving me from opening a photo editor every single time.

### What does it do?
- Removes backgrounds from any image (JPG, PNG, etc.).
- Outputs a PNG file with a transparent background.
- Runs locally on your machine.

### Getting started:
You'll need Python installed. The script uses two main packages:

```bash
pip install rembg pillow
```

*Tip: The first time you run it, it'll download the AI model automatically. It's normal for the first run to take a few minutes.*

### How to use:
1. Drop the image you want to process in the same folder as the script.
2. Open `Removedor.py` and put your image name in the `imagem_entrada` variable.
3. Run the script:
   ```bash
   python Removedor.py
   ```
4. The finished file will appear as `foto_sem_fundo.png`.

---

## Português

Um script simples em Python que usei para automatizar a remoção de fundo de imagens. Ele usa a biblioteca `rembg` pra fazer o trabalho pesado com IA, poupando o tempo de ter que abrir um editor de fotos toda vez.

### O que ele faz?
- Tira o fundo de qualquer imagem (JPG, PNG, etc).
- Cospe um arquivo PNG com fundo transparente.
- Funciona direto no seu computador.

### Pra rodar aí:
Você vai precisar do Python instalado. O script usa dois pacotes principais:

```bash
pip install rembg pillow
```

*Dica: Na primeira vez que rodar, ele vai baixar o modelo da IA sozinho. É normal demorar alguns minutos nessa primeira vez.*

### Como usar:
1. Joga a imagem que você quer tratar na mesma pasta do script.
2. Abre o `Removedor.py` e coloca o nome da sua imagem na variável `imagem_entrada`.
3. Roda o script:
   ```bash
   python Removedor.py
   ```
4. O arquivo pronto vai aparecer como `foto_sem_fundo.png`.

---
Made by [Pedro](https://github.com/pedrohr2011). If this script helped you, feel free to leave a star!