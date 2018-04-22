# Project 1: Movie Trailers Website
This is the first project from Udacity's Full Stack Developer Nanodegree.
It is a python generated webpage that displays my favorite movies and their trailers. It has been developed using Python 3.6.

### How it Works
The repository consists of three modules.
1. **media .py** : It contains a class movie and it's constructor that takes movie's title, poster and trailer link.
2. **entertainment_center.py**: This file makes use of the [The Movie Database](https://www.themoviedb.org/?language=en) API to retrieve information about different movies and create a list of objects, one for each movie. This list is then passed to fresh_tomatoes.py.
3. **fresh_tomatoes.py**: This file dynamically generates the html code based on the objects passed to it.

### How to Run
1. Clone the repository on to your desptop. 
2. Open the command line interface for your OS and navigate to the project directory.
3. Run the following command: `python entertainment_center.py`
4. The website will open on your default browser.
