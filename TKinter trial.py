from tkinter import *
from tkinter import ttk
import Meal_Types

def on_button_click():

    if lang == "Appetizers":
        
        for dish,ingredients_listed in Meal_Types.appetizers.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items():
                ingredient = ingredient.lower().strip()
                if ingredient in (ingredient1,ingredient2,ingredient3):
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

    elif lang == "Main Dishes":
        
        for dish,ingredients_listed in Meal_Types.main_dishes.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items():
                ingredient = ingredient.lower().strip()
                if ingredient in (ingredient1,ingredient2,ingredient3):
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
        

    elif lang == "Desserts":
        
        for dish,ingredients_listed in Meal_Types.desserts.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items():
                ingredient = ingredient.lower().strip()
                if ingredient in (ingredient1,ingredient2,ingredient3):
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

        
   

root = Tk()
root.geometry("900x600")

def show():
    lbl4.config(text=f"Meal Type: {opt.get()}")
    lbl.config(text=cb.get())
    lbl2.config(text=cb2.get())
    lbl3.config(text=cb3.get())
    

# Dropdown options  
ingredient1= ["eggs", "milk", "flour","butter", "mushrooms", "garlic", "salt", "black pepper", "tortilla chips", "breadcrumbs", "mozzerella cheese", "shredded cheese", "cream cheese", "tomato sauce", "ground beef", "heavy cream", "chicken" , "tomatoes", "chicken stock", "onions", "rice", "brown sugar", "chocolate chips", "vanilla extract"]
ingredient2= ["eggs", "milk", "flour","butter", "mushrooms", "garlic", "salt", "black pepper", "tortilla chips", "breadcrumbs", "mozzerella cheese", "shredded cheese", "cream cheese", "tomato sauce", "ground beef", "heavy cream", "chicken" , "tomatoes", "chicken stock", "onions", "rice", "brown sugar", "chocolate chips", "vanilla extract"]
ingredient3= ["eggs", "milk", "flour","butter", "mushrooms", "garlic", "salt", "black pepper", "tortilla chips", "breadcrumbs", "mozzerella cheese", "shredded cheese", "cream cheese", "tomato sauce", "ground beef", "heavy cream", "chicken" , "tomatoes", "chicken stock", "onions", "rice", "brown sugar", "chocolate chips", "vanilla extract"]


# Selected option variable  
opt = StringVar(value="Main Dishes")

# Radio buttons  
for lang in ["Appetizers", "Main Dishes", "Desserts"]:
    Radiobutton(root, text=lang, variable=opt, value=lang).pack()

# Combobox  
cb = ttk.Combobox(root, values= ingredient1)
cb.set("Select your first ingredient")
cb.pack()

cb2 = ttk.Combobox(root, values= ingredient2)
cb2.set("Select your second ingredient")
cb2.pack()

cb3 = ttk.Combobox(root, values= ingredient3)
cb3.set("Select your third ingredient")
cb3.pack()


# Label to show selected value  
lbl4 = Label(root, text=" ")
lbl4.pack()

lbl = Label(root, text=" ")
lbl.pack()

lbl2 = Label(root, text=" ")
lbl2.pack()

lbl3 = Label(root, text=" ")
lbl3.pack()

submit_button = ttk.Button(root, text="Submit and Print", command=on_button_click)
submit_button.pack()

root.mainloop()