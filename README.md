# CS-120-final
This was a project I worked on with my partner in my first year of university to create a recipe generator with python.

While building this recipe recommendation program, I encountered several challenges that pushed me to better understand Python logic and GUI development.

Initially, the program printed multiple ingredient matches for the same recipe instead of clearly summarizing how many ingredients matched each dish. This made the output confusing and hard to read. To fix this, I reworked the logic to properly count and display the exact number of matching ingredients per recipe, resulting in clearer and more meaningful output.

Another major challenge was integrating the program with a Tkinter interface. At first, the results were displayed using print statements in the terminal, which did not translate well into a graphical interface. I resolved this by separating the core logic into a function and connecting it to a Tkinter button. Instead of printing to the terminal, the program now updates output labels directly in the GUI, making the application more interactive and user-friendly.

I also improved how recipes were stored and displayed. Initially, all possible dishes were saved in a single list, which did not show which ingredients matched each recipe, and recipe links were printed separately. I refined this approach so that each recipe now displays the number of matching ingredients, the specific ingredients that matched, and a link to the full recipe together in a clear and organized format.

One area I struggled with was looping through dictionaries using .items(). Keeping track of keys and values was confusing at first, but using clearer variable names such as dish, ingredients, and number made the code easier to read, debug, and maintain.

Overall, this project strengthened my understanding of Python fundamentals, including loops, dictionaries, and GUI development with Tkinter. Working through these challenges helped me build a more organized, readable, and interactive program, and I learned a lot from both the mistakes and the improvements I made along the way.

## Future Improvements

Make recipe links clickable within the GUI

Add dietary filters such as vegetarian options

Include a serving-size option based on the number of people

Allow recipes to be sorted or filtered by nationality
