import media    # media.py to access Movie class and instantiate its objects
import fresh_tomatoes  # enables to call open_movies_page method

""" instantiating movie objects """
braveheart_movie = media.Movie("Braveheart",
                               "When his secret bride is executed for \
                               assaulting an English soldier who tried \
                               to rape her, William Wallace begins a revolt \
                               and leads Scottish warriors against the cruel \
                               English tyrant who rules Scotland with an \
                               iron fist.",
                               "http://ia.media-imdb.com/images/M/MV5BNjA4ODYxMDU3Nl5BMl5BanBnXkFtZTcwMzkzMTk3OA@@._V1_SX214_AL_.jpg",  # noqa
                               "www.youtube.com/watch?v=nMft5QDOHek",
                               "1995",
                               ["Mel Gibson", "James Robinson", "Sean Lawlor"])
ted_movie = media.Movie("Ted",
                        "From the creator of Family Guy comes a movie about \
                        John Bennett, whose wish of bringing his teddy bear \
                        to life came true. Now, John must decide between \
                        keeping the relationship with the teddy bear or his \
                        girlfriend, Lori.",
                        "http://ia.media-imdb.com/images/M/MV5BMTQ1OTU0ODcxMV5BMl5BanBnXkFtZTcwOTMxNTUwOA@@._V1_SX214_AL_.jpg",  # noqa
                        "https://www.youtube.com/watch?v=9fbo_pQvU7M",  # noqa
                        "2012",
                        ["Mark Wahlberg", "Mila Kunis", "Seth MacFarlane"])
shawshank_movie = media.Movie("Shawshank Redemption",
                              "Two imprisoned men bond over a number of years, \
                              finding solace and eventual redemption through \
                              acts of common decency.",
                              "http://ia.media-imdb.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SX214_AL_.jpg",  # noqa
                              "https://www.youtube.com/watch?v=6hB3S9bIaco",  # noqa
                              "1994",
                              ["Tim Robbins", "Morgan Freeman", "Bob Gunton"])

""" calling open_movies_page method by passing an array of movies
    instantiated above """
fresh_tomatoes.open_movies_page([braveheart_movie, ted_movie, shawshank_movie])
