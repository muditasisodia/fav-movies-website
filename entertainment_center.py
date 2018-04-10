import media
import fresh_tomatoes

pm=media.Movie("Princess Mononoke",
                "Saving a forest spirit",
                "https://upload.wikimedia.org/wikipedia/en/8/8c/Princess_Mononoke_Japanese_poster.png",
                "https://www.youtube.com/watch?v=4OiMOHRDs14")

hmc=media.Movie("Howl's Moving Castle",
                "Adventures with a wizard",
                "https://upload.wikimedia.org/wikipedia/en/a/a0/Howls-moving-castleposter.jpg",
                "https://www.youtube.com/watch?v=iwROgK94zcM")

sa=media.Movie("Spirited Away",
            "Saving your parents with a dragon",
            "https://upload.wikimedia.org/wikipedia/en/d/db/Spirited_Away_Japanese_poster.png",
            "https://www.youtube.com/watch?v=ByXuk9QqQkk")

tslowm=media.Movie("The Secret Life of Walter Mitty",
                    "Turning dreams into reality",
                    "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Secret_Life_of_Walter_Mitty_poster.jpg",
                    "https://www.youtube.com/watch?v=HddkucqSzSM")

tpobaw=media.Movie("The Perks of Being a Wallflower",
                    "The nuances of growing up",
                    "https://upload.wikimedia.org/wikipedia/en/0/0b/The_Perks_of_Being_a_Wallflower_Poster.jpg",
                    "https://www.youtube.com/watch?v=n5rh7O4IDc0")

pap=media.Movie("Pride and Prejudice",
                "Learning to get over ourselves",
                "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
                "https://www.youtube.com/watch?v=1dYv5u6v55Y")

movies = [pm, hmc, sa, tslowm, tpobaw, pap]

fresh_tomatoes.open_movies_page(movies)

