
# Introduction

This is the project page for [Udacity Programming Foundations with Python] (https://www.udacity.com/course/programming-foundations-with-python--ud036) 

[Udacity Programming Foundations with Python] (https://www.udacity.com/course/programming-foundations-with-python--ud036) is one of the courses in [Udacity Full Stack Web Developer Nano Degree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

In this project we implement a movie web page backend using python programming language. 

# Project details

There are 3 python files:

`media.py` defines a Movie class and we use Movie class later in `entertainment_center.py` to define movies. 
`fresh_tomatoes.py` is the python file we use to generate movies html page. It inputs movies from `entertainment_center.py` and generates html page.
`entertainment_center` is the file where we define indiviodual movies and then later call `fresh_tomatoes.py` to genererate Movies html page.

There is also one HTML file:
`fresh_tomatoes.html` is automatically generated when `entertainmet_center.py` executed. This HTML page is the front end result.# 

# How to generate your own page?

 - Define your movies in `entertainment_center.py` Example:

 ```
your_movie = media.Movie(movie_title,
                         movie_storyline,
                         poster_image_url,
                         youtube_trailer_url)
```

- Add all your movies into one list (Example: `movies =[movie_1, movie_2, ... ,movie_n]` )
- Call `open_movies_page(movies)` function from `fresh_tomatoes.py` file
- Your movies html page will be populated with name `fresh_tomatoes.html`

