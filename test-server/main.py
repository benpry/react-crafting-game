from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from multiset import FrozenMultiset as fms

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

starting_elements = [
    {
        "text": "sticks",
        "image": "sticks",
        "value": 0,
        "discovered": False,
    },
    {
        "text": "rock",
        "image": "stone",
        "value": 0,
        "discovered": False,
    },
    {
        "text": "flint",
        "image": "flint",
        "value": 0,
        "discovered": False,
    },
    {
        "text": "flax",
        "image": "flax",
        "value": 0,
        "discovered": False,
    },
    {
        "text": "forest",
        "image": "forest",
        "value": 0,
        "discovered": False,
    },
    {
        "text": "stream",
        "image": "stream",
        "value": 0,
        "discovered": False,
    },
]


crafting_table = {
    # making fire
    fms(("flint", "rock")): {"text": "spark", "image": "spark", "value": 1},
    fms(("spark", "sticks")): {"text": "fire", "image": "fire", "value": 2},
    # making tool handles
    fms(("flax", "flax")): {"text": "rope", "image": "rope", "value": 1},
    fms(("sticks", "rope")): {"text": "tool handle", "image": "handle", "value": 2},
    fms(("rock", "rock")): {
        "text": "sharpened rock",
        "image": "sharp-stone",
        "value": 1,
    },
    # tools you can make with a tool handle
    fms(("tool handle", "flint")): {"text": "axe", "image": "axe", "value": 3},
    fms(("tool handle", "rock")): {"text": "trowel", "image": "trowel", "value": 3},
    fms(("tool handle", "sharpened rock")): {
        "text": "spear",
        "image": "spear",
        "value": 3,
    },
    # gathering resources
    fms(("axe", "forest")): {"text": "logs", "image": "logs", "value": 2},
    fms(("spear", "forest")): {"text": "raw meat", "image": "meat", "value": 1},
    fms(("spear", "stream")): {"text": "raw fish", "image": "fish", "value": 1},
    fms(("trowel", "stream")): {"text": "clay", "image": "clay", "value": 1},
    fms(("trowel", "forest")): {"text": "carrot", "image": "carrot", "value": 2},
    # cooking food
    fms(("raw meat", "fire")): {
        "text": "cooked meat",
        "image": "cooked-meat",
        "value": 5,
    },
    fms(("raw fish", "fire")): {
        "text": "cooked fish",
        "image": "cooked-fish",
        "value": 5,
    },
    fms(("carrot", "fire")): {
        "text": "cooked carrot",
        "image": "cooked-carrot",
        "value": 5,
    },
    # making pottery
    fms(("clay", "clay")): {"text": "unfired bowl", "image": "raw-bowl", "value": 2},
    fms(("unfired bowl", "fire")): {"text": "bowl", "image": "cooked-bowl", "value": 3},
    # boiling grain
    fms(("bowl", "stream")): {
        "text": "bowl of water",
        "image": "water-bowl",
        "value": 3,
    },
    fms(("bowl of water", "flax")): {
        "text": "raw grain bowl",
        "image": "raw-grain-bowl",
        "value": 4,
    },
    fms(("raw grain bowl", "fire")): {
        "text": "cooked grain bowl",
        "image": "cooked-grain-bowl",
        "value": 7,
    },
    # building a cabin
    fms(("axe", "logs")): {
        "text": "planks",
        "image": "planks",
        "value": 3,
    },
    fms(("planks", "planks")): {
        "text": "cabin",
        "image": "cabin",
        "value": 7,
    },
}

junk = {"image": "bin", "text": "junk", "value": 0, "discovered": True}


class CraftMessageBody(BaseModel):
    item1: str
    item2: str


@app.post("/api/combine")
async def combine(body: CraftMessageBody):
    """
    Return the result of crafting two items together
    """
    pair = fms((body.item1, body.item2))
    if pair not in crafting_table:
        return {"message": "crafted junk", "element": junk}
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
