import assemblyai as aai
import os

# Configuración de la clave API de AssemblyAI
aai.settings.api_key = "60046ec2429d4502a1b433c5db148f96"  # Reemplaza con tu clave API

# Ruta del video o archivo de audio
#video_path = r"C:\Users\hvasq\OneDrive\Negocios\FACInnova\Clientes\Odoo\TrimCav\Visita-23-9-24\Almacen cauchos.mp4"
video_path = r"C:\Users\hvasq\OneDrive\Negocios\FACInnova\Clientes\El Representante\RubenDiana_PrimeraReunion.mp4"


#speakers_expected=2,
config = aai.TranscriptionConfig(language_code="es", speaker_labels=True, punctuate=True, format_text=True, iab_categories=True)

# Crear instancia del transcriptor
transcriber = aai.Transcriber()

# Hacer la transcripción directamente desde el archivo local
try:
    transcript = transcriber.transcribe(video_path, config=config)

    # Guardar la transcripción en un archivo de texto
    output_path = os.path.join(os.path.dirname(video_path), "Almacen cauchos.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        # Escribir el texto transcrito
        f.write("Transcripción:\n")
        f.write(transcript.text + "\n\n")
        
        # Escribir información de cada parlante
        f.write("Diálogo por parlante:\n")
        for utterance in transcript.utterances:
            f.write(f"Speaker {utterance.speaker}: {utterance.text}\n")

        # Escribir información de temas detectados
        f.write("\nTemas detectados:\n")
        for result in transcript.iab_categories.results:
            f.write(f"{result.text}\n")
            f.write(f"Timestamp: {result.timestamp.start} - {result.timestamp.end}\n")
            for label in result.labels:
                f.write(f" - {label.label} ({label.relevance})\n")

        # Escribir resumen de todos los temas
        f.write("\nResumen de temas:\n")
        for topic, relevance in transcript.iab_categories.summary.items():
            f.write(f"Audio es {relevance * 100:.2f}% relevante a {topic}\n")

    print(f"Transcripción guardada en: {output_path}")

except Exception as e:
    print("Error al transcribir:", e)
