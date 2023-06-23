from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    queijo = Ingredient('queijo mussarela')
    carne = Ingredient('carne')
    ovo = Ingredient('ovo')
    ovo2 = Ingredient('ovo')

    # Test 1.1
    assert hash(ovo) == hash(ovo2)

    # Test 1.2
    assert hash(ovo) != hash(queijo)

    # Test 1.3
    assert ovo == ovo2

    # Test 1.4
    assert queijo != carne

    # Test 1.5
    assert repr(carne) == "Ingredient('carne')"

    # Test 1.6
    assert ovo.name == 'ovo'

    # Test 1.7
    assert ovo.restrictions == {Restriction.ANIMAL_DERIVED}
