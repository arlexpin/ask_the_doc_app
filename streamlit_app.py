import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import streamlit as st
from langchain_community.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
import os

# Page configuration
st.set_page_config(
    page_title='🦜🔗 Ask the Doc App - Enhanced',
    page_icon='📚',
    layout='centered',
    initial_sidebar_state='expanded'
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2c3e50;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #3498db;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
    .upload-section {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #dee2e6;
        margin: 1rem 0;
    }
    .query-section {
        background-color: #e8f4fd;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #bee5eb;
        margin: 1rem 0;
    }
    .response-section {
        background-color: #f0f8f0;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def generate_response(uploaded_files, openai_api_key, query_text, chunk_size=1000, chunk_overlap=200, temperature=0.3):
    """Generate response using LangChain and OpenAI"""
    try:
        # Load documents if files are uploaded
        if uploaded_files is not None:
            documents = []
            for uploaded_file in uploaded_files:
                content = uploaded_file.read().decode()
                documents.append(content)
            
            # Combine all documents
            combined_text = "\n\n".join(documents)
            
            # Split documents into chunks
            text_splitter = CharacterTextSplitter(
                chunk_size=chunk_size, 
                chunk_overlap=chunk_overlap,
                separator="\n"
            )
            texts = text_splitter.create_documents([combined_text])
            
            # Select embeddings
            embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
            
            # Create a vectorstore from documents
            db = Chroma.from_documents(texts, embeddings)
            
            # Create retriever interface
            retriever = db.as_retriever(search_kwargs={"k": 3})
            
            # Create QA chain
            qa = RetrievalQA.from_chain_type(
                llm=OpenAI(openai_api_key=openai_api_key, temperature=temperature),
                chain_type='stuff', 
                retriever=retriever
            )
            
            return qa.run(query_text)
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Header
    st.markdown('<h1 class="main-header">🦜🔗 Ask the Doc App</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Configuración")
        
        # API Key input
        openai_api_key = st.text_input(
            'OpenAI API Key', 
            type='password',
            help="Ingresa tu API key de OpenAI (comienza con 'sk-')"
        )
        
        # Model settings
        st.subheader("⚙️ Configuración del Modelo")
        chunk_size = st.slider("Tamaño de chunk", 500, 2000, 1000, 100)
        chunk_overlap = st.slider("Solapamiento de chunks", 0, 500, 200, 50)
        temperature = st.slider("Temperatura", 0.0, 1.0, 0.3, 0.1)
        
        # Information
        st.markdown("---")
        st.markdown("### 📖 Cómo usar")
        st.markdown("""
        1. Sube uno o más archivos de texto (.txt)
        2. Escribe tu pregunta
        3. Ingresa tu API key de OpenAI
        4. Haz clic en 'Generar Respuesta'
        """)
        
        st.markdown("### 💡 Ejemplos de preguntas")
        st.markdown("""
        - "¿Cuál es el tema principal del documento?"
        - "Resume los puntos clave"
        - "¿Qué dice sobre [tema específico]?"
        - "¿Cuáles son las conclusiones?"
        """)
    
    # Main content - Vertical Layout
    
    # Section 1: File Upload
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">📄 Cargar Documentos</h2>', unsafe_allow_html=True)
    
    # File upload
    uploaded_files = st.file_uploader(
        'Selecciona archivos de texto', 
        type=['txt'], 
        accept_multiple_files=True,
        help="Puedes subir múltiples archivos de texto"
    )
    
    if uploaded_files:
        st.success(f"✅ {len(uploaded_files)} archivo(s) cargado(s) exitosamente")
        
        # Show file previews
        with st.expander("📖 Vista previa de documentos"):
            for i, file in enumerate(uploaded_files):
                st.subheader(f"Archivo {i+1}: {file.name}")
                content = file.read().decode()
                st.text_area(f"Contenido de {file.name}", content[:500] + "..." if len(content) > 500 else content, height=150)
                file.seek(0)  # Reset file pointer
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Section 2: Query Input
    st.markdown('<div class="query-section">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-header">❓ Tu Pregunta</h2>', unsafe_allow_html=True)
    
    # Query input
    query_text = st.text_area(
        'Escribe tu pregunta aquí:',
        placeholder='Ej: ¿Cuál es el tema principal del documento?',
        height=120,
        disabled=not uploaded_files
    )
    
    # Generate button
    if st.button('🚀 Generar Respuesta', 
                 disabled=not (uploaded_files and query_text and openai_api_key),
                 use_container_width=True):
        if not openai_api_key.startswith('sk-'):
            st.error("❌ Por favor ingresa una API key válida de OpenAI")
        else:
            with st.spinner('🤖 Procesando tu pregunta...'):
                response = generate_response(
                    uploaded_files, 
                    openai_api_key, 
                    query_text,
                    chunk_size,
                    chunk_overlap,
                    temperature
                )
                
                # Section 3: Response Display
                st.markdown('<div class="response-section">', unsafe_allow_html=True)
                st.markdown('<h2 class="section-header">📝 Respuesta</h2>', unsafe_allow_html=True)
                st.markdown('<div class="success-box">', unsafe_allow_html=True)
                st.write(response)
                st.markdown('</div>', unsafe_allow_html=True)
                
                # Add copy button
                st.code(response, language=None)
                st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="info-box">
    <strong>ℹ️ Información:</strong> Esta aplicación utiliza LangChain, OpenAI GPT y ChromaDB para procesar documentos 
    y responder preguntas basándose en el contenido de los archivos cargados.
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
