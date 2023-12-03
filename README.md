# Book Manager

## Installation
1. Download the files
2. Navigate to the root directory of the repo
3. Run the following command:
```
docker compose up
```

Once the container is running open your web browser and navigate to localhost:8000

## Concept
This project builds a container running Alpine Linux 3.18 with Python 3.12 installed.
It then installs Django 4.2.7 and loads in the project files.

This project allows users to add authors and books to a database.
Anyone can view the list of authors and books without being logged in, however if a user wants to contribute or make changes to the list they will need to make an account.
Users with an account can also create their own reading list which can not be seen by other users.

When visiting the website for the first time there wont be any users, authors, or books so the first step is to create an account and add an author, then add a book assigned to that author.

## Changes
1. Changed Authors to only have a "name" column not "first_name" and "last_name". Users can then write names as they are typically known rather than enforcing a format that is not always correct.
2. Added an "Add New Author" button and modal to the Add Book page. This allows users to add all the data they need on a single page without having to visit other pages.
3. Cleaned up the form pages and buttons. This made all the forms more inline and all buttons have the same appearance.
4. Removed the item IDs from the tables. Some tables were displayed aplhabetically so the IDs were out of order. The IDs were also useless to the users.
5. Changed the date_published column to be a DateField rather than a DateTimeField. Users had no need or control over the time so it just made the tables messy.
6. Added a search option to the list pages so users can quickly find the items they are after.
7. Added regex validation to the ISBN. There is a rule to ISBN formatting so it made sense to enforce it when adding items to the database.
8. Made author names unique. If author names are entered multiple times it could cause the book collection to be fractured or unorganised. Each author should only appear once.