# MovieTrailers
## Description
Movie trailer project reads a list of movies and loads them in an HTML page using python

## How to execute it?
1. Navigate to MovieTrailers projects folder
2. Execute the following command  `python entertainment_center.py`
3. To view the trailer, click on a movie tile on the webpage opened after executing last step

## Whats included?
Movie Trailer Project
- media.py
- entertainment_center.py
- fresh_tomatoes.py

### media.py
This python file contains Movie class constructor which is used to define the movie information using properties like title, description, poster, trailer, Release year, cast.

### entertainment_center.py
This python file generates multiple Movie instances and passes them to fresh_tomatoes.py method open_movies_page as a list to load these movies in HTML page

### fresh_tomatoes.py
It defines the method to receive movies list to load them in HTML page.
