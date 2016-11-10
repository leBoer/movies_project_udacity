import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
the_gladiator = media.Movie("The Gladiator",
                            "Commodus takes power and strips rank from "
                            "Maximus. Maximus is then relegated to fighting to"
                            " the death in the gladiator arenas.",
                            "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=ol67qo3WhJk")
the_dark_knight = media.Movie("The Dark Knight",
                              "Batman being Batman",
                              "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")
inception = media.Movie("Inception",
                        "A thief, who steals corporate secrets through use of"
                        " dream-sharing technology, is given the inverse task"
                        " of planting an idea into the mind of a CEO.",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in "
                           "space in an attempt to ensure humanity's"
                           " survival.",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=zSWdZVtXT7E")

movies = [toy_story,
          avatar,
          the_gladiator,
          the_dark_knight,
          inception,
          interstellar]
fresh_tomatoes.open_movies_page(movies)
