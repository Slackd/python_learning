from Questions import Question

question_prompts = [
  "What color are Apples?\n (a) Red/Green\n (b) Blue\n (c) Orange\n\n",
  "What color are Bananas?\n (a) Red\n (b) Green\n (c) Yellow\n\n",
  "WWhat color are Strawberries?\n (a) Teal\n (b) Magenta\n (c) Red\n\n"
]

question = [
  Question(question_prompts[0], "a"),
  Question(question_prompts[1], "c"),
  Question(question_prompts[2], "c"),
]

def run_test(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print("You gotr " + str(score) + "/" + str(len(questions)) + " Correct!")

run_test (question)


