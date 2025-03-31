fs = frozenset

starting_elements = (
    {
        "text": "sticks",
        "image": "sticks",
        "value": 0,
    },
    {
        "text": "rock",
        "image": "stone",
        "value": 0,
    },
    {
        "text": "flint",
        "image": "flint",
        "value": 0,
    },
    {
        "text": "flax",
        "image": "flax",
        "value": 0,
    },
    {
        "text": "forest",
        "image": "forest",
        "value": 0,
    },
    {
        "text": "stream",
        "image": "stream",
        "value": 0,
    },
)


crafting_table = {
    # making fire
    fs(("flint", "flint")): {
        "text": "spark",
        "image": "spark",
        "value": 1,
    },
    fs(("spark", "sticks")): {
        "text": "fire",
        "image": "fire",
        "value": 1,
    },
    fs(("spark", "sticks")): {
        "text": "fire",
        "image": "fire",
        "value": 1,
    },
    fs(("fire", "forest")): {
        "text": "forest fire",
        "image": "forest-fire",
        "value": 1,
    },
    fs(("sticks", "rock")): {"text": "fire pit", "image": "firepit", "value": 2},
    fs(("fire pit", "fire")): {
        "text": "bonfire",
        "image": "firepit-lit",
        "value": 2,
    },
    # trapping and hunting
    fs(("sticks", "sticks")): {"text": "trap", "image": "trap", "value": 1},
    fs(("trap", "forest")): {"text": "rabbit", "image": "rabbit", "value": 2},
    fs(("trap", "stream")): {"text": "fish", "image": "fish", "value": 2},
    fs(("sticks", "flint")): {"text": "arrow", "image": "arrowhead", "value": 1},
    fs(("bow", "arrow")): {
        "text": "bow and arrow",
        "image": "bow-and-arrow",
        "value": 3,
    },
    # making tool handles
    fs(("flax", "flax")): {"text": "rope", "image": "rope", "value": 1},
    fs(("sticks", "rope")): {"text": "tool handle", "image": "handle", "value": 1},
    fs(("rock", "flint")): {
        "text": "sharpened rock",
        "image": "sharp-stone",
        "value": 1,
    },
    fs(("rock", "rock")): {
        "text": "rock sliver",
        "image": "stone-sliver",
        "value": 1,
    },
    # tools you can make with a tool handle
    fs(("tool handle", "flint")): {"text": "axe", "image": "axe", "value": 2},
    fs(("tool handle", "rock sliver")): {
        "text": "trowel",
        "image": "trowel",
        "value": 2,
    },
    fs(("tool handle", "sharpened rock")): {
        "text": "spear",
        "image": "spear",
        "value": 2,
    },
    fs(("tool handle", "rope")): {"text": "bow", "image": "bow", "value": 3},
    # gathering resources
    fs(("sticks", "forest")): {"text": "apple", "image": "apple", "value": 2},
    fs(("axe", "forest")): {"text": "logs", "image": "logs", "value": 2},
    fs(("axe", "stream")): {"text": "reeds", "image": "reed", "value": 1},
    fs(("spear", "forest")): {"text": "raw meat", "image": "meat", "value": 1},
    fs(("spear", "rabbit")): {"text": "raw meat", "image": "meat", "value": 3},
    fs(("spear", "stream")): {"text": "raw fish", "image": "fish", "value": 1},
    fs(("trowel", "stream")): {"text": "clay", "image": "clay", "value": 1},
    fs(("trowel", "forest")): {"text": "carrot", "image": "carrot", "value": 2},
    fs(("bow and arrow", "forest")): {
        "text": "fancy raw meat",
        "image": "meat2",
        "value": 3,
    },
    # cooking food
    fs(("raw meat", "fire")): {
        "text": "cooked meat",
        "image": "cooked-meat",
        "value": 3,
    },
    fs(("fancy raw meat", "fire")): {
        "text": "fancy cooked meat",
        "image": "fancy-cooked-meat",
        "value": 3,
    },
    fs(("raw fish", "fire")): {
        "text": "cooked fish",
        "image": "cooked-fish",
        "value": 3,
    },
    fs(("carrot", "fire")): {
        "text": "cooked carrot",
        "image": "cooked-carrot",
        "value": 2,
    },
    fs(("cooked meat", "cooked fish")): {
        "text": "surf and turf",
        "image": "surf-and-turf",
        "value": 4,
    },
    fs(("fancy cooked meat", "cooked fish")): {
        "text": "surf and turf",
        "image": "surf-and-turf",
        "value": 4,
    },
    # making pottery
    fs(("clay", "clay")): {"text": "unfired bowl", "image": "raw-bowl", "value": 2},
    fs(("unfired bowl", "fire")): {"text": "bowl", "image": "cooked-bowl", "value": 2},
    # boiling grain
    fs(("bowl", "stream")): {
        "text": "bowl of water",
        "image": "water-bowl",
        "value": 2,
    },
    fs(("bowl of water", "flax")): {
        "text": "raw grain bowl",
        "image": "raw-grain-bowl",
        "value": 3,
    },
    fs(("bowl of water", "fire")): {
        "text": "bowl of boiling water",
        "image": "boiling-water-bowl",
        "value": 2,
    },
    # ways to make cooked grain bowls
    fs(("raw grain bowl", "fire")): {
        "text": "cooked grain bowl",
        "image": "cooked-grain-bowl",
        "value": 4,
    },
    fs(("bowl of boiling water", "flax")): {
        "text": "cooked grain bowl",
        "image": "cooked-grain-bowl",
        "value": 4,
    },
    # building some buildings
    fs(("axe", "logs")): {
        "text": "planks",
        "image": "planks",
        "value": 2,
    },
    fs(("planks", "rabbit")): {
        "text": "rabbit hutch",
        "image": "rabbit-house",
        "value": 4,
    },
    fs(("planks", "planks")): {
        "text": "cabin",
        "image": "cabin",
        "value": 3,
    },
    fs(("cabin", "bonfire")): {
        "text": "lighthouse",
        "image": "lighthouse",
        "value": 4,
    },
    # making paper and books
    fs(("reeds", "reeds")): {"text": "paper", "image": "paper", "value": 1},
    fs(("paper", "paper")): {"text": "book", "image": "book", "value": 2},
    fs(("book", "planks")): {"text": "bookshelf", "image": "bookshelf", "value": 3},
    fs(("bookshelf", "bookshelf")): {
        "text": "library",
        "image": "library",
        "value": 4,
    },
    # misc tools
    fs(("sticks", "flax")): {"text": "basket", "image": "basket", "value": 1},
    # making soup
    fs(("bowl", "cooked carrot")): {
        "text": "carrot soup",
        "image": "carrot-soup",
        "value": 3,
    },
    fs(("bowl of boiling water", "carrot")): {
        "text": "carrot soup",
        "image": "carrot-soup",
        "value": 3,
    },
}
