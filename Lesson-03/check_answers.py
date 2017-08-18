def check_answer(my_answer, correct_answer):
    if my_answer == correct_answer:
        return True
    else:
        return False



def check_answers(my_answers,correct_answers):
    """
    Checks the five answers provided to a multiple choice quiz and returns the results.
    my_answers = submitted answers 
    correct_answers - the correct answers to the test.
    """
    results= []
    for i in range(len(my_answers)):
        results.append(check_answer(my_answers[i], answers[i]))
    count_correct = 0
  
    for result in results:
        if result:
            count_correct += 1
            
    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif (len(results) - count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."