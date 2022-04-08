"""Control all server side logic and routes"""
import os
from dotenv import find_dotenv, load_dotenv
import flask
from requests import session
from yelp import business_search
from maps import maps_search
from flask_login import current_user
from models import db, User, Favorites


app = flask.Flask(__name__)

# set up a separate route to serve the index.html file generated
# by create-react-app/npm run build.
# By doing this, we make it so you can paste in all your old app routes
# from Milestone 2 without interfering with the functionality here.
bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

load_dotenv(find_dotenv())

# Point SQLAlchemy to your Heroku database
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("MY_DATABASE")
# Gets rid of a warning
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# route for serving React page
@bp.route("/home")
def home():
    """
    Route for serving React page
    """
    return flask.render_template("index.html")


app.register_blueprint(bp)


@app.route("/")
def index():
    """Route for index page"""
    return flask.redirect(flask.url_for("login"))


@app.route("/login")
def login():
    """Route for login page on React"""
    return flask.render_template("index.html")


@app.route("/signup")
def signup():
    """Route for signup page on React"""
    return flask.render_template("index.html")


@app.route("/profile")
def profile():
    """Route for profile page on React"""
    return flask.render_template("index.html")


@app.route("/dashboard")
def dashboard():
    """Route for dashbord page on React"""
    return flask.render_template("index.html")


@app.route("/search_yelp", methods=["GET", "POST"])
def search_yelp():
    """Route for loading yelp info"""
    request = flask.request.get_json(force=True)
    location = request["location"]
    term = request["term"]
    rating = int(request["rating"])
    price = request["price"]

    business_list = business_search(location, term, rating, price)

    return flask.jsonify(business_list)


@app.route("/search_maps", methods=["GET", "POST"])
def search_maps():
    """Route for loading google maps"""
    query = flask.request.get_json(force=True)

    google_maps = maps_search(query)

    return flask.jsonify(google_maps)


@app.route("/add_to_favorites", methods=["POST"])
def save_favorites():
    data = flask.request.get_json(force=True)
    print(data)
    # user_favorites = Favorites.query.all()
    # new_favorite = Favorites(
    #     place=data.place,
    #     address=data.address,
    #     rating=data.rating,
    #     range=data.range,
    #     yelp_url=data.yelp_url,
    # )
    # db.session.add(data)
    # db.session.commit()
    return flask.jsonify("Added to the database")


# @app.route("/del_activites", methods=["POST"])
# def del_activites():
#     """Deleting List of User Reviews"""
#     del_list = request.get_json(["Actvivites"])
#     print(dellist["Activites"])  # list of rev id to delete

#     deleted = delete(Favorites).where(Review.id.in(del_list["delReviews"]))

#     db.session.execute(deleted)
#     db.session.commit()
#     return jsonify(del_list)


app.run(
    debug=True,
    host="0.0.0.0",
    port=int(os.getenv("PORT", "8080")),
)
