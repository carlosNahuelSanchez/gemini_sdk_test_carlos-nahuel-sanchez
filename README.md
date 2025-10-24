# gemini_sdk_test_carlos-nahuel-sanchez

## Actividades : Desarrollo

### 1. Comparativa entre API de Gemini y Vertex Ai
En el hipotetico caso que el entorno de desarrollo sea en una startup con un presupuesto limitado o una gran empresa con requisitos de seguridad especificos. Lo mas recomendable seria utilizar **Vertex Ai** ya que contiene Asistencia para empresas y una seguridad robusta. A pesar de la diferencia de precio que existe con la **API de Gemini** que es mas economica, la seguridad y soporte que ofrece Vertex Ai es mas adecuado para entornos empresariales

### 2. Pasos para correr aplicacion con la API de Gemini

1. Clonar el repositorio:
   ```bash
   git clone
    ```

2. Navegar al directorio del proyecto:
    ```bash
    cd gemini_sdk_test_carlos-nahuel-sanchez
    ```

3. Crear un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

4. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Configurar la variable de entorno para la API Key de Gemini:
    ```bash
        setx API_KEY "TU_API_KEY_AQUI"
    ```

6. Verificar si las dependencias se instalaron correctamente:
    ```bash
    pip list
    ```

7. Ejecutar la aplicación 

- Para generacion de texto:
    ```bash
    python generate_content.py
    ```
- Para generacion de texto en streaming:
    ```bash
    python generate_content_stream.py
    ```
- Para generacion multimodal:
    ```bash
    python multimodal_content.py
    ```

### 3. Reflexión sobre latencia

Teniendo en cuenta la siguiente consulta realizada a la API de Gemini:

```bash
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Porque recomiendas aprender Python como primer lenguaje de programación?",
)

print(response.text)
```

El modelo devolvio: 

```bash
1.  **Facilidad de Aprendizaje y Sintaxis Intuitiva:**
    *   **Legibilidad:** La sintaxis de Python es muy limpia y se parece mucho al lenguaje natural (inglés). Esto significa que es más fácil de leer, entender y escribir para los principiantes, que no tienen que luchar con símbolos o estructuras complejas desde el principio.
    *   **Menos Código:** Python permite lograr mucho con menos líneas de código en comparación con otros lenguajes (como Java o C++), lo que reduce la frustración inicial y permite a los estudiantes ver resultados rápidamente.
    *   **Curva de Aprendizaje Suave:** Su diseño prioriza la simplicidad, lo que hace que la curva de aprendizaje sea más gradual y menos intimidante.

2.  **Versatilidad y Amplio Campo de Aplicación:**
    *   **Multiusos:** Python no te encierra en un nicho. Puedes usarlo para desarrollo web (Django, Flask), inteligencia artificial y aprendizaje automático (TensorFlow, PyTorch, scikit-learn), ciencia de datos y análisis (Pandas, NumPy), automatización de tareas y scripting, desarrollo de juegos (Pygame), aplicaciones de escritorio, y mucho más.
    *   **Motivación:** Esta versatilidad permite a los principiantes explorar diferentes áreas y encontrar lo que más les apasione, manteniendo la motivación alta al ver las múltiples posibilidades.

3.  **Gran Comunidad y Abundantes Recursos:**
    *   **Soporte:** Python tiene una de las comunidades más grandes y activas del mundo. Esto significa que hay una cantidad inmensa de tutoriales, documentación, foros (como Stack Overflow), cursos y ejemplos de código disponibles.
    *   **Ayuda Inmediata:** Cuando un principiante se atasca (que es algo común y necesario al tediosos como llaves, puntos y comas obligatorios al final de cada línea, o la gestión de memoria.
tediosos como llaves, puntos y comas obligatorios al final de cada línea, o la gestión de memoria.
    *   **Indentación Obligatoria:** Python utiliza la indentación (espacios al principio de una línea) para definir bloques de código, lo que fomenta buenas prácticas de codificación y hace que el código sea inherentemente más organizado.

6.  **Biblioteca Estándar Robusta y Ecosistema de Librerías:**
    *   **Funcionalidades Incluidas:** Python viene con una biblioteca estándar muy completa que ofrece funcionalidades para trabajar con archivos, fechas, redes, expresiones regulares, etc., sin necesidad de instalar nada adicional.
    *   **Ecosistema Extenso:** Más allá de la biblioteca estándar, el ecosistema de paquetes de terceros (disponibles a través de `pip`) es gigantesco. Esto significa que puedes añadir funcionalidades muy avanzadas a tus programas con solo unas pocas líneas de código, permitiendo a los tediosos como llaves, puntos y comas obligatorios al final de cada línea, o la gestión de memoria.
    *   **Indentación Obligatoria:** Python utiliza la indentación (espacios al principio de una línea) para definir bloques de código, lo que fomenta buenas prácticas de codificación y hace que el código sea inherentemente más organizado.

6.  **Biblioteca Estándar Robusta y Ecosistema de Librerías:**
    *   **Funcionalidades Incluidas:** Python viene con una biblioteca estándar muy completa que ofrece funcionalidades para trabajar con archivos, fechas, redes, expresiones regulares, etc., sin necesidad de instalar nada adicional.
    *   **Ecosistema Extenso:** Más allá de la biblioteca estándar, el ecosistema de paquetes detediosos como llaves, puntos y comas obligatorios al final de cada línea, o la gestión de memoria.
    *   **Indentación Obligatoria:** Python utiliza la indentación (espacios al principio de una línea) para definir bloques de código, lo que fomenta buenas prácticas de codificación y hace que el código sea inherentemente más organizado.

6.  **Biblioteca Estándar Robusta y Ecosistema de Librerías:**
    *   **Funcionalidades Incluidas:** Python viene con una biblioteca estándar muy completa quetediosos como llaves, puntos y comas obligatorios al final de cada línea, o la gestión de memoria.
    *   **Indentación Obligatoria:** Python utiliza la indentación (espacios al principio de una línea) para definir bloques de código, lo que fomenta buenas prácticas de codificación y hace que el código sea inherentemente más organizado.

tediosos como llaves, puntos y comas obligatorios al final de cada línea, o la gestión de memoria.
    *   **Indentación Obligatoria:** Python utiliza la indentación (espacios al principio de una línea) para definir bloques de código, lo que fomenta buenas prácticas de codificación y hace qtediosos como llaves, puntos y comas obligatorios al final de cada línea, o la gestión de memoria.
    *   **Indentación Obligatoria:** Python utiliza la indentación (espacios al principio de una línea) para definir bloques de código, lo que fomenta buenas prácticas de codificación y hace que el código sea inherentemente más organizado.
 línea) para definir bloques de código, lo que fomenta buenas prácticas de codificación y hace que el código sea inherentemente más organizado.
ue el código sea inherentemente más organizado.

6.  **Biblioteca Estándar Robusta y Ecosistema de Librerías:**

6.  **Biblioteca Estándar Robusta y Ecosistema de Librerías:**
    *   **Funcionalidades Incluidas:** Python viene con una biblioteca estándar muy completa que6.  **Biblioteca Estándar Robusta y Ecosistema de Librerías:**
    *   **Funcionalidades Incluidas:** Python viene con una biblioteca estándar muy completa que ofrece funcionalidades para trabajar con archivos, fechas, redes, expresiones regulares, etc.,     *   **Funcionalidades Incluidas:** Python viene con una biblioteca estándar muy completa que ofrece funcionalidades para trabajar con archivos, fechas, redes, expresiones regulares, etc.,  ofrece funcionalidades para trabajar con archivos, fechas, redes, expresiones regulares, etc., sin necesidad de instalar nada adicional.
    *   **Ecosistema Extenso:** Más allá de la biblioteca estándar, el ecosistema de paquetes de terceros (disponibles a través de `pip`) es gigantesco. Esto significa que puedes añadir funcionalidades muy avanzadas a tus programas con solo unas pocas líneas de código, permitiendo a los principiantes crear cosas impresionantes desde el principio.

En resumen, Python es una excelente puerta de entrada al mundo de la programación porque es **accesible, potente y te ofrece un camino claro para seguir aprendiendo y aplicando tus habilidades en diversos campos**. Te permite construir una base sólida en los principios de la programación de una manera menos intimidante y más gratificante.
```

