import media
import fresh_tomatoes

# creating different instances of Movie class
me_before_you = media.Movie("Me Before You", "You only get one life. It's actually your duty to live it as fully as possible",
                            "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
                            "https://www.youtube.com/watch?v=T0MmkG_nG1U")

devil_wears_prada = media.Movie("The Devil Wears Prada","A story about cruel boss, making the experience a living hell for everybody around",
                                "https://upload.wikimedia.org/wikipedia/en/e/e7/The_Devil_Wears_Prada_main_onesheet.jpg",
                                "https://www.youtube.com/watch?v=XTDSwAxlNhc")

pearl_harbor = media.Movie("Pearl Harbor","Amazing American romantic action war film",
                                "https://upload.wikimedia.org/wikipedia/en/3/3c/Pearl_harbor_movie_poster.jpg",
                                "https://www.youtube.com/watch?v=ozksd76CSIs")

the_intern = media.Movie("The Intern","A film is about experience, that never gets old",
                                "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
                                "https://www.youtube.com/watch?v=ZU3Xban0Y6A")

into_you = media.Movie("He's Just Not That Into You","How people deal with their romantic problems and repeatedly misinterpret behaviour of their partners",
                                "https://upload.wikimedia.org/wikipedia/ru/archive/8/86/20120821044511%21He%27s_Just_Not_That_Into_You.jpg",
                                "https://www.youtube.com/watch?v=lV7bvxRQGkc")

wedding_crashers = media.Movie("Wedding Crashers","Life's a party. Crash it",
                                "https://upload.wikimedia.org/wikipedia/uk/5/53/Wedding_crashers_ver2.jpg",
                                "https://www.youtube.com/watch?v=VYrEQbtV2V4")

# Pulling objects into a list
movies = [me_before_you, devil_wears_prada, pearl_harbor, the_intern, into_you, wedding_crashers]

# Open_movies_page function receives an argument as a list of movies
fresh_tomatoes.open_movies_page(movies)
