<h1 align="center">B.O.O.K. - Testing</h1>


## Functionality

- #### Navigation Bar
    - When the logo 'B.O.O.K.' (located in the top left corner on Desktop and in the middle on tablets and mobile devices) is clicked, it brings the user to the Home Page.
    - All links in the navbar are working and have been tested.
    - The hamburger menu appears on screen sizes smaller than 993px. When clicked, it expands to reveal navbar links. These have been tested and are working as expected.
    - The navigation bar stays at the top of the page on all screen sizes.
    - The navigation links change depending on if the user has registered and logged in, this has been tested.
        - Logged in user - Home, Profile, Add Book, Genres, Log Out.
        - Not logged in user - Home, Log In, Register.
    - The hover effect and active class work on all navbar links.
- #### Footer
    - Footer is always located at the bottom of the page.
- #### Buttons
    - All buttons have been tested and they bring the user to correct pages as indicated in the name of the button.
- #### Redirect
    - When a user adds a new book they are redirected to the home page where they can see the book in the "Newly Added" section.
    - When a user adds a comment for a book, they are redirected to the book's page they were on when they clicked "Add Comment".
    - When a user deletes a comment, they are redirected to the page they were on when they performed the action.
- #### Internal links
    - All internal links were tested to make sure that all pages are correctly connected 
    - Navigation links bring the user to the relevant pages.
    - Links connecting the 'Register' page to the 'Log In' page and vice versa work and have been tested.
    - Links on the book covers cards in "Newly Added" section and on "Genres" page are redirecting the user to the book's profile page.

- #### Home/Books Page
    - Search Bar returns results from book's name and auther's name fields.
    - "Newly Added" section shows the last 6 added books in descending order.
- #### Register Page
    - Username and Password are required and form will not submit unless they have been entered in the required format.
    - After submition the user is directed to his user's profile page and there is "Registration Successful!" message on the top.
- #### Log In Page
    - When correct credentials are entered, the user is logged in and a welcome flash message is displayed.
    - When incorrect credentials are entered, a flash message "Incorrect Username and/or Password" is displayed letting the user know.
- #### Log Out
    - When 'Log Out' is clicked, the user is removed from the session cookie and logged out.
    - Flash message is displayed.
- #### Profile Page
    - Displays list of all books added by the user and list of all rated/commented books.
    - The list of all rated/commented books gives the user a option to edit or delete a specific comment.
    - On clicking the "Edit" comment button a modal is displayed with autopopulated star rating bar and text field with the comment that will be edited.
    - On clicking the submit button on the edit modal, the user's rate and comment is getting updated in the database and the user is directed to his profile page where the edit comment is displayed. 

- #### Genres Page
    - Displays list of blocks for each genre and each block containg 6 book covers where each is a working link directing to the book's profile.
    - At the bottom right corner of each block there is an inactive for now link which will be directing to page with full list of all books in the respective genre.

- #### Book's Profile Page
    - Links on the book covers cards in "Newly Added" section and on "Genres" page are redirecting the user to this book's profile page.
    - Author's name is a link redirecting to page with list of all books on the site by the respective author.
    - Inactive for now Amazon website link which will be directing to the relevent book in the shopping site.
    - Active and working for logged in users "Add comment" button. For the not logged in users there is "Log in to add comment" button instead, reditrecting to the "Log in" page.
    - Comments section which displays all add comments for the relevent book but the users.

- #### Author's Page
    - The author's name, in the book's profile page, is a link redirecting to page with list of all books on the site by the respective author.
    - the page contains book covers  which are active and working links, redirecting to the relevant book's profile page. 

## Validators

-   W3C Markup Validator: 
    - [Home page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/home_html_validation.png)
    - [Register page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/register_html_validation.png)
    - [Login page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/login_html_validation.png)
    - [Profile page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/profile_html_validation.png)
    - [Add book page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/add_book_html_validation.png)
    - [Book profile page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/book_profile_html_validation.png)
    - [Genres page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/genres_html_validation.png)
    - [Author page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/author_html_validation.png)

