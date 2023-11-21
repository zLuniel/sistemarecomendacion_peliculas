## Mini tutorial para ejecutar la siguiente aplicación en sus máquinas 🚀

```bash
# Paso 1: Configurar un entorno virtual
# Si no tienes venv instalado, ejecuta:
python -m ensurepip --default-pip

# Paso 2: Crear y activar el entorno virtual
python -m venv myenv

# En sistemas Windows:
myenv\Scripts\activate

# En sistemas Unix/Linux:
source myenv/bin/activate

# Paso 3: Instalar las dependencias
# Dentro del entorno virtual, instala las siguientes dependencias:
python -m pip install -r requirements.txt
