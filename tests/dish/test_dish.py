from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    hamburguer = Dish('hamburguer', 12.5)
    hamburguer2 = Dish('hamburguer', 12.5)
    pizza = Dish('pizza', 30)

    # Test 2.1
    assert hamburguer.name == 'hamburguer'

    # Test 2.2
    assert hash(hamburguer) == hash(hamburguer2)

    # Test 2.3
    assert hash(hamburguer) != hash(pizza)

    # Test 2.4
    assert hamburguer == hamburguer2

    # Test 2.5
    assert hamburguer != pizza

    # Test 2.6
    assert repr(pizza) == "Dish('pizza', R$30.00)"

    # Test 2.7
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish('pizza', '30')

    # Test 2.8
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish('pizza', -2)

    # Test 2.9
    queijo = Ingredient('queijo mussarela')
    pizza.add_ingredient_dependency(queijo, 8)
    pizza.recipe.get('queijo mussarela') == 8

    # Test 2.10
    assert pizza.get_restrictions() == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
    }

    # Test 2.11
    assert pizza.get_ingredients() == {queijo}
