import os
from rembg import remove
from PIL import Image

def quitar_fondo_pngs():
    directorio = "/images"  # volumen montado
    for archivo in os.listdir(directorio):
        if archivo.lower().endswith(".png"):
            ruta_entrada = os.path.join(directorio, archivo)

            try:
                with Image.open(ruta_entrada) as img:
                    img_sin_fondo = remove(img)
                    # Sobrescribe el mismo archivo
                    img_sin_fondo.save(ruta_entrada, "PNG")
                    print(f"✅ Fondo eliminado y sobrescrito: {archivo}")
            except Exception as e:
                print(f"❌ Error con {archivo}: {e}")

if __name__ == "__main__":
    quitar_fondo_pngs()
