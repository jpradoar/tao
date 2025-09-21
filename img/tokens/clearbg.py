import os
from rembg import remove
from PIL import Image

def quitar_fondo_pngs():
    # Directorio actual
    directorio = os.getcwd()
    # Iterar por todos los archivos PNG
    for archivo in os.listdir(directorio):
        if archivo.lower().endswith(".png"):
            ruta_entrada = os.path.join(directorio, archivo)
            ruta_salida = os.path.join(directorio, f"sin_fondo_{archivo}")

            try:
                # Abrir imagen
                with Image.open(ruta_entrada) as img:
                    # Quitar fondo
                    img_sin_fondo = remove(img)
                    # Guardar resultado en formato PNG
                    img_sin_fondo.save(ruta_salida, "PNG")
                    print(f"✅ Fondo eliminado: {archivo} -> {ruta_salida}")
            except Exception as e:
                print(f"❌ Error con {archivo}: {e}")

if __name__ == "__main__":
    quitar_fondo_pngs()
