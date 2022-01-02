import csv

with open('movies.csv',encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    headers = data[0]
    # print(headers)

headers.append("poster_link")

with open("final.csv", "a+",newline='',encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)

with open("movie_links.csv",encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movie_links = data[1:]



for movie_item in all_movies:
    # print(len(movie_item))
    # Check if the movie title in our movies.csv has an entry in movies_links.csv. Any function returns a boolean value.
    poster_found = any(movie_item[7] in movie_link_items for movie_link_items in all_movie_links)
    if poster_found:
        for movie_link_item in all_movie_links:
            if movie_item[7] == movie_link_item[0]:
                movie_item.append(movie_link_item[1])
                # Checking if we have 27 columns for the movie. Removes inconsistency in our data
                if len(movie_item) == 27:
                    with open("final.csv", "a+",newline='',encoding="utf-8") as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerow(movie_item)