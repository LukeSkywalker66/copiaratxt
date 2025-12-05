import os
import shutil
import sys

def copiar_con_txt(origen, destino):
    for root, dirs, files in os.walk(origen):
        # Ruta relativa desde la carpeta origen
        rel_path = os.path.relpath(root, origen)
        destino_actual = os.path.join(destino, rel_path)

        # Crear la carpeta correspondiente en destino
        os.makedirs(destino_actual, exist_ok=True)

        # Copiar cada archivo agregando ".txt"
        for archivo in files:
            ruta_origen = os.path.join(root, archivo)
            nuevo_nombre = archivo + ".txt"
            ruta_destino = os.path.join(destino_actual, nuevo_nombre)
            shutil.copy2(ruta_origen, ruta_destino)
            print(f"Copiado: {ruta_origen} -> {ruta_destino}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: copiar_txt.exe <origen> <destino>")
    else:
        origen = sys.argv[1]
        destino = sys.argv[2]
        copiar_con_txt(origen, destino)