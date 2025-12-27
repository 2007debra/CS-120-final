
import Meal_Types
import THE_FINAL_FINAL_PROJECT
def on_button_click():   
    if  THE_FINAL_FINAL_PROJECT.lang == "Appetizers":
        
        for dish,ingredients_listed in Meal_Types.appetizers.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items():
                ingredient = ingredient.lower().strip()
                if ingredient in (THE_FINAL_FINAL_PROJECT.ingredient1,THE_FINAL_FINAL_PROJECT.ingredient2,THE_FINAL_FINAL_PROJECT.ingredient3):
                    counter+= 1
                    matched_ingredients.append(ingredient)

            if counter == 1:
                print(f"You have 1 ingredient to make {dish} : {matched_ingredients[0]}")    
                recipe_link = Meal_Types.links_appetizers.get(dish.lower())
                print(f"Find the full recipe here! - {recipe_link}")
                    
            elif counter >= 2:
                print(f"You have {counter} ingredients to make {dish}: {matched_ingredients}")
                recipe_link = Meal_Types.links_appetizers.get(dish.lower())
                print(f"Find the full recipe here! - {recipe_link}")

    elif THE_FINAL_FINAL_PROJECT.lang == "Main Dishes":
            
        for dish,ingredients_listed in Meal_Types.main_dishes.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items():
                ingredient = ingredient.lower().strip()
                if ingredient in (THE_FINAL_FINAL_PROJECT.ingredient1,THE_FINAL_FINAL_PROJECT.ingredient2,THE_FINAL_FINAL_PROJECT.ingredient3):
                    counter+= 1
                    matched_ingredients.append(ingredient)

            if counter == 1:
                print(f"You have 1 ingredient to make {dish} : {matched_ingredients[0]}")    
                recipe_link = Meal_Types.links_main_dishes.get(dish.lower())
                print(f"Find the full recipe here! - {recipe_link}")
                    
            elif counter >= 2:
                print(f"You have {counter} ingredients to make {dish}: {matched_ingredients}")
                recipe_link = Meal_Types.links_main_dishes.get(dish.lower())
                print(f"Find the full recipe here! - {recipe_link}")
            

    elif meal_type == "desserts":
            
        for dish,ingredients_listed in Meal_Types.desserts.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items():
                ingredient = ingredient.lower().strip()
                if ingredient in (THE_FINAL_FINAL_PROJECT.ingredient1,THE_FINAL_FINAL_PROJECT.ingredient2,THE_FINAL_FINAL_PROJECT.ingredient3):
                    counter+= 1
                    matched_ingredients.append(ingredient)

                
            if counter == 1:
                print(f"You have 1 ingredient to make {dish} : {matched_ingredients[0]}")    
                recipe_link = Meal_Types.links_desserts.get(dish.lower())
                print(f"Find the full recipe here! - {recipe_link}")
                    
            elif counter >= 2:
                print(f"You have {counter} ingredients to make {dish}: {matched_ingredients}")
                recipe_link = Meal_Types.links_desserts.get(dish.lower())
                print(f"Find the full recipe here! - {recipe_link}")


