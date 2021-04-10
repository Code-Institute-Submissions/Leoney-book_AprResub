import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Creating an instance of Flask
app = Flask(__name__)

# MongoDB connection
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Creating an instance of PyMongo
mongo = PyMongo(app)


# Creating an instance of
@app.route("/")
@app.route("/get_books")
def get_books():
    # Retrieve all books from collection 'books'
    books = list(mongo.db.books.find())
    return render_template("books.html", books=books)

# Search route
@app.route("/search", methods=["GET", "POST"])
def search():
    # text search through the 'books' collection string content
    query = request.form.get("query")
    books = list(mongo.db.books.find({"$text": {"$search": query}}))
    return render_template("books.html", books=books)

# Register route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

# User's profile route
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    books = list(mongo.db.books.find())
    check_comments = mongo.db.comments.find()
    return render_template(
        "profile.html",
        username=username,
        books=books,
        check_comments=check_comments)

# Logout route
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

# Add a book route
@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    # add new book to 'books' collection
    if request.method == "POST":
        book = {
            "category_name": request.form.get("category_name"),
            "book_name": request.form.get("book_name"),
            "author_name": request.form.get("author_name"),
            "book_cover_link": request.form.get("book_cover_link"),
            "book_description": request.form.get("book_description"),
            "added_by_user": session["user"]
        }
        mongo.db.books.insert_one(book)
        flash("Book Successfully Added")
        return redirect(url_for("get_books"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_book.html", categories=categories)

# Genres route
@app.route("/get_genres", methods=["GET"])
def get_genres():
    """ get a list of all category names and a list
        with all books through which to loop on the Genres page
        and split the books by genre """
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    books = list(mongo.db.books.find())
    return render_template("genres.html", books=books, categories=categories)

# Book's profile/details route
@app.route("/get_book_profile/<book_id>", methods=["GET"])
def get_book_profile(book_id):
    """ By the passed book_id find and get all fields of the book from books collection.
        Gets a list of all comments so on the Book Profile page can loop through it
        get only the comments which are for this book by book_name. """
    book_id = book_id
    find_book_id = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    book_name = find_book_id.get("book_name")
    check_comments = list(mongo.db.comments.find())
    books = list(mongo.db.books.find())
    return render_template(
        "book_profile.html",
        find_book_id=find_book_id,
        books=books,
        book_id=book_id,
        check_comments=check_comments)

# Author's books route
@app.route("/get_author_books/<author_name>", methods=["GET"])
def get_author_books(author_name):
    """ Get books list and on the Author page loop through it
        get only the books which have the same as the passed in author_name field value."""
    author_name = author_name
    books = list(mongo.db.books.find())
    return render_template("author.html", books=books, author_name=author_name)

# Add comment route
@app.route("/add_comment/<book_id>", methods=["GET", "POST"])
def add_comment(book_id):
    """ Post a comment for a book and redirect the user
        to the page of the same book where is posted the comment."""
    if request.method == "POST":
        dook_id = book_id
        find_book_id = mongo.db.books.find_one({"_id": ObjectId(book_id)})
        book_name = find_book_id.get("book_name")
        check_comments = mongo.db.comments.find({"book_name": book_name})
        books = list(mongo.db.books.find())
        rate_comment = {
            "book_name": book_name,
            "username": session["user"],
            "given_rate": request.form.get("rate"),
            "added_comment": request.form.get("comment_area")
        }
        mongo.db.comments.insert_one(rate_comment)
        flash("Rate/Comment Successfully Added")
        return redirect(url_for("get_book_profile", book_id=book_id))
    return render_template(
        "book_profile.html",
        find_book_id=find_book_id,
        books=books,
        book_id=book_id,
        check_comments=check_comments)

# Edit comment/review route
@app.route("/edit_review/<comment_id>", methods=["GET", "POST"])
def edit_review(comment_id):
    # Edit a comment left by the same user who has logged in
    if request.method == "POST":
        find_comment_id = mongo.db.comments.find_one(
            {"_id": ObjectId(comment_id)})
        book_name = find_comment_id.get("book_name")
        rate_comment = {
            "book_name": book_name,
            "username": session["user"],
            "given_rate": request.form.get("rate"),
            "added_comment": request.form.get("comment_area")
        }
        mongo.db.comments.update({"_id": ObjectId(comment_id)}, {
                                 "$set": rate_comment})
        flash("Review Successfully Updated")
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    books = list(mongo.db.books.find())
    check_comments = mongo.db.comments.find()
    return render_template(
        "profile.html",
        username=username,
        books=books,
        check_comments=check_comments)

# Delete comment/review route
@app.route("/delete_review/<comment_id>")
def delete_review(comment_id):
    # Delete a comment left by the same user who has logged in
    mongo.db.comments.remove({"_id": ObjectId(comment_id)})
    flash("Review Successfully Deleted")
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    books = list(mongo.db.books.find())
    check_comments = mongo.db.comments.find()
    return render_template(
        "profile.html",
        username=username,
        books=books,
        check_comments=check_comments)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
