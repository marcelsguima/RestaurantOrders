from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData
from src.models.dish import Dish

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path: str = DATA_PATH,
                 inventory_path: str = INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        dish = self._get_dish_by_name(dish_name)
        self.inventory.consume_recipe(dish.recipe)

    def get_main_menu(self, restriction: str = None) -> List[Dict]:
        main_menu = []

        for dish in self.menu_data.dishes:
            if (
                restriction is None
                or restriction not in dish.get_restrictions()
            ):
                if self._are_ingredients_available(dish):
                    dish_info = {
                        "dish_name": dish.name,
                        "ingredients": list(dish.get_ingredients()),
                        "price": dish.price,
                        "restrictions": list(dish.get_restrictions())
                    }
                    main_menu.append(dish_info)

        return main_menu

    def _are_ingredients_available(self, dish: Dish) -> bool:
        for ingredient in dish.get_ingredients():
            if self.inventory.inventory.get(ingredient, 0) <= 0:
                return False
        return True
