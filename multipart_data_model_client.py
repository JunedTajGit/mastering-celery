import time
from celery import group, chord

from multipart_data_model_worker import (
    movie_info_parta,
    movie_info_partb,
    movie_info_partc,
    combine_parts,
)


prompt = "Tell me about movie inception"

# sponing parallel task
header = group(
    movie_info_parta.s("promptA"),
    movie_info_partb.s("promptB"),
    movie_info_partc.s("promptC"),
)

result = chord(header)(combine_parts.s())

combined = result.get()

print(combined)
