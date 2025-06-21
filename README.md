# 🦜🔗 Ask the Doc App

Una aplicación web interactiva que permite hacer preguntas sobre documentos de texto utilizando inteligencia artificial. La aplicación utiliza LangChain, OpenAI GPT y Streamlit para crear una experiencia de usuario intuitiva y eficiente.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [API de OpenAI](#-api-de-openai)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

## ✨ Características

- **📄 Carga de Documentos**: Sube archivos de texto (.txt) para analizar
- **🤖 IA Avanzada**: Utiliza OpenAI GPT para generar respuestas inteligentes
- **🔍 Búsqueda Semántica**: Encuentra información relevante en documentos largos
- **🌐 Interfaz Web**: Interfaz intuitiva construida con Streamlit
- **⚡ Procesamiento Rápido**: Análisis eficiente de documentos grandes
- **🔒 Seguridad**: Manejo seguro de API keys

## 🛠 Tecnologías Utilizadas

- **Streamlit**: Framework web para la interfaz de usuario
- **LangChain**: Framework para aplicaciones de IA
- **OpenAI GPT**: Modelo de lenguaje para generar respuestas
- **ChromaDB**: Base de datos vectorial para embeddings
- **Python**: Lenguaje de programación principal

## 📦 Instalación

### Prerrequisitos

- Python 3.8 o superior
- Cuenta de OpenAI con API key

### Pasos de Instalación

1. **Clona el repositorio**:

   ```bash
   git clone <url-del-repositorio>
   cd ask_the_doc_app
   ```
2. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```
3. **Configura tu API key de OpenAI** (ver sección de configuración)

## ⚙️ Configuración

### API Key de OpenAI

1. Ve a [OpenAI Platform](https://platform.openai.com/)
2. Crea una cuenta o inicia sesión
3. Genera una nueva API key
4. Guarda la key de forma segura (comienza con `sk-`)

## 🚀 Uso

### Ejecutar la Aplicación

1. **Navega al directorio del proyecto**:

   ```bash
   cd ask_the_doc_app
   ```
2. **Ejecuta la aplicación**:

   ```bash
   streamlit run app.py
   ```
3. **Abre tu navegador** en `http://localhost:8501`

### Cómo Usar la Aplicación

1. **Carga un Documento**: Haz clic en "Browse files" y selecciona un archivo .txt
2. **Escribe tu Pregunta**: En el campo de texto, escribe la pregunta sobre el documento
3. **Ingresa tu API Key**: Proporciona tu clave de API de OpenAI
4. **Genera la Respuesta**: Haz clic en "Submit" para obtener la respuesta

### Ejemplos de Preguntas

- "¿Cuál es el tema principal del documento?"
- "Resume los puntos clave"
- "¿Qué dice sobre [tema específico]?"
- "¿Cuáles son las conclusiones?"
- "¿Puedes explicar el concepto de [término]?"

## 📁 Estructura del Proyecto

```
ask_the_doc_app/
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias de Python
├── README.md             # Este archivo
└── .streamlit/           # Configuración de Streamlit
```

## 🔑 API de OpenAI

### Configuración de la API

La aplicación requiere una API key válida de OpenAI para funcionar. La key debe:

- Comenzar con `sk-`
- Tener créditos disponibles en tu cuenta
- Tener permisos para usar el modelo GPT

### Costos

- Los costos dependen del uso de la API de OpenAI
- Consulta [OpenAI Pricing](https://openai.com/pricing) para más detalles
- El procesamiento de documentos grandes puede generar costos adicionales

## 🔧 Solución de Problemas

### Errores Comunes

#### Error: "No module named 'langchain'"

```bash
pip install -r requirements.txt
```

#### Error: "Invalid API key"

- Verifica que tu API key comience con `sk-`
- Asegúrate de que la key sea válida y tenga créditos

#### Error: "Streamlit not found"

```bash
pip install streamlit
```

#### Error: "File not found"

- Asegúrate de estar en el directorio correcto
- Ejecuta `streamlit run app.py` desde `ask_the_doc_app/`

### Warnings de Deprecación

Si ves warnings sobre importaciones deprecadas de LangChain, estos son normales y no afectan la funcionalidad. La aplicación seguirá funcionando correctamente.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Mejoras Sugeridas

- [ ] Soporte para más formatos de archivo (PDF, DOCX)
- [ ] Interfaz en español
- [ ] Historial de preguntas
- [ ] Exportar respuestas
- [ ] Configuración de modelos de IA
- [ ] Análisis de múltiples documentos

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 🙏 Agradecimientos

- [LangChain](https://langchain.com/) por el framework de IA
- [OpenAI](https://openai.com/) por los modelos de lenguaje
- [Streamlit](https://streamlit.io/) por el framework web
- [ChromaDB](https://www.trychroma.com/) por la base de datos vectorial

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa la sección de [Solución de Problemas](#-solución-de-problemas)
2. Busca en los [Issues](https://github.com/tu-usuario/ask_the_doc_app/issues)
3. Crea un nuevo issue si no encuentras la solución

---

**¡Disfruta usando Ask the Doc App! 🎉**
