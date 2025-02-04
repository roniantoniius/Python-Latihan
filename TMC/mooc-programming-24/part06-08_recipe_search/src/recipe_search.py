# Write your solution here
def search_by_name(filename: str, word: str) -> list:
    with open(filename) as file_name:
        lines = file_name.read().strip().split("\n\n")
    hasil = []
    for resep in lines:
        reseps = resep.split("\n")
        name = reseps[0]
        if word.lower() in name.lower():
            hasil.append(name)
    return hasil    

def search_by_time(filename: str, prep_time: int):
    with open(filename) as file_name:
        lines = file_name.read().strip().split("\n\n")
    hasil = []
    for resep in lines:
        reseps = resep.split("\n")
        name = reseps[0]
        time = int(reseps[1])
        if time <= prep_time:
            hasil.append(f"{name}, preparation time {time} min")
    return hasil


def search_by_ingredient(filename: str, ingredient: str):
    with open(filename) as f:
        recipes = f.read().strip().split("\n\n")

    result = []
    for recipe in recipes:
        lines = recipe.split("\n")
        name = lines[0]
        time = int(lines[1])
        ingredients = lines[2:]
        
        if any(ingredient.lower() in ing.lower() for ing in ingredients):
            result.append(f"{name}, preparation time {time} min")

    return result

if __name__ == "__main__":
    found_recipes = search_by_name("src/recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes2 = search_by_time("src/recipes1.txt", 20)
    for recipe2 in found_recipes2:
        print(recipe2)