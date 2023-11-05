## Mini tutorial para ejecutar la siguiente aplicación en sus máquinas 🚀

```bash
# Paso 1: Instalar Flask
pip install Flask

# Paso 2: Configurar un entorno virtual
# Si no tienes venv instalado, ejecuta:
python -m ensurepip --default-pip

# Paso 3: Crear y activar el entorno virtual
python -m venv myenv

# En sistemas Windows:
myenv\Scripts\activate

# En sistemas Unix/Linux:
source myenv/bin/activate

# Paso 4: Instalar las dependencias
# Dentro del entorno virtual, instala las siguientes dependencias:
pip install pandas scikit-learn Flask
