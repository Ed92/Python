def psychologist():
    print("Please tell me your problems")
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Dont ask yourself too many questions")
            elif "good" in answer:
                print("A thats good, go on")
            elif "b" in answer:
                print("Dont be so negative")

free = psychologist()
