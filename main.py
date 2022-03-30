

app = FastAPI()

@app.get("/")
def root():
    return "recipes app {"id": id, "recipe": recipe}"


'''
define your create recipe function here at API "/recipe", given a recipe string create the recipe in any persitant storage
and return the created recipe json {"id": id, "recipe": recipe}
'''


'''
define your get recipe function here at API "/recipe/{id}", given a recipe id return a recipe json {"id": id, "recipe": recipe}
'''


'''
define your update recipe function here at API "/recipe/{id}", given a recipe id and a new recipe string(recipe_update),
 update the recipe string of recipe(id) and return new updatede recipe json {"id": id, "recipe": recipe}
return a recipe json {"id": id, "recipe": recipe}
'''


'''
define your delete recipe function here at API "/recipe/{id}", given a recipe id delete the recipe with id=id.
'''
