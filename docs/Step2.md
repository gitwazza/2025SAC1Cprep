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


when adding a booking <span style="color:red"> *some emphasized markdown text*</span>

should our code's `__init__` method create an empty booking, which our code subsequently
adds attribute values to, or should we add all the attribute values when the __init__
method is run. Either way there is an issue, in that as soon as the Booking object is
instantiated it has been created, and so effectively we may have an Booking object
# with some incorrect value. There are several ways we might try to solve this dilemma
# one is that we might try to validate data prior to attempting to create the new booking
# or the other way is to leave the validation up to methods within the Booking class.
# The second method is more inline with OOP as we are making the code within the class
# responsible for it's own functionality. However, we need to handle the fact that
# we may attempt to make an object and not succeed but still have an object with an
# error that we don't want.
You have been given a starting program (step1.py), which implements some of these features. Currently, the program only stores the first and last names into the list. 

### What you are required to do