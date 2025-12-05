===========================================
Herramienta: copiaratxt.exe
===========================================

Descripción:
------------
Este programa copia todos los archivos de una carpeta origen hacia una carpeta destino,
replicando la estructura completa de subcarpetas. Al copiar, agrega la extensión ".txt"
a cada archivo para facilitar su subida o procesamiento posterior.

Además:
- Ignora automáticamente las carpetas: .venv, venv, dist, build, __pycache__.
- Incluye la carpeta raíz de origen dentro de la carpeta destino, evitando mezclar
  exportaciones de diferentes proyectos.
- Permite aplicar un filtro opcional por extensiones de archivo.

Uso:
----
copiaratxt.exe <origen> <destino> [extensiones...]

Ejemplos:
---------
1. Copiar todo el contenido:
   copiaratxt.exe C:\Desarrollo\Fuentes\Fuenteatxt C:\Desarrollo\Fuentes\Exportar

   Resultado:
   C:\Desarrollo\Fuentes\Exportar\Fuenteatxt\...

2. Copiar solo archivos de código fuente (.c, .cpp, .h):
   copiaratxt.exe C:\Desarrollo\Fuentes\Fuenteatxt C:\Desarrollo\Fuentes\Exportar .c .cpp .h

   Resultado:
   C:\Desarrollo\Fuentes\Exportar\Fuenteatxt\...
   (solo se copian archivos con esas extensiones)

Notas:
------
- En PowerShell, si ejecutás desde la carpeta donde está el .exe, usá:
  .\copiaratxt.exe ...
- No uses comas entre parámetros, solo espacios.
- Los atributos de los archivos (fecha de modificación, permisos básicos) se conservan.

===========================================




para compilar ejecutable:
 python -m PyInstaller --onefile --name "copiaratxt" copiar_txt.py