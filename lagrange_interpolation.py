#!/usr/bin/python3
program_description='''program created to interpolate values from given set using lagrange's interpolation method'''
author_name="Abhijith N Raj"
org_name = "TKMCE"
print(program_description)
print("Created By "+author_name+ " of "+org_name)


#reading values from stdin
x=[float(i) for i in input("Enter x ").split()]
y=[float(i) for i in input("Enter y ").split()]

#calculating L as ((x-x0)(x-x1)..(x-[i-1])(x-[i+1])..(x-xn))/((xi-x0)(xi-x1)..(xi-x[i-1])(xi-x[i+1])..(xi-xn))
def L(x_entered,i): 
	answer=1
	for j in range(len(x)):
		if i!=j: #every value except current index
			answer*=(x_entered-x[j])/(x[i]-x[j])
	return answer

#reading the value whose corresponding y value must be found
x_entered = float(input("Enter the x value you want to find"))

#lagranges's equation to find the polynomial
def lagrange_interpolation_algorithm(x_entered):
	solution=0
	for i in range(len(x)):
		solution+=L(x_entered,i)*y[i]
	return solution

#displaying the results of the calculations
print("Solution is y("+str(x_entered)+")= "+ str(lagrange_interpolation_algorithm(x_entered)))


		
