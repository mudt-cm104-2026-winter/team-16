"""Car Ratings: users rate cars from 1 to 10, the app shows the ratings.


"""

from pathlib import Path

from fastapi import FastAPI, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import storage

HERE = Path(__file__).parent

app = FastAPI(title="Car Ratings")
app.mount("/static", StaticFiles(directory=HERE / "static"), name="static")
templates = Jinja2Templates(directory=HERE / "templates")


@app.get("/")
def show_list(request: Request):
    """The start page: the form and all entries."""
    return templates.TemplateResponse(
        request, "index.html", {"entries": storage.all_entries()}
    )


@app.post("/add")
def add(car: str = Form(...), rating: int = Form(..., ge=1, le=10)):
    """The form on the start page sends its fields here."""
    storage.add_entry(car=car.strip(), rating=rating)
    # Back to the start page. 303 tells the browser: load it with GET.
    return RedirectResponse("/", status_code=303)
