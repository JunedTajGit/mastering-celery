import os
from celery import Celery
from langchain_openai import AzureChatOpenAI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = Celery(
    "movie-info",
    broker=os.getenv("CELERY_BROKER_URL"),
    backend=os.getenv("CELERY_BACKEND_URL"),
)

llm = AzureChatOpenAI(
    api_version=os.getenv("api_version"),
    model=os.getenv("model_name"),
    azure_deployment=os.getenv("model_name"),
    temperature=0,
    max_tokens=120,
    timeout=None,
    max_retries=2,
)


class Movie(BaseModel):
    title: str
    release_year: int
    director: str
    genre: str


llm.bind(response_format=Movie)


@app.task
def movie_info(prompt: str):
    # response = llm.invoke(prompt)
    # print(response)
    movie = Movie(
        title=prompt, release_year=2010, director="Christopher Nolan", genre="Sci-Fi"
    )
    movie = Movie.model_validate_json(movie.model_dump_json(indent=2))

    return movie.model_dump()
