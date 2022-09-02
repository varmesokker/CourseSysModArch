## Inheritance

Classes
- Subclass can inherit from parent class
- Child-class inherits from parent class
![[Pasted image 20220902102826.png]]

Truck and Car inherit from Vehicle
Car and Truck are subclasses from Vehicle



### What does modular mean?
"A class you can use in other places"

"Think of modular as building blocks. You can use it elsewhere"

Code that is "standalone". It can run on its own without having to be overly specific


Modular code saves time, and therefore  reduces cost



### What does refactor mean?

Make code more readable, modular, more structure.

It is restructuring without changing the outcome and fuctionability



### What is clean code?

- Readability
- Using proper variable names (not x, y z)
- Define in functions how many methods (etc.) are used in said function

## Abstraction

Taking what you need from code
F.ex. only taking numpy from the library

"Hiding a complex structure behind a name"
- A house
- Facebook
	- You use facebook graphcially without having to execute code on your own

Abstraction is a natural extension of encapsulation



An object can have both abstract methods and concrete methods

#### Concrete method
Just a method

#### Abstract method
We always have to implement an abstract method
An abstract method is to be redefined in a child-class


### What is open source

"A project where the source code for the project is available for free"


### Importance of abstraction

Ease of use - You dont have to recreate functionality if you can just re-use it from somewhere else

Prevents code repetioion
Improves flexibility
Improves working in large teams - You dont have to know the code of other members, you just have to know what it does



## Polymorphism

There are certain prerequisites for method overriding in Python. 
- Method overriding cannot be done within a class. So we need to derive a child class from a parent
- The method must have the same name as in the parent class
- The method must have the same number of parameters as in the parent class