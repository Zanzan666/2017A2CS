len([],0).
len([_|T],L):-
	len(T,X),
	L is X+1.

mymember(I,[I|_]).
mymember(I,[J|T]):-
	mymember(I,T).

/* 1.01 */
last(X,[X]).
last(X,[_|T]):-
	last(Y,T),
	X is Y.

/* 1.02 */
second_last(H,[H|T]):-
	len(Z, T),
	Z is 1.
second_last(X,[_|T):-
	secondlast(Y,T),
	X is Y.
