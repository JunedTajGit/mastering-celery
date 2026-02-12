# in real work scenario where datamodel is large sometime we need to split into mutiple models
import os
import time
import random
from pydantic import BaseModel

# chord and group are you to send and merge multiple models into single model
from celery import Celery, chord, group

app = Celery(
    "movie_multipart-info",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_BACKEND_URL"),
)


class MovieObjPartA(BaseModel):
    title: str
    release_year: int


class MovieObjPartB(BaseModel):
    director: str
    genre: str


class MovieObjPartC(BaseModel):
    actors: list[str]


@app.task
def movie_info_parta(prompt):
    movie = MovieObjPartA(title=prompt, release_year=2010)
    movie = MovieObjPartA.model_validate_json(MovieObjPartA.model_dump_json(indent=2))

    return MovieObjPartA.model_dump(movie)


@app.task
def movie_info_partb(prompt):
    movie = MovieObjPartA(director=prompt, genre="gener1")
    movie = MovieObjPartA.model_validate_json(MovieObjPartA.model_dump_json(indent=2))

    return MovieObjPartA.model_dump(movie)


@app.task
def movie_info_partc(prompt):
    movie = MovieObjPartA(actors=["prompt", "Actor2"])
    movie = MovieObjPartA.model_validate_json(MovieObjPartA.model_dump_json(indent=2))

    return MovieObjPartA.model_dump(movie)


@app.task
def combine_parts(parts):
    merged = {}

    for part in parts:
        merged.update(part)

    return merged
