import os
import logging
from appconfig_helper import AppConfigHelper
from flask import Flask, Blueprint, render_template

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("RecipeLogger")

recipe = Blueprint("recipe", __name__, template_folder="templates")

os.environ['AWS_DEFAULT_REGION'] = 'eu-north-1'
appconfig = AppConfigHelper(
    "GuacFeatureFlag",
    "dev",
    "doros",
    15
)


@recipe.route("/")
def display_recipe():
    appconfig.update_config()
    form_enabled = appconfig.config["guac_flag"]["enabled"]
    logger.info(f"form_enabled = {form_enabled}")
    return render_template("recipe.html", form_enabled=form_enabled)


app = Flask(__name__)
app.register_blueprint(recipe, url_prefix="/")

if __name__ == "__main__":
    app.run(debug=True)
