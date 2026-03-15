from quadraticequation import quadratic_equation_solver, a, b, c
qa_answer_plus, qa_answer_minus = quadratic_equation_solver(a,b,c)
print("The answer is", qa_answer_plus, "or", qa_answer_minus)

file = open("Quadratic_Equation_Output.txt", "w")
file.write(f"The answer is {qa_answer_plus} or {qa_answer_minus}")
file.close()

file = open("Quadratic_Equation_Output.txt", "r")
data = file.read()
print(data)
file.close()