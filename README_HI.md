# CHROMA AI — Backend Starter (v0.1)

यह शुरुआती परीक्षण backend है। इसे FastAPI पर बनाया गया है।

## अभी क्या काम करता है
- `/health` से server status जाँचना
- `/v1/process` पर JPG/PNG upload करना
- एक साधारण baseline enhancement के साथ JPG या PNG output पाना

## महत्वपूर्ण सीमाएँ
- यह संस्करण अभी वास्तविक AI semantic masking नहीं करता।
- यह संस्करण RAW files को decode/process नहीं करता।
- इसमें केवल शुरुआती global enhancement है; इसे professional colour-grading engine न समझें।
- RAW support, AI subject/sky/skin masks, local adjustments, सुरक्षित cloud storage और production deployment आगे के चरण हैं।

## स्थानीय रूप से चलाना
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

फिर `/docs` खोलकर API test करें।

## API
- `GET /health`
- `POST /v1/process?output_format=jpg` — multipart field का नाम `photo` रखें।

अभी केवल JPG और PNG स्वीकार हैं। अधिकतम upload size 15 MB है।
