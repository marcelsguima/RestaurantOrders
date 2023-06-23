import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.ingredients = set()
        self.load_menu_data(source_path)

    def load_menu_data(self, source_path: str) -> None:
        with open(source_path, newline="") as file:
            recipes = csv.reader(file)
            next(recipes)

            for row in recipes:
                dish_name, price, ingredient_name, quantity = row[:4]
                price = float(price)
                quantity = int(quantity)

                ingredient = self._get_or_create_ingredient(ingredient_name)
                dish = self._get_or_create_dish(dish_name, price)
                dish.add_ingredient_dependency(ingredient, quantity)

    def _get_or_create_ingredient(self, name: str) -> Ingredient:
        ingredient = next(
            (ing for ing in self.ingredients if ing.name == name),
            None,
        )
        if ingredient is None:
            ingredient = Ingredient(name)
            self.ingredients.add(ingredient)
        return ingredient

    def _get_or_create_dish(self, name: str, price: float) -> Dish:
        dish = next(
            (d for d in self.dishes if d.name == name and d.price == price),
            None,
        )
        if dish is None:
            dish = Dish(name, price)
            self.dishes.add(dish)
        return dish
