#!/usr/bin/python3

x=[float(i) for i in input("Enter x ").split()]
y=[float(i) for i in input("Enter y ").split()]

#calculating L as ((x-x0)(x-x1)..(x-[i-1])(x-[i+1])..(x-xn))/((xi-x0)(xi-x1)..(xi-x[i-1])(xi-x[i+1])..(xi-xn))
def L(x_entered,i): 
	answer=1
	for j in range(len(x)):
		if i!=j: #every value except current index
			answer*=(x_entered-x[j])/(x[i]-x[j])
	return answer

x_entered = float(input("Enter the x value you want to find"))

def lagrange_interpolation_algorithm(x_entered):
	solution=0
	for i in range(len(x)):
		solution+=L(x_entered,i)*y[i]
	return solution

print("Solution is y("+str(x_entered)+")= "+ str(lagrange_interpolation_algorithm(x_entered)))


		
