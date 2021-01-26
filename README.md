<h1 align="center">B.O.O.K</h1>

B.O.O.K. is my third milestone project. The name stands for "Big Ocean of Knowledge" and it is book review and recommendation site where users can find their next read, add their recent read, rate it and share what is their oppinion about it and discuss it with other users/readers. 

## Demo 

A live demo can be found [here](https://books-ms3.herokuapp.com/).

<img src="documentation/mockup/mockup.png">

## User Experience (UX)

-   ### User stories
1. As a user I want to be able to search for books.
2. As a user I want to be able to add a book if it is not in the site and edit it if needed.
3. As a user I want to be able to rate the book and write a review and edit it if needed.
4. As a user I want to be able to register in the site.
5. As a user I want to be able to log in with username and password and have a list with all added by me books and revies.
6. As a user I want to be able to search by book or author name.
7. As a user I want to be able to filter the books by genre or author.

-   ### Wireframes

    [Balsamiq](https://balsamiq.com/) was used wireframing.
    The wireframes can be checked [here](https://github.com/Leoney/book/tree/master/documentation/wireframe).

-   ### Design

    -   #### Colour Scheme
        
        - The three main colors I have used for the design are orange, teal and white.

    -   #### Typography

        I have used three types of fonts: 
        - 'Rubik' with fallback on  Arial and sans-serif font;
        - 'Georgia' with fallback on 'Times New Roman', Times and serif font;

## Features

-   Responsive on all device sizes

-   Interactive elements

    -   #### base.html

        -   All pages will inherit html from base.html which contains website logo, navbar and footer. 
        -   Navabar pre log in: Home, Login, Register
        -   Navabar after register/log in: Home, Profile, Add Book, Genres, Log Out

    -   #### books.html(Home)

        -   Search bar 
        -   Newly Added section with the last 6 added books 

    -   #### login.html

        - Log in form with username and password.
        - Link to registration form if the user hasn't done it yet.

    -   #### register.html

        - Register form with username and password.
        - Link to log in page.

    -   #### add_book.html

        - Add book form which contains fields for: genre, book name, author name, book cover image link and book description. 

    -   #### profile.html

        - User profile page. 
        - Visible after log in. 
        - Contains list with the books and book reviews added by the user.
        - The book reviews have the option to be edited or deleted.

    -  #### book_profile.html
        
        - Contains book details like cover image, book name, author name, shor description, amazon affiliated link(not working yet), comments section. 
        - The author name is a link to author's page with all books by this author. 
        - The comments section has a button for adding new comment which is disabled if the user hasn't logged in. 

    -  #### author.html

        - Author's name and a list with all his books.

    -  #### genres.html

        - Page with all genres and samples of 6 books from each genre.
        - At the end of each genre row there is a link for more book from this genre.(inactive for the moment)

### Features Left to Implement

1. Create an affiliate link in each book profile to online store from where the user might buy it. 
2. In user's profile > Added books section -  to add edit option. 
3. In book's profile to add average rating.
4. In genres page to enable the "More [genre] ... " links. 
5. In author's page to add short biography.

## Technologies Used

### Languages Used

-   HTML
-   CSS
-   JavaScript 
-   JQuery 
-   Python3
-   Jinja

### Libraries

-   [MaterializeCSS](https://materializecss.com/): A CSS framework that assists the programmer in creating responsive, mobile first front-end web sites.
-   [Google Fonts](https://fonts.google.com/): A library of free licensed font families 
-   [PyMong](https://pymongo.readthedocs.io/en/stable/): A Python distribution containing tools for working with MongoDB.
-   [Werkzeug Security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/): Provides password security.

### API's

-   [Flask](https://flask.palletsprojects.com/en/1.1.x/): Web framework for developing applications

### Database

-   [MongoDB](https://www.mongodb.com/2): Database service.

### Deployment

- [Heroku](https://signup.heroku.com/?c=70130000000NeLCAA0&gclid=EAIaIQobChMIvb-6i4-47gIVi-5RCh2mLgpTEAAYASAAEgJSj_D_BwE): cloud platform as a service

- [Git](https://git-scm.com/): A version control system for tracking changes in source code during software development.

- [GitHub](https://github.com/): A provider of Internet hosting for software development and version control using Git.

## Testing

- [Firefox Web Developer Tools](https://developer.mozilla.org/en-US/docs/Tools)
- [ChromeDevTools](https://developers.google.com/web/tools/chrome-devtools)
- [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/#validate_by_input)
- [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
- [Pep8](http://pep8online.com/)

## Deployment

-   #### In Heroku 
    This project was deployed on [Heroku](https://signup.heroku.com/?c=70130000000NeLCAA0&gclid=EAIaIQobChMIvb-6i4-47gIVi-5RCh2mLgpTEAAYASAAEgJSj_D_BwE) and can be seen on address [http://books-ms3.herokuapp.com/](http://books-ms3.herokuapp.com/).

1. In your local project repository create requirements.txt file which to contain all the dependancies that have to be installed. It can be done by running the command bellow in your CLI: 
    ```pip3 freeze --local > requirements.txt```
2. Next create Procfile. It should be always with capital P and it specifies the commands that are executed by the app on startup. It can be done by running the command bellow in your CLI: 
    ```echo web: python app.py > Procfile```
3. Push all the files to your Git repository.
4. Register and log in [Heroku](https://signup.heroku.com/?c=70130000000NeLCAA0&gclid=EAIaIQobChMIvb-6i4-47gIVi-5RCh2mLgpTEAAYASAAEgJSj_D_BwE)
5. In Heroku click on 'Create  New App'. It has to be with unique name and for region choose the nearest to you one.
6. In the newly created app, go to Settings -> Config Vars. Here add the variables and theit values:
    -   IP = 0.0.0.0
    -   PORT = 5000
    -   SECRET_KEY = [Your Secret key]
    -   MONGO_DBNAME = [Name of DB]
    -   MONGO_URI = [MongoDb connection string]
7. To connect your project through the GitHub repository, again in your Heroku app, this time go to Deploy -> Deployment method and choose GitHub. Then select the master branch and enable automatic deployment. 

-   #### Forking the GitHub Repository
    - A fork is a copy of a repository. Forking a repository allows you to freely experiment with changes without affecting the original project.

1. Log in to GitHub and locate the [Leoney/book](https://github.com/Leoney/book)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ``` git clone ```, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Leoney/Memory-Game.git
```

7. Press Enter. Your local clone will be created.

Click [Here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

- Code Institute Tutorials 
- [MaterializeCSS](https://materializecss.com/)
- [w3school](https://www.w3schools.com/)
- [stackoverflow](https://stackoverflow.com/)
- [Goodreads](https://www.goodreads.com/)

### Acknowledgements

-   Tutor support at Code Institute for their support.
-   Code Institute's Slack Channels.
