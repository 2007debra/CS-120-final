from tkinter import *
from tkinter import ttk
import Meal_Types

#formatting gui window
root = Tk()
root.geometry("1000x600")
root.title("What's For Dinner? - Recipe Generator Project")
root.config(bg= "light blue")

#labels on radio button and drop downs, .get() connects it to appropriate information
def show():
    lbl4.config(text=f"Meal Type: {opt.get()}")
    lbl.config(text=cb.get())
    lbl2.config(text=cb2.get())
    lbl3.config(text=cb3.get())
    

#dropdown options  
ingredient1= ["eggs", "milk", "flour","butter", "mushrooms", "garlic", "salt", "black pepper", "tortilla chips", "breadcrumbs", "mozzerella cheese", "shredded cheese", "cream cheese", "tomato sauce", "ground beef", "heavy cream", "chicken" , "tomatoes", "chicken stock", "onions", "rice", "brown sugar", "chocolate chips", "vanilla extract"]
ingredient2= ["eggs", "milk", "flour","butter", "mushrooms", "garlic", "salt", "black pepper", "tortilla chips", "breadcrumbs", "mozzerella cheese", "shredded cheese", "cream cheese", "tomato sauce", "ground beef", "heavy cream", "chicken" , "tomatoes", "chicken stock", "onions", "rice", "brown sugar", "chocolate chips", "vanilla extract"]
ingredient3= ["eggs", "milk", "flour","butter", "mushrooms", "garlic", "salt", "black pepper", "tortilla chips", "breadcrumbs", "mozzerella cheese", "shredded cheese", "cream cheese", "tomato sauce", "ground beef", "heavy cream", "chicken" , "tomatoes", "chicken stock", "onions", "rice", "brown sugar", "chocolate chips", "vanilla extract"]


#auto-selects radiobutton option   
opt = StringVar(value="Main Dishes")

#radio button options  
for lang in ["Appetizers", "Main Dishes", "Desserts"]:
    Radiobutton(root, text=lang, variable=opt, value=lang).pack(pady=2)

#drop downs information, title and formatting (known as combobox) 
cb = ttk.Combobox(root, values= sorted(ingredient1))
cb.set("First ingredient")
cb.place(x=227, y=100)

cb2 = ttk.Combobox(root, values= sorted(ingredient2))
cb2.set("Second ingredient")
cb2.pack(pady=14)

cb3 = ttk.Combobox(root, values= sorted(ingredient3))
cb3.set("Third ingredient")
cb3.place(x=627, y=100)


#regular button to display selection, aligned middle
Button(root, text="See Your Selections", command=show).pack()

#label of selections, formatted to match window's bg color, aligned middle
lbl4 = Label(root, bg= "light blue",text=" ")
lbl4.pack()

lbl = Label(root, bg= "light blue", text=" ")
lbl.pack()

lbl2 = Label(root, bg= "light blue", text=" ")
lbl2.pack()

lbl3 = Label(root, bg= "light blue", text=" ")
lbl3.pack()

#from orginal code, produces appropriate recipe result
def on_button_click():   
    selected_type = opt.get() #takes radio button result
    selected_ingredients = [cb.get().lower(), cb2.get().lower(), cb3.get().lower()] #takes drop down results
    
    if  selected_type == "Appetizers":
        
        for dish,ingredients_listed in Meal_Types.appetizers.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items(): #updates counter for selected ingredients
                ingredient = ingredient.lower().strip()
                if ingredient in (selected_ingredients):
                    counter+= 1
                    matched_ingredients.append(ingredient)

            #matches ingredients to recipe
            if counter == 1:
                output.insert(END, f" ~ You have 1 ingredient to make {dish} : {matched_ingredients[0]}\n")    
                recipe_link = Meal_Types.links_appetizers.get(dish.lower())
                output.insert(END, f"Find the full recipe here! - {recipe_link}\n\n")
                    
            elif counter >= 2:
                ingredient_string = ", ".join(matched_ingredients)
                output.insert(END, f" ~ You have {counter} ingredients to make {dish}: {ingredient_string}\n")
                recipe_link = Meal_Types.links_appetizers.get(dish.lower())
                output.insert(END, f"Find the full recipe here! - {recipe_link}\n\n")

    elif selected_type == "Main Dishes":
            
        for dish,ingredients_listed in Meal_Types.main_dishes.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items(): #updates counter for selected ingredients
                ingredient = ingredient.lower().strip()
                if ingredient in (selected_ingredients):
                    counter+= 1
                    matched_ingredients.append(ingredient)

             #matches ingredients to recipe
            if counter == 1:
                output.insert(END, f" ~ You have 1 ingredient to make {dish} : {matched_ingredients[0]}\n")    
                recipe_link = Meal_Types.links_main_dishes.get(dish.lower())
                output.insert(END, f"Find the full recipe here! - {recipe_link}\n\n")
                    
            elif counter >= 2:
                ingredient_string = ", ".join(matched_ingredients)
                output.insert(END, f" ~ You have {counter} ingredients to make {dish}: {ingredient_string}\n")
                recipe_link = Meal_Types.links_main_dishes.get(dish.lower())
                output.insert(END, f"Find the full recipe here! - {recipe_link}\n\n")
            

    elif selected_type == "Desserts":
            
        for dish,ingredients_listed in Meal_Types.desserts.items():
            counter = 0
            matched_ingredients = []

            for num, ingredient in ingredients_listed.items(): #updates counter for selected ingredients
                ingredient = ingredient.lower().strip()
                if ingredient in (selected_ingredients):
                    counter+= 1
                    matched_ingredients.append(ingredient)

            #matches ingredients to recipe
            if counter == 1:
                output.insert(END, f" ~ You have 1 ingredient to make {dish} : {matched_ingredients[0]}\n")    
                recipe_link = Meal_Types.links_desserts.get(dish.lower())
                output.insert(END, f"Find the full recipe here! - {recipe_link}\n\n")
                    
            elif counter >= 2:
                ingredient_string = ", ".join(matched_ingredients)
                output.insert(END, f" ~ You have {counter} ingredients to make {dish}: {ingredient_string}\n")
                recipe_link = Meal_Types.links_desserts.get(dish.lower())
                output.insert(END, f"Find the full recipe here! - {recipe_link}\n\n")


#displays information, aligned middle
Button(root, text="See Your Recipes!", command= on_button_click).pack(pady=10)

#presents output in textbox
output =Text(root, height=15, width=100)
output.pack(pady=10)

root.mainloop()