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
