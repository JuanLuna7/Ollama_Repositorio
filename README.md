# Chat Local con LLM — Ollama + Python + Tkinter

## Descripción

Aplicación de escritorio que permite chatear con un modelo de lenguaje local (gemma2:2b) usando Ollama.

## Requisitos

- Python 3.10+
- 4 GB RAM mínimo
- Ollama instalado

## Prerrequisitos

Instalar Ollama:
https://ollama.com/download

Descargar modelo:

ollama pull gemma2:2b

## Instalación

git clone https://github.com/TU_USUARIO/mi-chat-llm.git
cd mi-chat-llm

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

## Uso

Asegúrate de que Ollama esté corriendo:

ollama serve

Ejecuta la app:

python main.py

## Modelo usado

- gemma2:2b

## Conclusión

Permite ejecutar IA local sin internet, con buena velocidad y privacidad.

## Autor

Tu nombre