# Import all necessary libraries/files
import media
import fresh_tomatoes

# Define 6 movies using Movies class from media file
butterfly_dream = media.Movie("The Dream of a Butterfly",
                              "Rustu Onur and Muzaffer Tayyip Uslu learn "
                              "poetry from their literature teacher, the "
                              "poet Behcet Necatigil.",
                              "https://i.jeded.com/i/the-butterflys-dream.15234.jpg",
                              "https://www.youtube.com/watch?v=AtHirtYl0v0")

winter_sleep = media.Movie("Winter Sleep",
                           "Aydin, his wife and his recently divorced sister "
                           "spend the winter in their hotel",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcSf9x1w9kp0GLPmiaopG13M-EFviW2zmi-QKJqKliulLdW6GJnO",
                           "https://www.youtube.com/watch?v=F2_H9b0H4d0")

leviathan = media.Movie("Leviathan",
                        "A Russian fisherman (Alexey Serebryakov) fights back "
                        "when a corrupt mayor tries to seize possession of "
                        "his ancestral home.",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcSgTLszfR7iwxmFBCyfninVzEF1rAPtRZCEEkjDBpAr6Nsx8YL_",
                        "https://www.youtube.com/watch?v=2oo7H25kirk")

the_bandit = media.Movie("The Bandit",
                         "The Bandit is a 1996 Turkish film written and "
                         "directed by Yavuz Turgul and starring Sener "
                         "Sen and Ugur Yucel",
                         "https://upload.wikimedia.org/wikipedia/tr/thumb/f/f5/Eskiya_film.jpg/220px-Eskiya_film.jpg",
                         "https://www.youtube.com/watch?v=bkFYF_hzj-o")

father_son = media.Movie("My Father and My Son",
                         "A Turkish boy (Ege Tanman) helps to mend the ties "
                         "between his father (Fikret Kuskan) and his "
                         "grandfather (Cetin Tekindor)",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/0/08/Posterbaba.jpg/220px-Posterbaba.jpg",
                         "https://www.youtube.com/watch?v=KTmrUXNxwWI")

twelve_angry_men = media.Movie("12 Angry Men",
                               "Following the closing arguments in a murder "
                               "trial, the 12 members of the jury must "
                               "deliberate, with a guilty verdict meaning "
                               "death for the accused, an inner-city teen. "
                               "As the dozen men try to reach a unanimous "
                               "decision while sequestered in a room",
                               "http://t1.gstatic.com/images?q=tbn:ANd9GcQuhFZT3lQfr0vDy4XWMHQ8X93FWuamEuw_5iB4dmOTxc_w79rA",
                               "https://www.youtube.com/watch?v=A7CBKT0PWFA")

# Add all instances of Movies class to a list called movies
movies = [winter_sleep, leviathan, butterfly_dream,
          the_bandit, father_son, twelve_angry_men]

# Use fresh_tomatoes library and the movies list to generate movies HTML page
fresh_tomatoes.open_movies_page(movies)