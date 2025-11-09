from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Добавляем раздачу статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/quick_setup", response_class=HTMLResponse)
async def quick_setup(request: Request):
    return templates.TemplateResponse("quick_setup.html", {"request": request})


@app.get("/detailed_settings", response_class=HTMLResponse)
async def detailed_settings(request: Request):
    return templates.TemplateResponse("detailed_settings.html", {"request": request})


@app.get("/windows_features", response_class=HTMLResponse)
async def windows_features(request: Request):
    return templates.TemplateResponse("windows_features.html", {"request": request})


@app.get("/routing_rules", response_class=HTMLResponse)
async def routing_rules(request: Request):
    return templates.TemplateResponse("routing_rules.html", {"request": request})


@app.get("/dns_explained", response_class=HTMLResponse)
async def dns_explained(request: Request):
    return templates.TemplateResponse("dns_explained.html", {"request": request})


# Новые разделы
@app.get("/quick_setup_windows", response_class=HTMLResponse)
async def quick_setup_windows(request: Request):
    return templates.TemplateResponse("quick_setup_windows.html", {"request": request})


@app.get("/quick_setup_android", response_class=HTMLResponse)
async def quick_setup_android(request: Request):
    return templates.TemplateResponse("quick_setup_android.html", {"request": request})


@app.get("/quick_setup_ios", response_class=HTMLResponse)
async def quick_setup_ios(request: Request):
    return templates.TemplateResponse("quick_setup_ios.html", {"request": request})