import gradio as gr
import httpx
from io import BytesIO

# Replace this with your deployed Render URL:
# Example: "https://your-render-service.onrender.com"
RENDER_URL = "https://lab1-api-latest.onrender.com"


def predict(image):
    """
    Sends an uploaded image to the FastAPI backend deployed on Render.
    """
    if image is None:
        return "No image uploaded."

    try:
        # Convert PIL image to bytes
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
    title="Image Classifier (MLOps Lab 2)",
    description="Uploads an image and queries the FastAPI API deployed on Render.",
)

if __name__ == "__main__":
    demo.launch()
