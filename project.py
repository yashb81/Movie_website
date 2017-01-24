import media
import fresh_tomatoes

up = media.Movie("UP", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
"https://www.youtube.com/watch?v=pkqzFUhGPJg")
jolly = media.Movie("Jolly LLB 2", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/4/4b/Jolly_LLB_2_first_look.jpg",
"https://www.youtube.com/watch?v=kvjxoBG5euo")
dangal = media.Movie("Dangal", "A story of a boy and his toys that come to life",
"https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSsJH9vC6yxTdoTWEqLWsjhJniiS3zJDVXRDMAmi_z3GOmOmiLs",
"https://www.youtube.com/watch?v=x_7YlGv9u1g")
raees = media.Movie("Raees", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg",
"https://www.youtube.com/watch?v=J7_1MU3gDk0")
kaabil = media.Movie("Kaabil", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Kaabil_Movie_Poster.jpg/220px-Kaabil_Movie_Poster.jpg",
"https://www.youtube.com/watch?v=nubDFeiUAsI")
ok_j = media.Movie("Ok Jaanu", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/b/b8/Ok_Jaanu_poster.jpg",
"https://www.youtube.com/watch?v=HLdbAdya2po")
ice = media.Movie("Ice Age - Collission Course", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/c/c5/Ice_age_collision_course.jpg",
"https://www.youtube.com/watch?v=YUrbZS-XKC4")
jungle = media.Movie("The Jungle Book", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
"https://www.youtube.com/watch?v=5mkm22yO-bs")
idiots = media.Movie("3 Idiots", "A story of a boy and his toys that come to life",
"https://upload.wikimedia.org/wikipedia/en/thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg",
"https://www.youtube.com/watch?v=K0eDlFX9GMc")

arr = [up, jolly, dangal, raees, kaabil, ok_j, ice, jungle, idiots]
fresh_tomatoes.open_movies_page(arr)
