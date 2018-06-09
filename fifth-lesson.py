from MovieModel import Movie
import fresh_tomatoes

toy_story = Movie("Toy Story",
                  "A story of a boy and his toys that come to life",
                  "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                  "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = Movie("Avatar",
               "A marine on an alien planet",
               "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
               "https://www.youtube.com/watch?v=-9ceBgWV8io")

theCircle = Movie("The circle",
                  "A technology company employee lives a moral dilemma by engaging in " +
                  "a project that leaves users' privacy limits vulnerable.",
                  "https://upload.wikimedia.org/wikipedia/en/8/80/The_Circle_%282017_film%29.png",
                  "https://www.youtube.com/watch?v=yI_av33WY8k")

movies = [toy_story, avatar, theCircle]

fresh_tomatoes.open_movies_page(movies)

