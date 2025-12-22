import subprocess
from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Добавляем раздачу статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Централизованный список навигационных ссылок с описаниями
navigation_links = [
    {
        "path": "/quick_setup_windows",
        "title": "Karing - Быстрая настройка Windows",
        "description": "Пошаговая инструкция по настройке Karing на Windows",
    },
    {
        "path": "/quick_setup_android",
        "title": "Karing - Быстрая настройка Android",
        "description": "Пошаговая инструкция по настройке Karing на Android",
    },
    {
        "path": "/quick_setup_ios",
        "title": "Karing - Быстрая настройка iOS",
        "description": "Пошаговая инструкция по настройке Karing на iOS",
    },
    {
        "path": "/windows_features",
        "title": "Особенности Karing в Windows",
        "description": "Специфические настройки для операционной системы Windows",
    },
    {
        "path": "/detailed_settings",
        "title": "Подробнее о настройках",
        "description": "Расширенные настройки и возможности программы",
    },
    {
        "path": "/routing_rules",
        "title": "Karing - маршрутизация и правила",
        "description": "Настройка правил маршрутизации трафика",
    },
    {
        "path": "/dns_explained",
        "title": "Karing - что такое DNS и как с ним бороться",
        "description": "Настройка и оптимизация DNS-серверов",
    },
    {
        "path": "/faq",
        "title": "Часто задаваемые вопросы",
        "description": "Часто задаваемые вопросы о Karing и решения проблем",
    },
]


def get_last_commit_date():
    try:
        # Выполняем команду git для получения даты последнего коммита
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cd", "--date=format:%d.%m.%Y"],
            capture_output=True,
            text=True,
            check=True,
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
        "last_updated": get_last_commit_date(),
    }


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/images/favicon.ico")


# Individual routes for each page to ensure FastAPI works correctly
# Routes without .html extension (for direct access)
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("index.html", context)


@app.get("/quick_setup_windows", response_class=HTMLResponse)
async def quick_setup_windows(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("quick_setup_windows.html", context)


@app.get("/quick_setup_android", response_class=HTMLResponse)
async def quick_setup_android(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("quick_setup_android.html", context)


@app.get("/quick_setup_ios", response_class=HTMLResponse)
async def quick_setup_ios(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("quick_setup_ios.html", context)


@app.get("/detailed_settings", response_class=HTMLResponse)
async def detailed_settings(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("detailed_settings.html", context)


@app.get("/windows_features", response_class=HTMLResponse)
async def windows_features(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("windows_features.html", context)


@app.get("/routing_rules", response_class=HTMLResponse)
async def routing_rules(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("routing_rules.html", context)


@app.get("/dns_explained", response_class=HTMLResponse)
async def dns_explained(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("dns_explained.html", context)


# Routes with .html extension (for compatibility with static site links)
@app.get("/index.html", response_class=HTMLResponse)
async def index_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("index.html", context)


@app.get("/quick_setup_windows.html", response_class=HTMLResponse)
async def quick_setup_windows_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("quick_setup_windows.html", context)


@app.get("/quick_setup_android.html", response_class=HTMLResponse)
async def quick_setup_android_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("quick_setup_android.html", context)


@app.get("/quick_setup_ios.html", response_class=HTMLResponse)
async def quick_setup_ios_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("quick_setup_ios.html", context)


@app.get("/windows_features.html", response_class=HTMLResponse)
async def windows_features_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("windows_features.html", context)


@app.get("/detailed_settings.html", response_class=HTMLResponse)
async def detailed_settings_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("detailed_settings.html", context)


@app.get("/routing_rules.html", response_class=HTMLResponse)
async def routing_rules_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("routing_rules.html", context)


@app.get("/dns_explained.html", response_class=HTMLResponse)
async def dns_explained_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("dns_explained.html", context)


@app.get("/faq", response_class=HTMLResponse)
async def faq(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("faq.html", context)


@app.get("/faq.html", response_class=HTMLResponse)
async def faq_html(request: Request):
    context = get_template_context(request)
    return templates.TemplateResponse("faq.html", context)
