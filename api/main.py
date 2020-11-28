from fastapi import FastAPI
from typing import Optional
from api.etc import grabber, imiggger
from api.utils import verifier

app = FastAPI()


@app.get("/")
async def index():
    return "MAGNA - Simple Manhwa, Manhua and Manga Scraper and Linker"


# Main Manga, Manhwa, Manhua Chapters Links
@app.get("/manga")
async def manga(q: Optional[str] = None):
    if verifier(q, "manga"):
        return await grabber(q)

    return "Get the Chapters of the Manga"


@app.get("/manga/chapters")
async def chapters(q: Optional[str] = None):
    if verifier(q, "chapter"):
        return await imiggger(q)

    return "Get the Images from the Manga Chapter page"