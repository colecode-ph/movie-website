import media
import fresh_tomatoes

# movie instances to be displayed

avatar = media.Movie("Avatar",
                     "2009",
                     "A marine on an alien planet.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=v3qvfCPRWG0")

moon = media.Movie("Moon",
                   "2009",
                   "A Man experiences a personal crisis while living on the moon.",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Moon_%282008%29_film_poster.jpg",
                   "https://www.youtube.com/watch?v=yjevDdT3bRE")

primer = media.Movie("Primer",
                     "2004",
                     "A bunch of guys in a garage discover time travel.",
                     "https://upload.wikimedia.org/wikipedia/en/f/f7/Primer_%282004_film_poster%29.jpg",
                     "https://www.youtube.com/watch?v=3nj5MMURCm8")

coherence = media.Movie("Coherence",
                        "2013",
                        "High strangeness ensues at a dinner party as a comet passes by.",
                        "https://upload.wikimedia.org/wikipedia/en/9/9d/Coherence_2013_theatrical_poster.jpg",
                        "https://www.youtube.com/watch?v=sEceDz1Rodc")

pi = media.Movie("Pi",
                 "1998",
                 "A mathematician discovers some interesting numbers which drive him to the brink.",
                 "https://upload.wikimedia.org/wikipedia/en/5/5a/Piposter.jpg",
                 "https://www.youtube.com/watch?v=jo18VIoR2xU")

the_fountain = media.Movie("The Fountain",
                           "2006",
                           "An unconventional story about love and immortality.",
                           "https://upload.wikimedia.org/wikipedia/en/e/ee/Fountain_poster_1.jpg",
                           "https://www.youtube.com/watch?v=-4CgGfYkyFE")

#put the movies in a list and create the .html page

movies = [avatar, moon, primer, coherence, pi, the_fountain]
fresh_tomatoes.open_movies_page(movies)
