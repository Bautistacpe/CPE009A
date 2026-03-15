def quadratic_equation_solver(a,b,c):
    quadratic_answer_plus = -(b) + ((b**2)-(4*a*c)**1/2)/(2*a)
    quadratic_answer_minus = -(b) - ((b**2)-(4*a*c)**1/2)/(2*a)
    return quadratic_answer_plus, quadratic_answer_minus

a = float(input("Enter a value for a: "))
b = float(input("Enter a value for b: "))
c = float(input("Enter a value for c: "))

qa_answer_plus, qa_answer_minus = quadratic_equation_solver(a,b,c)
print("The answer is:", qa_answer_plus,"or",qa_answer_minus)