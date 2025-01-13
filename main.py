from flask import Flask, Blueprint, render_template

recipe = Blueprint("recipe", __name__, template_folder="templates")

@recipe.route("/")
def display_recipe():
    return render_template("recipe.html", display_form=True)

app = Flask(__name__)
app.register_blueprint(recipe, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
