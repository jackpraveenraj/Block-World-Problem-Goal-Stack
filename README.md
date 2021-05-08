# Block-World-Problem-Goal-Stack

# Aim:
To Solve Block World problem using Goal Stack Algorithm.

# Algorithm:
In Block World problem we will model a simple block world under certain rules and constraints. That is, we will ``program'' a robotic arm to respond to a limited set of commands.
•	Push the Goal state in to the Stack
•	Push the individual Predicates of the Goal State into the Stack
•	Loop till the Stack is empty
o	Pop an element E from the stack
	IF E is a Predicate
•	IF E is True then
o	Do Nothing
•	ELSE
o	Push the relevant action into the Stack
o	Push the individual predicates of the Precondition of the action into the Stack
•	Else IF E is an Action
o	Apply the action to the current State.
o	Add the action ‘a’ to the plan
