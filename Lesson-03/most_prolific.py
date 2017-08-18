Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

movies = {'The Game': 1980, 'A Night at the Opera': 1975, 'Jazz': 1978, 'Queen II': 1974, 'A Day at the Races': 1976, 'News of the World': 1977, 'Queen': 1973, 'Sheer Heart Attack': 1974}


def most_prolific(dictionary):
    year_list = {}
    for year in dictionary:
        if dictionary[year] not in year_list:
            year_list[dictionary[year]] = 1
        else:
            year_list[dictionary[year]] += 1
    
    counts = []
    for nums in year_list:
        counts.append(year_list[nums])
    i = max(counts)
    
    prolific_year = []
    
    for k, v in year_list.items():
        if v == i:
            prolific_year = k
    
    return prolific_year

print(most_prolific(Beatles_Discography))

print(most_prolific(movies))