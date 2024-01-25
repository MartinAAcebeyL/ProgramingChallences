recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}


def cakes(recipe, available):
    amounts = []
    for ingredients in recipe:
        recipe_amount = recipe.get(ingredients)
        available_amount = available.get(ingredients, None)
        if available_amount is None or available_amount < recipe_amount:
            return 0
        amount = 0
        while available_amount >= recipe_amount:
            available_amount -= recipe_amount
            amount += 1
        amounts.append(amount)

    return min(amounts)


_cakes = cakes(recipe, available)

print(_cakes)
