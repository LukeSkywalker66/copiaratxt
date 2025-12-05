import os
import shutil
import sys

# Carpetas a ignorar
IGNORAR = {".venv", "venv", "dist", "build", "__pycache__"}

def copiar_con_txt(origen, destino, extensiones=None):
    # Normalizar extensiones (ej: ".c", ".cpp", ".h")
    if extensiones:
        extensiones = {ext.lower() for ext in extensiones}

    # Nombre de la carpeta raíz
    raiz_nombre = os.path.basename(os.path.normpath(origen))
    destino_raiz = os.path.join(destino, raiz_nombre)

    for root, dirs, files in os.walk(origen):
        # Filtrar directorios a ignorar
        dirs[:] = [d for d in dirs if d not in IGNORAR]

        # Ruta relativa desde la carpeta origen
        rel_path = os.path.relpath(root, origen)
        destino_actual = os.path.join(destino_raiz, rel_path)

        # Crear la carpeta correspondiente en destino
        os.makedirs(destino_actual, exist_ok=True)

        # Copiar cada archivo agregando ".txt"
        for archivo in files:
            ruta_origen = os.path.join(root, archivo)

            # Si hay filtro de extensiones, aplicar
            if extensiones:
                _, ext = os.path.splitext(archivo)
                if ext.lower() not in extensiones:
                    continue

            nuevo_nombre = archivo + ".txt"
            ruta_destino = os.path.join(destino_actual, nuevo_nombre)
            shutil.copy2(ruta_origen, ruta_destino)
            print(f"Copiado: {ruta_origen} -> {ruta_destino}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: copiaratxt.exe <origen> <destino> [extensiones...]")
        print("Ejemplo: copiaratxt.exe C:/origen C:/destino .c .cpp .h")
    else:
        origen = sys.argv[1]
        destino = sys.argv[2]
        extensiones = sys.argv[3:] if len(sys.argv) > 3 else None
        copiar_con_txt(origen, destino, extensiones)