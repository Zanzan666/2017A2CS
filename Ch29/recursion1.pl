even(X):- 0 is mod(X,2).
odd(X):- not(even(X)).

factorial(0,1).
factorial(N,F):-
	X is N - 1,
	factorial(X, Y),
	F is N * Y.

bunny_ears(0,0).
bunny_ears(N,B):-
	X is N-1,
	bunny_ears(X,Y),
	B is Y+2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(2,1).
fibonacci(N,F):-
	X is N-1,
	Y is N-2,
	fibonacci(X,A),
	fibonacci(Y,B),
	F is A+B.

bunny_ears_2(0,0).
bunny_ears_2(N,B):-
	odd(N),
	X is N-1,
	bunny_ears_2(X,A),
	B is A+2.
bunny_ears_2(N,B):-
	even(N),
	X is N-1,
	bunny_ears_2(X,A),
	B is A+3.

triangle(0,0).
triangle(N,T):-
	X is N-1,
	triangle(X,A),
	T is A+N.

sum_digits(N,S):-
	0 is N//10,
	S is N.
sum_digits(N,S):-
	A is N//10,
	B is mod(N,10),
	sum_digits(A,C),
	S is B+C.

is7(1,X):-
	7 is mod(X,10).
is7(0,_).

count7(0,0).
count7(X,Y):-
	Z is Y//10,
	count7(N,Z),
	is7(M,Y),
	X is N+M.