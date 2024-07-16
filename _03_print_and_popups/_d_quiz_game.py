from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 

    question = simpledialog.askstring(title="question", prompt="What is 1+1")
    #      // 3.  Use an if statement to check if their answer is correct
    if question == "2":
        print("Correct")
        score = score + 1
    else:
        print("incorrect")
    #      // 4.  if the user's answer was correct, add one to their score
    question2 = simpledialog.askstring(title="question", prompt="What is 2+2")
    #      // 3.  Use an if statement to check if their answer is correct
    if question2 == "4":
        print("Correct")
        score = score + 1
    else:
        print("incorrect")
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    print("your score is " + str(score))
    # Run the window's .mainloop() method
