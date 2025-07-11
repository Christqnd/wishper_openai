import os
import sys
import whisper
import ffmpeg
import tempfile
from pathlib import Path

def extract_audio(video_path, output_dir):
    audio_path = os.path.join(output_dir, Path(video_path).stem + ".wav")
    (
        ffmpeg
        .input(video_path)
        .output(audio_path, ac=1, ar='16000')  # mono, 16kHz
        .run(quiet=True, overwrite_output=True)
    )
    return audio_path

def transcribe_file(model, video_path):
    with tempfile.TemporaryDirectory() as tmpdir:
        audio_path = extract_audio(video_path, tmpdir)
        print(f"🗣️  Transcribiendo: {video_path}")
        result = model.transcribe(audio_path)
        print(f"✅ Transcripción completada: {video_path}\n")
        return result['text']

def process_path(path):
    model = whisper.load_model("base")  # Usa "small", "medium", o "large" si tienes buena GPU

    if os.path.isfile(path) and path.endswith(".mp4"):
        text = transcribe_file(model, path)
        output_file = Path(path).with_suffix('.txt')
        output_file.write_text(text, encoding="utf-8")
        print(f"📝 Transcripción guardada en: {output_file}")

    elif os.path.isdir(path):
        mp4_files = sorted(Path(path).glob("*.mp4"))
        if not mp4_files:
            print("⚠️ No se encontraron archivos .mp4 en el directorio.")
            return

        for video in mp4_files:
            text = transcribe_file(model, str(video))
            output_file = video.with_suffix('.txt')
            output_file.write_text(text, encoding="utf-8")
            print(f"📝 Transcripción guardada en: {output_file}")
    else:
        print("❌ Ruta inválida. Debe ser un archivo .mp4 o un directorio.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python openai_app.py <archivo.mp4 | carpeta>")
        sys.exit(1)

    input_path = sys.argv[1]
    process_path(input_path)
