import media
import fresh_tomatoes


# variable containing names of the movies
name = ["UP", "JOLLY LLB 2", "DANGAL", "RAEES",
        "KAABIL", "OK JAANU", "ICE AGE - COLLISSION COURSE",
        "THE JUNGLE BOOK", "3 IDIOTS"]
# variable containing storyline of the movies
story = ["Seventy-eight year old Carl Fredricksen travels"
         " to Paradise Falls in his home equipped with balloons, inadvertently"
         " taking a young stowaway.",
         "Jolly is a clumsy lawyer who is faced with representing the"
         " most critical court case of his career.",
         "Biographical sports drama on former wrestler Mahavir Singh Phogat"
         " and his two wrestler daughters' struggle towards glory at the"
         " Commonwealth Games in the face of societal oppression",
         "Criticizing the prohibition of alcohol,"
         "prostitution and illegal drugs in Gujarat, this"
         " film unfolds the story of a cruel and clever bootlegger, "
         "whose business is challenged by a tough cop.",
         "A blind man sets out to avenge the murder of his girlfriend.",
         "Adi and Tara move to Mumbai to pursue their dreams."
         " A chance meeting sparks off a heady, no strings attached romance"
         " until their careers pull them apart. Will ambition prevail over"
         "matters of the heart?",
         "Manny, Diego, and Sid join up with Buck to fend "
         "off a meteor strike that would destroy the world.",
         "After a threat from the tiger Shere Khan forces him "
         "to flee the jungle, a man-cub named Mowgli embarks on"
         " a journey of self discovery with the help of panther, Bagheera"
         ", and free spirited bear, Baloo.",
         "Two friends are searching for their"
         " long lost companion. They revisit their college days and recall"
         " the memories of their friend who inspired"
         " them to think differently,"
         " even as the rest of the world called them idiots."]
# variable containing poster url of the movies
poster = ["https://upload.wikimedia.org/wikipedia/en/0/05/"
          "Up_%282009_film%29.jpg",
          "https://upload.wikimedia.org/wikipedia"
          "/en/4/4b/Jolly_LLB_2_first_look.jpg",
          "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS"
          "sJH9vC6yxTdoTWEqLWsjhJniiS3zJDVXRDMAmi_z3GOmOmiLs",
          "https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg",
          "https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Kaabil"
          "_Movie_Poster.jpg/220px-Kaabil_Movie_Poster.jpg",
          "https://upload.wikimedia.org/wikipedia/en/b/b8/Ok_Jaanu_poster.jpg",
          "https://upload.wikimedia.org/wikipedia/en/c/c5"
          "/Ice_age_collision_course.jpg",
          "https://upload.wikimedia.org/wikipedia/en/a/a4/"
          "The_Jungle_Book_%282016%29.jpg",
          "https://upload.wikimedia.org/wikipedia/en/"
          "thumb/d/df/3_idiots_poster.jpg/220px-3_idiots_poster.jpg"]
# variable containing trailer url of the movies
trailer = ["https://www.youtube.com/watch?v=pkqzFUhGPJg",
           "https://www.youtube.com/watch?v=CevgxHk6KOk",
           "https://www.youtube.com/watch?v=x_7YlGv9u1g",
           "https://www.youtube.com/watch?v=J7_1MU3gDk0",
           "https://www.youtube.com/watch?v=nubDFeiUAsI",
           "https://www.youtube.com/watch?v=HLdbAdya2po",
           "https://www.youtube.com/watch?v=YUrbZS-XKC4",
           "https://www.youtube.com/watch?v=5mkm22yO-bs",
           "https://www.youtube.com/watch?v=K0eDlFX9GMc"]
# variable which will contain objects of the movies
ob = []
for i in range(0, 9):
    ob.append(media.Movie(name[i], story[i], poster[i], trailer[i]))
fresh_tomatoes.open_movies_page(ob)
