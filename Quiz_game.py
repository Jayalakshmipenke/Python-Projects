questions=[
    {
        "prompt" : "The Homolographic projection has the correct representation of:",
        "options" : ["A.shape","B.distance","C.baring","D.area"],
        "answer" : "D"
    },

    {
        "prompt" : "The ratio of width of our National flag to its length is:",
        "options" : ["A.3:5","B.2:4","C.2:3","D.3:4"],
        "answer" : "C"
    },
     
    {
        "prompt" : "Entomology is the science that studies:",
        "options" : ["A.on human beings","B.on Insects","C.on technical and scientific terms","D.on formation of rocks"],
        "answer" : "B"
    },
    
    {
        "prompt" : "The great Victoria Desert is located in:",
        "options" : ["A.Australia","B.Canada","C.North America","D.West Africa"],
        "answer" : "A"
    },

    {
        "prompt" : "The famous Dilwara Temples are situated in:",
        "options" : ["A.Uttar Pradesh","B.Rajasthan","C.Maharashtra","D.Madhya Pradesh"],
        "answer" : "B"
    }
]

def run_quiz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A, B, C, or D): ").upper()
        if answer == question["answer"]:
            print("Hoorey! It's correct.....!\n")
            score +=1
        else:
            print("Ohoooo! It's wrong answer....!!!! The correct answer was",question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)