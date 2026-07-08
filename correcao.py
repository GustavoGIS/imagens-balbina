from PIL import Image, ImageOps
import os

pasta = os.path.dirname(os.path.abspath(__file__))

for nome in os.listdir(pasta):
    if nome.lower().endswith((".jpg", ".jpeg", ".png")):
        caminho = os.path.join(pasta, nome)
        img = Image.open(caminho)
        img_corrigida = ImageOps.exif_transpose(img)
        img_corrigida.save(caminho)
        print(f"Corrigido: {nome}")