-   W3C CSS Validator:
    - [CSS validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/css_validation.png)

-   JSHint Validator:
    - [JavaScript validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/javascript_validation.png)

-   PEP8 Validator:
    - [PEP8 validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/PEP8_validation.png)

## User Stories Testing

- #### As a first time visitor
    1. I want to be able to search for a specific book or author.
        >  Search bar is visible and available for all users on the home page.
    1. I want to be able to find the 'Register' page easily.
        >  - Link to Register page is in a navigation bar.
        >  - Link to register page under log in button in Log In page.
    1. I want to be able to register easily.
        > After registration user is logged in automatically and redirect to the Profile page.
    1. I want to be able to register easily.
        >  - Link to Register page is in a navigation bar.
        >  - Link to register page under log in button in Log In page.
 
- #### As a returning user
    1. I want to be able to navigate to the 'Login' page easily.
        >  - Link to Login page is in a navigation bar.
        >  - Link to Login page under  Register button in Register page.
    1. I want to be able to see the most recent added books.
        > On the Home page can be found lest of the 6 newly added books in descending order.
    1. I want to be able to filter books by their genre.
        > On the Home page can be found search bar where the user can search for a book by keywork or full name.
    1. I want to be able to filter books by their author.
        > On the each book's profile page, the auther's name is an activ link which directs the user to page with all books by the respected author.
    1. I want to add new books easily.
        > After log in a 'Add Book' link is visible and available in the navigation bar.
    1. I want to see list of the books I have added.
        > After successful log in user is directed to his Profile page where a list of all added by him books can be found.
    1. I want to be able to rate a book and leave a comment.
        > After log in, on each book's profile page there is visible and active button to add comment and rate a book.
    1. I want to be able to edit or delete the rate/comment I have left.
        > After successful log in user is directed to his Profile page where a list all added by the user comments can be found and a 'Delete' and 'Edit' button for each separate comment.
    1. I want to see list of the rates and comments I have left for a book.
        > After successful log in user is directed to his Profile page where a list all added by the user comments can be found.
    1. I want to view all my activity(added books and comments) on my profile page.
        > After successful log in user is directed to his Profile page where a list of all added by him books and comments can be found.
    1. I want to be able to Log out.
        > A 'Log Out' link can be faound in the navigation bar.

- #### As an admin
    1. I want to be able to delete books from the website.
        > An administrator profile is not yet added to the page. 
    1. I want to have a control of all data on the website database.
        > This can be achieved only via log in to the database directly, for now. 


### Performance Testing

- [Home page Lighthouse performance audit](https://github.com/Leoney/book/blob/master/documentation/validation_results/home_lighthouse_performance_audit.png)
- [Login page Lighthouse performance audit](https://github.com/Leoney/book/blob/master/documentation/validation_results/login_lighthouse_performance_audit.png)
- [Register page Lighthouse performance audit](https://github.com/Leoney/book/blob/master/documentation/validation_results/register_lighthouse_performance_audit.png)


### Further Testing
-   The Website was tested on Google Chrome,Mozilla Firefox, Safari.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPad, iPhone7, iPhone 8 & iPhoneX.

## Known Bugs and Errors

- On 'Add Book', if the book cover link is not from Goodreads the size of the box with the book cover link is different from the rest.
- The book cover links boxes size has to be fixed for iPad display size as well.
- In the [Profile page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/profile_html_validation.png) there are errors for repeating id names, which is happenening as the modal block is in 'for loop' and this causes the repetition. I am planing to fix it by removing the modal from the loop and using javascript function.
- In the [Add book page validation results](https://github.com/Leoney/book/blob/master/documentation/validation_results/add_book_html_validation.png) tehre is an error with a materialize component. The readonly attribute is added automatically to the component by materialize.
- After search the home page shows the results with the 'Newly Added' heading, which has to be fixed.