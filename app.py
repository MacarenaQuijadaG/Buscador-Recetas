from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = '23a27707dd72478bb31126ecb193bed2'
BASE_URL = 'https://api.spoonacular.com/recipes'

@app.route('/')
def search():
    return render_template('search.html')

@app.route('/results', methods=['POST'])
def results():
    ingredients = request.form['ingredients']
    response = requests.get(f"{BASE_URL}/findByIngredients", params={
        'ingredients': ingredients,
        'number': 5,
        'apiKey': API_KEY
    })
    recipes = response.json()
    return render_template('results.html', recipes=recipes)


@app.route('/recipe/<int:recipe_id>')
def recipe(recipe_id):
    response = requests.get(f"{BASE_URL}/{recipe_id}/information", params={'apiKey': API_KEY})
    recipe = response.json()
    return render_template('recipe.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
