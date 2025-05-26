from ultralytics import YOLO
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

model = YOLO("yolov8s.pt")
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def form(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/upload", response_class=HTMLResponse)
def upload(request: Request, file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        raise HTTPException(status_code=500, detail='Something went wrong')
    finally:
        file.file.close()
        
    results = model(file.filename, show=False)
    oggetti_trovati = results[0].boxes.cls.tolist()
    classe = results[0].names
    output = ""
    
    for id in set(oggetti_trovati):
        output += classe[id].capitalize() + ": " + str(oggetti_trovati.count(id)) + " | "
    
    return templates.TemplateResponse(request=request, name="upload.html", context={"oggetto": output})
    