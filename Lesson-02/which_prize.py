def which_prize(points):
    """points, int
    input the number of points to see
    what prize they won. 
    """
    if points <= 50:
        print("Congratulations! You have won a wooden rabbit!")
    elif points <= 150:
        print("Oh dear, no prize this time.")
    elif points <= 180:
        print("Congratulations! You have won a wafer-thin mint!")
    else:
        print("Congratulations! You have won a penguin!")
        
        
which_prize(200)