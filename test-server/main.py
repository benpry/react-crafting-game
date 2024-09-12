from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
        "discovered": False,
    },
    {
        "text": "rock",
        "image": "stone",
        "discovered": False,
    },
    {
        "text": "flint",
        "image": "flint",
        "discovered": False,
    },
    {
        "text": "flax",
        "image": "flax",
        "discovered": False,
    },
    {
        "text": "forest",
        "image": "forest",
        "discovered": False,
    },
    {
        "text": "stream",
        "image": "stream",
        "discovered": False,
    },
]


crafting_table = {
    # making fire
    frozenset(("flint", "rock")): {"text": "spark", "image": "spark"},
    frozenset(("spark", "sticks")): {"text": "fire", "image": "fire"},
    # making tool handles
    frozenset(("flax", "flax")): {"text": "rope", "image": "rope"},
    frozenset(("sticks", "rope")): {"text": "tool handle", "image": "handle"},
    frozenset(("rock", "rock")): {"text": "sharpened rock", "image": "sharp-stone"},
    # tools you can make with a tool handle
    frozenset(("tool handle", "flint")): {"text": "axe", "image": "axe"},
    frozenset(("tool handle", "rock")): {"text": "trowel", "image": "trowel"},
    frozenset(("tool handle", "sharpened rock")): {"text": "spear", "image": "spear"},
    # gathering resources
    frozenset(("axe", "forest")): {"text": "logs", "image": "logs"},
    frozenset(("spear", "forest")): {"text": "raw meat", "image": "meat"},
    frozenset(("spear", "stream")): {"text": "raw fish", "image": "fish"},
    frozenset(("trowel", "stream")): {"text": "clay", "image": "clay"},
    frozenset(("trowel", "forest")): {"text": "carrot", "image": "carrot"},
    # cooking food
    frozenset(("raw meat", "fire")): {"text": "cooked meat", "image": "cooked-meat"},
    frozenset(("raw fish", "fire")): {"text": "cooked fish", "image": "cooked-fish"},
    frozenset(("carrot", "fire")): {"text": "cooked carrot", "image": "cooked-carrot"},
    # making pottery
    frozenset(("clay", "clay")): {"text": "unfired bowl", "image": "raw-bowl"},
    frozenset(("unfired bowl", "fire")): {"text": "bowl", "image": "cooked-bowl"},
    # boiling grain
    frozenset(("bowl", "stream")): {"text": "bowl of water", "image": "water-bowl"},
    frozenset(("bowl of water", "flax")): {
        "text": "raw grain bowl",
        "image": "raw-grain-bowl",
    },
    frozenset(("raw grain bowl", "fire")): {
        "text": "cooked grain bowl",
        "image": "cooked-grain-bowl",
    },
    # building a cabin
    frozenset(("axe", "logs")): {
        "text": "planks",
        "image": "planks",
    },
    frozenset(("planks", "planks")): {
        "text": "cabin",
        "image": "cabin",
    },
}

junk = {"image": "bin", "text": "junk", "discovered": True}


class CraftMessageBody(BaseModel):
    item1: str
    item2: str


@app.post("/api/combine")
async def combine(body: CraftMessageBody):
    """
    Return the result of crafting two items together
    """
    pair = frozenset((body.item1, body.item2))
    if pair not in crafting_table:
        return {"message": "crafted junk", "element": junk}
    else:
        result = crafting_table[pair]
        return {
            "message": "new element created",
            "element": {
                "image": result["image"],
                "text": result["text"],
                "discovered": True,
            },
        }


@app.get("/api/start")
async def get_starting_elements():

    return {"elements": starting_elements}
