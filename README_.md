# 🎙️ OpenAI Whisper Video Transcriber

Este script transcribe automáticamente el audio hablado en archivos `.mp4` utilizando **OpenAI Whisper localmente**. Funciona tanto con un archivo individual como con una carpeta que contenga múltiples videos.

## 🚀 Características

- Transcripción automática de videos `.mp4`.
- Compatible con carpetas o archivos individuales.
- No requiere conexión a internet (usa modelos locales).
- Guarda la transcripción como un archivo `.txt` con el mismo nombre del video.

---

## 🛠️ Requisitos

### Python >= 3.8

### Dependencias

Instálalas ejecutando:

```bash
pip install openai-whisper ffmpeg-python
```

### Sistema

#### Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install ffmpeg
```

#### Windows:

- Descarga `ffmpeg` desde: https://ffmpeg.org/download.html
- Agrega `ffmpeg/bin` al **PATH** del sistema.

---

## 📦 Instalación del script

Guarda el archivo como:

```bash
openai_app.py
```

---

## ▶️ Uso

### 🔹 Transcribir un solo archivo `.mp4`

#### Linux/macOS:

```bash
python3 openai_app.py "/ruta/a/mi_video.mp4"
```

#### Windows:

```cmd
python openai_app.py "C:\Ruta\A\mi_video.mp4"
```

---

### 🔹 Transcribir todos los videos en una carpeta

#### Linux/macOS:

```bash
python3 openai_app.py "/ruta/a/mis_videos/"
```

#### Windows:

```cmd
python openai_app.py "C:\Ruta\A\mis_videos"
```

---

## 📝 Salida

Por cada archivo `.mp4` procesado, se genera un archivo `.txt` en la misma ubicación:

```
mi_video.mp4   ➜   mi_video.txt
```

---

## 🧠 Modelos disponibles

El script usa por defecto el modelo `base`. Puedes cambiarlo a:

- `tiny`
- `base` ✅
- `small`
- `medium`
- `large`

Modifica esta línea en el script si deseas usar otro modelo:

```python
model = whisper.load_model("base")
```

---

## 📌 Notas adicionales

- Si usas CPU, se recomienda `tiny` o `base` por rendimiento.
- En GPU, puedes usar `medium` o `large` para mayor precisión.

---

## 📄 Licencia

MIT License. Script basado en la librería oficial [OpenAI Whisper](https://github.com/openai/whisper).
