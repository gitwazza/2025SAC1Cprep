# Step 2

In this step you will add validation. 

As adding or updating a booking should ideally involve some form of validation we
need to consider where validation code should occur. For example, our code could 
check the values it will assign to `first`, and `last` etc. prior to the Booking being
instantiated via the line of code `newbook = Booking(first, last)`. However, it makes 
sense that the `Booking` class code in the code's `__init__` method checks that the 
data it's been supplied is valid. This is part of the idea of OOP programming - in that
we would like the class to be robust. So if our program tries to instantiate a Booking object
with erroneous data, then our `Booking` class can handle it appropriately. 

However, there are some potential issues with such an approach. By the time the `__init()__` 
function runs, the new object of class Booking has already been created. This occurs because 
the __init()__ function is not a constructor. There are ways we could deal with this issue,
but because they are very Python specific, we'll treat the __init__() function like it's a 
constructor and find a way to ensure any bookings with errors don't get added to our 
Bookings list.

### protected and private variables
Most OOP languages allow for protected and private variables. Protected and private 
variables within a class (or an object), cannot be directly accessed by code other
than by the code which is part of the class definition. Python does not support truly
protected and private variables, but does have some techniques to mimic this behaviour. 
You can read about this elsewhere, but to complete this step we will make use of single
underscore variables (which are commonly referred to as protected values). So to repeat
myslef, these variables are not truly protected but Python programmers agree to treat
them as such. 

The new protected variables we will introduce will have the same name as the attributes
from step1.py program, but with an underscore in front of them. The new variables are as
follows.

`_first`,
`_last`,
`_mobile`, and
`_no_of_guests`

### @property, @xxxx.setter decorators
As with protected and private variables, most OOP languages support getter and setter 
functions. These functions are designed to get and set the values of the attributes
(variables) which are part of the class(or object). Python does have getter and setter
functions which are created by the use of certain decorators. In Python decorators are
lines that begin with '@' symbol. To add to the confusion though, because this requires
the use of the `@property` decorator this makes the use of separate getter function 
somewhat redundant. It also means that the word 'property' in Python has a very specific 
meaning, whereas in more general use within Python the work 'property' may be a synonym
for attribute or variable.

### Complete step 2
The code in **step2.py** is a modified version of **step1.py**. This code has in effect 
changed the attribute (or class variable) named `first` into a property called 
`first`. At the same time it has introduced an attribute named `_first`. It has also 
introduced two class functions - that perform the function of getting and setting. Within
the setter function, it performs validation and raises a ValueError if no firstname was
supplied. This code technique can be quite confusing at first inspection, 
and I suggest you watch https://youtu.be/k4efInGWlYI for 
an explanation of this technique if it's not clear.

Within the while loop, the code handles any error within the try except block. Bookings
only get appended to the `book_list` where no error was raised.

In a similar way you update should your code to Step1 to make this same change, and also 
the following changes.

* Make `last` a property and introduce `_last` as an attribute. Perform existence validation
so that an empty string can't be assigned to `_last`.
* Make `mobile` a property and introduce `_mobile` as an attribute. Perform existence validation
so that an empty string can't be assigned to `_mobile`.
* Make `no_of_guests` a property and introduce `_no_of_guests` as an attribute. Perform validation
so that the value will only be assigned to `_no_of_guests` if it is an 
integer between and including the values 1 and 4 .

If any of the values above is not valid then a ValueError is raised the booking is not 
added to the list.

Save your completed file as **step2*firstamelastname*.py** - where _firstname_ is your first 
name and _lastname_ is your lastname. 

Return to [index](../README.md)