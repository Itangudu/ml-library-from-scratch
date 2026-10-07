First idea for process based off of spec is to create two functions, first is the one that calculates the derivative given the function and the variable it should be based off of and then the gradient check function will create a vector using the derivative function and compare the two to see if it is right.

Thing is code can not do derivatives algabraically, instead f is just a black box that receives a point and hands back one number, what happens inside can not be seen.

So if we can only call f at certain points and recieve certain numbers, how do we estimate the slope with respect to one variable?
My guess is that since the code can not handle any of this automatically, we just have to use estimates of the slope by plugging in two really close numbers and finding the average rate of change, but I am not sure how that will relate to multivariable functions and finding average rate of change is not the same as a using a limit definition.

I need to estimate the slope of the secant line with a small gap, so we need to girue out how small gap and where to put the points.