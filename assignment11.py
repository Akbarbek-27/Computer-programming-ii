class IngredientError(Exception):
    pass
from dataclasses import dataclass,field
@dataclass
class Ingredient:
    name:str
    category:str
    weight:int
    _availability: str = field(init=False,default="UNKNOWN")
    def __post_init__(self):
        if self.weight <= 0:
            raise IngredientError(f"Invalid weight for {self.name}")
    @property
    def is_heavy(self):
        return self.weight > 200
    def __str__(self):
        return f"{self.name} ({self.category}, {self.weight}g) [{self._availability}]"
    def __gt__(self,other):
        return self.weight > other.weight
class PantryChecker:
    def __init__(self,ingredients,categories):
        self.ingredients = ingredients
        self.categories = categories
        self._cursor = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._cursor >= len(self.ingredients):
            raise StopIteration
        ingredient = self.ingredients[self._cursor]
        if ingredient.category in self.categories:
            ingredient._availability = "IN STOCK"
        else:
            ingredient._availability = "OUT OF STOCK"
        self._cursor += 1
        return ingredient
def pantry_report(checker):
    in_stock = 0
    out_of_stock = 0
    for ingredient in checker:
        yield str(ingredient)
        if ingredient._availability == "IN STOCK":
            in_stock += 1
        else:
            out_of_stock += 1
    yield f"Check: {in_stock} in stock, {out_of_stock} out of stock"
from contextlib import contextmanager
@contextmanager
def kitchen_session(name):
    print(f"--- Kitchen: {name} ---")
    pantry = []
    try:
        yield pantry
    except IngredientError as e:
        print(f"!!! Error: {e}")
    finally:
        print(f"--- Done: {name} ({len(pantry)} ingredients) ---")
