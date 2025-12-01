# src/api/api.py
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from pathlib import Path

from src.logic.predictor import predict_class, resize_image, get_image_size

app = FastAPI(title="MLOps Lab1 API")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    width: int | None = Form(None),
    height: int | None = Form(None),
):
    content = await file.read()
    if not content:
        raise HTTPException(status_code=400, detail="Empty file")
    original_size = get_image_size(content)
    output_bytes = content
    if width is not None and height is not None:
        try:
            output_bytes = resize_image(content, int(width), int(height))
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Resize failed: {e}")
    predicted = predict_class(output_bytes)
    new_size = get_image_size(output_bytes)
    return JSONResponse(
        {
            "predicted_class": predicted,
            "original_size": {"width": original_size[0], "height": original_size[1]},
            "processed_size": {"width": new_size[0], "height": new_size[1]},
        }
    )

@app.get("/health")
def health():
    return {"status": "ok"}
