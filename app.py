import gradio as gr
import spaces
from PIL import Image
 
MAX_SIDE = 2048  # keeps processing fast on free CPU hardware
 
 
@spaces.GPU(duration=30)
def pixelate(img, block_size, colors):
    """Pixelate an image.
 
    block_size: size of each pixel block in source pixels (higher = chunkier).
    colors: number of palette colors (0 keeps the original colors).
    """
    if img is None:
        return None
 
    img = img.convert("RGB")
 
    # Downscale very large uploads so the Space stays responsive
    if max(img.size) > MAX_SIDE:
        img.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
 
    w, h = img.size
    block_size = max(1, int(block_size))
    small_w = max(1, w // block_size)
    small_h = max(1, h // block_size)
 
    # Shrink (averaging each block), optionally reduce colors, then scale back up
    small = img.resize((small_w, small_h), Image.BOX)
 
    colors = max(0, min(256, int(colors)))
    if colors > 0:
        small = small.quantize(colors=colors, method=Image.Quantize.MEDIANCUT).convert("RGB")
 
    return small.resize((w, h), Image.NEAREST)
 
 
CSS = """
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

:root {
    --pixel-purple: #000000;
    --pixel-pink: #2b2b2b;
    --pixel-ink: #171322;
}
.gradio-container {
    max-width: none !important;
    min-height: 100vh;
    padding: 0 !important;
    background:
        radial-gradient(circle at 8% 8%, rgba(0, 0, 0, 0.12), transparent 28rem),
        radial-gradient(circle at 92% 18%, rgba(0, 0, 0, 0.08), transparent 24rem),
        #faf9ff;
    font-family: "DM Sans", sans-serif;
}
.gradio-container h1,
.gradio-container h2,
.gradio-container h3 {
    font-family: "Space Grotesk", sans-serif;
}
.app-shell {
    max-width: 1180px;
    min-height: 100vh;
    padding: 38px 24px 24px;
    margin: 0 auto;
}
.hero {
    position: relative;
    overflow: hidden;
    padding: 42px 44px;
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 28px;
    background:
        radial-gradient(circle at 90% 15%, rgba(255, 255, 255, 0.14), transparent 13rem),
        linear-gradient(120deg, #000000 0%, #111111 55%, #292929 100%);
    box-shadow: 0 24px 70px rgba(49, 24, 91, 0.22);
    color: white;
    margin-bottom: 24px;
}
.hero::after {
    position: absolute;
    right: -40px;
    bottom: -90px;
    width: 240px;
    height: 240px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 34px;
    transform: rotate(28deg);
    content: "";
}
.hero-content {
    position: relative;
    z-index: 1;
    max-width: 650px;
}
.eyebrow {
    display: inline-block;
    margin-bottom: 16px;
    padding: 6px 11px;
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 99px;
    background: rgba(255, 255, 255, 0.18);
    color: #ffffff !important;
    opacity: 1 !important;
    font-size: 0.85rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
    text-transform: uppercase;
}
.hero h1 {
    margin: 0 0 8px;
    color: #ffffff !important;
    opacity: 1 !important;
    font-size: clamp(2.2rem, 5vw, 4rem);
    letter-spacing: -0.06em;
}
.hero p {
    margin: 0;
    color: #ffffff !important;
    opacity: 1 !important;
    font-size: 1.15rem;
    font-weight: 500;
    line-height: 1.6;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.75);
}
.panel {
    border: 1px solid rgba(0, 0, 0, 0.14);
    border-radius: 22px;
    padding: 22px;
    background: rgba(255, 255, 255, 0.78);
    box-shadow: 0 14px 40px rgba(51, 35, 92, 0.08);
    backdrop-filter: blur(12px);
}
.panel h3 {
    margin-top: 0;
    color: var(--pixel-ink);
}
.panel .label-wrap,
.result-panel .label-wrap {
    display: inline-flex !important;
    margin-bottom: 10px;
    padding: 6px 11px;
    border-radius: 99px;
    background: #000000 !important;
    color: #ffffff !important;
    font-weight: 700;
}
.panel .label-wrap *,
.result-panel .label-wrap * {
    color: #ffffff !important;
    opacity: 1 !important;
}
.result-panel {
    margin-top: 24px;
    padding: 22px;
    border: 1px solid rgba(0, 0, 0, 0.14);
    border-radius: 22px;
    background: rgba(255, 255, 255, 0.82);
    box-shadow: 0 14px 40px rgba(51, 35, 92, 0.08);
}
.section-label {
    margin: 0 0 12px;
    color: #111111;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
}
.drop-zone {
    border-radius: 16px !important;
}
.drop-zone .upload-text,
.drop-zone .upload-text *,
.drop-zone button,
.drop-zone button * {
    color: #000000 !important;
    opacity: 1 !important;
}
.action-row {
    margin-top: 12px;
}
.primary-action {
    border: 0 !important;
    border-radius: 12px !important;
    background: linear-gradient(100deg, var(--pixel-purple), var(--pixel-pink)) !important;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.24);
}
.reset-action {
    border-radius: 12px !important;
}
.footer {
    padding: 24px 0 0;
    color: #716b80;
    text-align: center;
    font-size: 0.86rem;
}
.tip {
    color: var(--body-text-color-subdued);
    font-size: 0.9rem;
    line-height: 1.5;
}
@media (max-width: 700px) {
    .app-shell {
        padding: 18px 12px;
    }
    .hero {
        padding: 30px 24px;
        border-radius: 22px;
    }
    .panel,
    .result-panel {
        padding: 16px;
        border-radius: 18px;
    }
}
"""

with gr.Blocks(
    title="Bangu - Image Pixelator",
) as demo:
    with gr.Column(elem_classes="app-shell"):
        gr.HTML(
            """
            <section class="hero">
                <div class="hero-content">
                    <span class="eyebrow">Image remix studio</span>
                    <h1>Bangu</h1>
                    <p>Turn any image into beautiful pixel art in seconds.
                    Tune the detail, choose your palette, and make it yours.</p>
                </div>
            </section>
            """
        )

        with gr.Row(equal_height=False):
            with gr.Column(scale=1, elem_classes="panel"):
                gr.HTML('<p class="section-label">01 / Start here</p>')
                gr.Markdown("### Choose an image")
                inp = gr.Image(
                    type="pil",
                    label="Source image",
                    sources=["upload", "clipboard", "webcam"],
                    height=350,
                    elem_classes="drop-zone",
                )
                gr.Markdown(
                    '<p class="tip">Upload, paste, or take a photo. '
                    "Your image is processed locally and is not stored.</p>"
                )

            with gr.Column(scale=1, elem_classes="panel"):
                gr.HTML('<p class="section-label">02 / Make it yours</p>')
                gr.Markdown("### Adjust the effect")
                block = gr.Slider(
                    minimum=2,
                    maximum=128,
                    value=16,
                    step=1,
                    label="Pixel size",
                    info="Small values keep more detail; large values create chunky pixels.",
                )
                colors = gr.Slider(
                    minimum=0,
                    maximum=64,
                    value=0,
                    step=1,
                    label="Color palette",
                    info="0 keeps the original colors. Lower values create a retro look.",
                )
                with gr.Row(elem_classes="action-row"):
                    btn = gr.Button(
                        " Pixelate image",
                        variant="primary",
                        elem_classes="primary-action",
                        scale=2,
                    )
                    clear_btn = gr.Button(
                        "Reset",
                        elem_classes="reset-action",
                        scale=1,
                    )

        with gr.Column(elem_classes="result-panel"):
            gr.HTML('<p class="section-label">03 / Your creation</p>')
            gr.Markdown("### Pixelated result")
            out = gr.Image(
                type="pil",
                label="Result",
                format="png",
                interactive=False,
                height=500,
            )
        gr.HTML('<p class="footer">Bangu &middot; Image Pixelator</p>')
 
    # Live preview as the user moves the sliders or uploads a new image
    for component in (inp, block, colors):
        component.change(pixelate, [inp, block, colors], out, show_progress="hidden")
    btn.click(pixelate, [inp, block, colors], out)
    clear_btn.click(
        lambda: (None, 16, 0, None),
        outputs=[inp, block, colors, out],
        show_progress="hidden",
    )
 
if __name__ == "__main__":
    demo.launch(
        theme=gr.themes.Soft(
            primary_hue="violet",
            secondary_hue="purple",
            neutral_hue="slate",
        ),
        css=CSS,
    )