El modelo tardo aproximadamente 20 segundos en devolver una respuesta completa. Esta latencia es razonable para una consulta de este tipo, ya que implica el procesamiento de lenguaje natural y la generación de una respuesta detallada. Sin embargo, en aplicaciones en tiempo real o interactivas, una latencia menor podría ser preferible para mejorar la experiencia del usuario. 

### Prueba con generate_content_stream
Teniendo en cuenta el siguiendo código modificado para utilizar `generate_content_stream`:

```bash
response = client.models.generate_content_stream(
    model="gemini-2.5-flash",
    contents="Porque recomiendas aprender Python como primer lenguaje de programación?"
)
    for chunk in response:
    if chunk.text:
        print(chunk.text, end="", flush=True)
```
El modelo devolvio la misma respuesta pero en fragmentos (chunks) mas pequeños y con una latencia mucho menor entre cada fragmento. Esto mejora significativamente la experiencia del usuario en aplicaciones interactivas, ya que permite comenzar a ver partes de la respuesta casi de inmediato, en lugar de esperar a que se genere la respuesta completa. En este caso, la latencia entre cada fragmento fue de aproximadamente 1-2 segundos, lo que es mucho más adecuado para aplicaciones en tiempo real.

### 5. Prueba con contenido multimodal
Utilizando el siguiente código para generar contenido multimodal con una imagen:

```bash
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=[
        {
            "role": "user",
            "parts": [
                {"text": "Describe lo que ves en la imagen en español."},
                {"inline_data": {
                    "mime_type": "image/jpg",  
                    "data": open("C:/Users/IPF-2025/Desktop/google-api/galope-del-caballo.jpg", "rb").read()
                }}
            ]
        }
    ]
)

print(response.text)
```
Se le adjunto esta imagen al modelo:

![alt text](galope-del-caballo.jpg)


El modelo devolvio:

```bash
En la imagen, veo un caballo de color castaño corriendo en un campo verde lleno de flores amarillas. El caballo tiene una mancha blanca en la frente y su crin y cola son negras. Parece estar corriendo con energía y libertad. En el fondo, se puede ver una valla blanca.
```

El modelo devuelve una respuesta muy acertada y detallada sobre el contenido de la imagen. La latencia para este tipo de consulta multimodal fue de aproximadamente de 10 segundos. Lo cual es razonable considerando que el modelo tiene que procesar tanto la imagen como el texto para generar una respuesta coherente.