from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from constants import crafting_table, starting_elements

fs = frozenset

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CraftMessageBody(BaseModel):
    item1: str
    item2: str


@app.post("/api/combine")
async def combine(body: CraftMessageBody):
    """
    Return the result of crafting two items together
    """
    pair = fs((body.item1, body.item2))
    if pair not in crafting_table:
        return {"message": "crafted nothing", "element": None}
    else:
        result = crafting_table[pair]
        return {
            "message": "new element created",
            "element": {
                "image": result["image"],
                "text": result["text"],
                "value": result["value"],
                "discovered": True,
            },
        }


@app.get("/api/start")
async def get_starting_elements():

    return {"elements": starting_elements}


@app.get("/api/n-steps")
async def get_n_steps():

    return {"n_steps": 1000}
