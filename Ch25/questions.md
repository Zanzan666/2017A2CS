# Chapter 25 Exam-style Questions
## Jenny Zhan Option3

1.
a.
Iteration:A sequence of steps is performed a number of times
Recursion: a function or procedure defined in terms of itself.

b.
Advantage: When designing a solution to a mathematical problem that is inherently recursive, the easiest way to write a solution is to implement the recursive definition.
Disadvantage: Repeated recursive calls can carry large overheads in terms of memory usage and processor time.

2.
a.
A function or procedure defined in terms of itself.

b. 
| Call number	| Procedure call	|Exponent=0	| Result	|Returned value	|
| - |---| --|---|----|
| 1             | Power(2,4)		|False		|		|		|
| 2             | Power(2,3)            |False		|		|		|
| 3             | Power(2,2)		|False		|		|		|
| 4             | Power(2,1)		|False		|		|		|
| 5             | Power(2,0)		|True		|1		|1		|
| (4)           | Power(2,1)		|		|2*1		|2		|
| (3)           | Power(2,2)		|		|2*2		|4		|
| (2)           | Power(2,3)		|		|2*4		|8		|
| (1)           | Power(2,4)		|		|2*8		|16		|

c.
For Power(2,4), the actual parameter Exponent=4, Base=2. The function call causes the return address to be put on the stack. When Result ¡û Base*Power(Base, Exponent-1)is reached, the function call causes the return address to be stored on the stack, together with the current contents of the local variables. The locations used to store these values are referred to as the stack frame. Each recursive call will add another stack frame to the stack until the base case is reached. When the base case is reached, the result of the function call Power(2,0) is returned by pushing it onto the stack. The result is popped off the stack by the previous invocation of the function. With each return from a function call, the corresponding stack frame is taken off and the values of the local variables are restroed. Eventually, control is returned with the result of the function call on the top of the stack.

e.
FUNCTION Power(Base: INTEGER, Exponent: INTEGER) RETURNS INTEGER
	Result ¡û 1
	WHILE Exponent > 0
		Result ¡û Result * Base
		Exponent ¡û Exponent - 1
	ENDWHILE
	RETURN Result
ENDFUNCTION

f
i.
Repeated recursive calls can carry large overheads in terms of memory usage and processor time.
ii. 
When designing a solution to a mathematical problem that is inherently recursive, the easiest way to write a solution is to implement the recursive definition.
		


3.
a.
i.
04
ii.
06

b.

| Call number	| Procedure call|(n = 0) OR (n = 1)	| Result	|Returned value	|
| - |---| --|---|----|
| 1             | Fibonacci(4)	|False			|		|		|
| 2             | Fibonacci(3)	|False			|		|		|
| 3             | Fibonacci(2)	|False			|		|		|
| 4             | Fibonacci(1)	|True			|0		|0		|
| 5             | Fibonacci(0)	|True			|1		|1		|
| (3)		| Fibonacci(2)	|			|1+0		|1		|
| 6		| Fibonacci(1)	|True			|1		|1		|
| (2)		| Fibonacci(3)	|			|		|2		|
| 7		| Fibonacci(2)	|False			|		|		|
| 8		| Fibonacci(1)	|True			|1		|1		|
| 9		| Fibonacci(0)	|True			|1		|1		|
| (7)		| Fibonacci(2)	|			|1+0		|1		|
| 1		| Fibonacci(4)	|			|2+1		|3		|








