#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    recipe_list = [amt for amt in recipe.values()]
    ingredients_list = [amt for amt in ingredients.values()]
    total_resources = 0
    cost_per_batch = 0
    batches = 0
    for ingredient, amount in ingredients.items():
        total_resources += amount
    for ingredient, amount in recipe.items():
        cost_per_batch += amount
    print(total_resources, cost_per_batch)
    if len(recipe_list) == 1 and len(ingredients_list) == 1:
        while total_resources >= cost_per_batch:
            batches += 1
            total_resources -= cost_per_batch
        return batches
    if len(recipe_list) != len(ingredients_list):
        return 0
    while total_resources > cost_per_batch:
        for i in range(0, len(recipe_list)):
            current_recipe_item = recipe_list[i]
            current_ingredient_item = ingredients_list[i]

            if current_recipe_item > current_ingredient_item:
                break
            else:
                ingredients_list[i] = current_ingredient_item - \
                    current_recipe_item
            if i == len(recipe_list) - 1:
                batches += 1
        total_resources -= cost_per_batch
    return batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
