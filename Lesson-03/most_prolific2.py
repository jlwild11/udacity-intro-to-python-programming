Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}

movies = {'The Game': 1980, 'A Night at the Opera': 1975, 'Jazz': 1978, 'Queen II': 1974, 'A Day at the Races': 1976, 'News of the World': 1977, 'Queen': 1973, 'Sheer Heart Attack': 1974}




def most_prolific(discs): 
#We will store a dictionary of years 
#and number of albums per year     
    years = {} 
    maxyears = [] 
    maxnumber = 0 
    for disc in discs: 
        year = discs[disc]
        if year in years: 
            years[year] += 1 
        else: 
            years[year] = 1 

#find the year in which the maximum 
#number of albums was published 
#there are more elegant ways of accomplishing this, 
#but the code below works 
    for year in years:
        if years[year] > maxnumber: 
            maxyears=[] 
            maxyears.append(year) 
            maxnumber = years[year] 
        elif years[year] == maxnumber and not (year in maxyears): 
            maxyears.append(year) 
    if (len(maxyears) == 1): 
        return maxyears[0] 
    else: 
        return maxyears


print(most_prolific(Beatles_Discography))

print(most_prolific(movies))