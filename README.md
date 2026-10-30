<div align="center">

<img src="logo.png" alt="Bangu logo" width="180">

# Bangu — Image Pixelator

### Turn any image into beautiful pixel art in seconds.

<p>
  <a href="https://huggingface.co/spaces/skelon/BanguImagePixelator">
    <img src="https://img.shields.io/badge/%E2%96%B6%20Try%20Bangu%20Live-FF4B4B?style=for-the-badge&logo=huggingface&logoColor=white" alt="Try Bangu live">
  </a>
  <a href="#-quick-start">
    <img src="https://img.shields.io/badge/Run%20Locally-111111?style=for-the-badge&logo=python&logoColor=white" alt="Run locally">
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.9+">
  <img src="https://img.shields.io/badge/Gradio-UI-FF7C00?style=flat-square&logo=gradio&logoColor=white" alt="Gradio">
  <img src="https://img.shields.io/badge/Pillow-Image%20Processing-306998?style=flat-square" alt="Pillow">
  <img src="https://img.shields.io/badge/Status-Ready%20to%20pixelate-2EA44F?style=flat-square" alt="Ready to pixelate">
</p>

<p><i>Upload. Tune. Pixelate. Share.</i></p>

</div>

---

## What is Bangu?

**Bangu** is a lightweight image-pixelation studio built with Python, Gradio, and Pillow. It transforms ordinary photos into crisp, retro-inspired pixel art with a responsive live preview.

No design software. No complicated workflow. Just a few controls and a great-looking result.

> ** Try it yourself:** [Open Bangu on Hugging Face Spaces →](https://huggingface.co/spaces/skelon/BanguImagePixelator)

##  Features

| Feature | Why it is useful |
| --- | --- |
|  **Upload, paste, or capture** | Start with a file, clipboard image, or webcam snapshot. |
|  **Live preview** | See every slider change immediately. |
|  **Pixel size control** | Choose detailed pixels or bold, chunky blocks. |
|  **Palette reduction** | Keep original colors or create a limited retro palette. |
|  **Fast processing** | Smart resizing keeps large images responsive. |
|  **Privacy-friendly** | The app processes images without storing them. |
|  **One-click reset** | Quickly return to a clean starting state. |

##  How to use

1. **Choose an image** — upload, paste, or use your webcam.
2. **Set the pixel size** — smaller values preserve more detail; larger values feel more 8-bit.
3. **Choose the color palette** — set it to `0` for original colors, or lower it for a retro look.
4. **Preview and refine** — Bangu updates the result as you adjust the controls.
5. **Save your creation** — download the generated PNG from the result panel.

### Keyboard-friendly workflow

```text
[ Upload / Paste / Webcam ]  →  [ Tune ]  →  [ Preview ]  →  [ Download ]
```

| Control | Range | Default | Effect |
| --- | ---: | ---: | --- |
| `Pixel size` | `2–128` | `16` | Controls the size of each pixel block. |
| `Color palette` | `0–64` | `0` | Controls the number of colors used. |

## Quick start

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows**

```powershell
.venv\Scripts\activate
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Bangu

```bash
python app.py
```

Then open the local Gradio URL shown in your terminal.

## How the pixelation works

1. Convert the image to RGB.
2. Downscale it with box filtering to average each pixel block.
3. Optionally quantize the image to a smaller color palette.
4. Scale it back up with nearest-neighbor interpolation for sharp pixel edges.

Large images are capped at a maximum side length so the interface stays fast on free CPU hardware.

## Project structure

```text
.
├── app.py           # Gradio interface and pixelation pipeline
├── logo.png         # Bangu branding
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

## Built with

- [Python](https://www.python.org/)
- [Gradio](https://www.gradio.app/)
- [Pillow](https://python-pillow.org/)
- [Hugging Face Spaces](https://huggingface.co/spaces)

## Make it viral

Made something cool? Share your result and tag the project:

```text
#Bangu #PixelArt #ImagePixelator #Python #Gradio #HuggingFace
```

If Bangu helped you make something fun, leave a ⭐ and share the live demo:

**[▶ Try Bangu now](https://huggingface.co/spaces/skelon/BanguImagePixelator)**

##  Contributing

Ideas, improvements, and bug reports are welcome. Open an issue or submit a pull request with a clear description of the change and a reproducible example when relevant.

---

<div align="center">

**Bangu · Image Pixelator**

<a href="https://huggingface.co/spaces/skelon/BanguImagePixelator">Try it live</a> ·
<a href="#-quick-start">Run locally</a> ·
<a href="#-contributing">Contribute</a>

</div>
