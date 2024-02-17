Alright so we will try to implement the gredient descent algorithm that is used 
to minimize the cost function in some machine learning algorithms, like the linear regression.
So to better understand this notion of gredient and cost function and all of this shiit, 
we will have to do a simple example of a linear regression model.

## Linear Regression
So first before moving to the cost function we will try to implement a simple linear regression situation or example
and from that we move on, am not going to explain what a linear regression is and all of that because we should already know that, 
this is only a gredient descent.

We are goint to use the grades of my classmates in the last semester as a data set i just removed on point 16.65 i consider it as
an outliar becayse its two hight, and the rest looks very linear. 

So first after we choosed and ploted the dataset now we have to create the model. but what is this model, 
yeah what does it look like, is it a function or a class or what? i don't know all i know is that at the first it should be 
a straight line, yeah and the line is defined by four things i guess, the **a**, **b** and **(x, y)**, yeah and this is 
the eqution of the line **y = ax + b**, and the process of training is nothing but adjusting the values of a and b.

But is this some kind of standard thing, is machine learnign just a bunch of straight line? well obviously no, that's why i said you 
should go and get a couse on machine learning before reading this.

Anyways now what are those parameters, well lets see for the **a, b** we know there they are the coeficients of the 
line, so they are the ones to adjest if we want to fit the line to the data set i think one is called the solpe and 
the other called the intercept, and for the **x** we can take it from the train data, and once we have all of these 
we can now calculate the **y**, and compare it with the actual y of the data set, to optimize the model, or more specificelly 
the a and b of the model, we will see how.

So first of all we will stat everything the parameters randomly, bur what about x should we also start it randomly,
no you idiot, don't understand what that x is, its the training values or more specificlly the absis of the points in
the data set.

## Cost Function 
Now we can describe how those values of a and b are updated, so to not be confused what is the cost function and what is the 
gredient descent, lets make it easy, the cost function uses the gredient descent algorithm to minimize the mean squared error 
between the predictd points and actual points, yeah i know it's complicated but the only way to really get it is to see it 
in action (or to see the math equations).

In general the cost function solves a minimization problem of \((y' - y)^2\), and we can do that by adjusting the a and b
and we can adject them using the gredient descent algorithm.

First of all before moving to the gredient descent stuff, let us explore further this cost function and see what we can get out
of it, first let us see the formula of a cost function, so that we can plot it, \[ J(a, b) = \frac{1}{2m} \sum_{i=1}^{m} (ax^{(i)} + b - y^{(i)})^2 \]
it looks scary, but i promiss this is the simplest formula you will ever see in machine learning world, am not saying that its easy, but what 
am saying is that there is a much more complex stuff in this world.

Alright so using that formula we will try to plot the J, by varing a and b from 0 up tp some number, by the way if you are wondering what
is that x and y , there are the pairs of data in the data set, so to plot this cost function i think we will just fix this x and y, means we 
will take some point in the data set, and then as i said keep varing a and b.

Ok so now after we played with the cost function and we know how it works and what it does, we can move to the most 
serious thing and the main reason we are here, which is the gredient descent.

## Gredient Descent
Now the big stuff.