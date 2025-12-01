import gradio as gr
import httpx
from io import BytesIO

# URL to your backend, adjust if deployed
RENDER_URL = "https://lab1-api-latest.onrender.com"
#RENDER_URL = "http://127.0.0.1:8000"

def predict(image):
    if image is None:
        return "No image uploaded."

    try:
        buf = BytesIO()
        image.save(buf, format="PNG")
        buf.seek(0)

        with httpx.Client(timeout=20) as client:
            files = {"file": ("image.png", buf, "image/png")}
            r = client.post(f"{RENDER_URL}/predict", files=files)
            r.raise_for_status()

        return r.json().get("prediction", "Malformed response from API")
    except Exception as e:
        return f"Error: {e}"

demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Textbox(label="Predicted Class"),
    title="Image Classifier (Lab1)",
    description="Uploads an image and queries the FastAPI API backend.",
)

if __name__ == "__main__":
    demo.launch()
