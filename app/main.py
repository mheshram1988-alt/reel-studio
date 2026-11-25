from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
from PIL import Image, ImageEnhance
import io

app = FastAPI(title="CHROMA AI")

@app.get("/health")
def health():
    return {"status": "ok", "project": "CHROMA AI"}

@app.post("/v1/process")
async def process_photo(photo: UploadFile = File(...)):
    name = (photo.filename or "").lower()

    if not name.endswith((".jpg", ".jpeg", ".png")):
        raise HTTPException(415, "Only JPG and PNG supported")

    data = await photo.read()

    if len(data) > 15 * 1024 * 1024:
        raise HTTPException(413, "Image too large")

    try:
        image = Image.open(io.BytesIO(data)).convert("RGB")
    except Exception:
        raise HTTPException(400, "Invalid image")

    image = ImageEnhance.Color(image).enhance(1.08)
    image = ImageEnhance.Contrast(image).enhance(1.04)
    image = ImageEnhance.Brightness(image).enhance(1.02)

    output = io.BytesIO()
    image.save(output, format="JPEG", quality=94)

    return Response(
        output.getvalue(),
        media_type="image/jpeg"
    )
  
