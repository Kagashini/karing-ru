from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from datetime import datetime
import subprocess

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Добавляем раздачу статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Централизованный список навигационных ссылок с описаниями
navigation_links = [
    {"path": "/quick_setup_windows", "title": "Karing - Быстрая настройка Windows", "description": "Пошаговая инструкция по настройке Karing на Windows"},
    {"path": "/quick_setup_android", "title": "Karing - Быстрая настройка Android", "description": "Пошаговая инструкция по настройке Karing на Android"},
    {"path": "/quick_setup_ios", "title": "Karing - Быстрая настройка iOS", "description": "Пошаговая инструкция по настройке Karing на iOS"},
    {"path": "/detailed_settings", "title": "Подробнее о настройках", "description": "Расширенные настройки и возможности программы"},
    {"path": "/windows_features", "title": "Особенности Karing в Windows", "description": "Специфические настройки для операционной системы Windows"},
    {"path": "/routing_rules", "title": "Karing - маршрутизация и правила", "description": "Настройка правил маршрутизации трафика"},
    {"path": "/dns_explained", "title": "Karing - что такое DNS и как с ним бороться", "description": "Настройка и оптимизация DNS-серверов"},
]

def get_last_commit_date():
    try:
        # Выполняем команду git для получения даты последнего коммита
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%cd', '--date=format:%d.%m.%Y'],
            capture_output=True,
            text=True,
            check=True
        )
        # Возвращаем дату, убирая лишние пробелы и символы новой строки
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        # В случае ошибки возвращаем None или значение по умолчанию
        return "N/A"

def get_template_context(request: Request):
    return {
        "request": request,
        "nav_links": navigation_links,
        "current_year": datetime.now().year,
        "last_updated": get_last_commit_date()
    }

@app.get('static/images/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("static/images/favicon.ico")

@app.get("/{page_name}", response_class=HTMLResponse)
async def show_page(request: Request, page_name: str):
    template_path = f"{page_name}.html"
    
    # Проверка существования файла шаблона
    if not os.path.exists(os.path.join("templates", template_path)):
        raise HTTPException(status_code=404, detail="Page not found")
        
    context = get_template_context(request)
    return templates.TemplateResponse(template_path, context)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("index.html", context)