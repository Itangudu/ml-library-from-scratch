After learning linear regression and how to find the proper weights through both linear regression and gradient descent this is my thought process on setting up the program

Linear Regression Function:
    1. Get the data in the proper format
    3. Add a ones column to the x data in order to be able to apply a bias to each of the rows
    4. Set up a weight matrix with x.shape[1] features
    5. Set up the error matrix to use for the loss function (might not be needed)
    6. Set the weights matrix equal to solved loss derivative function by using either mp.linalg.solve or isolating it to one side using np.linalg.inv
Gradient Descent Function:
    1. Same process in terms of data as the linear regression
    2. Set up w as an inital array of zeros so that gradient descent can adjust it as it changes
    3. make the function for the derivative of the loss function
    4. use that derivative to calculate weights using gradient descent
    5. Set limits to gradient descent using iteration limit and tolerance