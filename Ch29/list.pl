len([],0).
len([_|T],L):-
	len(T,X),
	L is X+1.

mymember(I,[I|_]).
mymember(I,[J|T]):-
	mymember(I,T).


last(X,[X]).
last(X,[_|T]):-
	last(Y,T),
	X is Y.


second_last(H,[H|T]):-
	len(Z, T),
	Z is 1.
second_last(X,[_|T):-
	secondlast(Y,T),
	X is Y.

findK([A|_],1,A).
findK([_|T], N, R) :-
	findK(T, X, R),
	N is X + 1.


number([],0).
number([_|T],L) :-
  number(T,X),
  L is X + 1.

myappend([],L,L).
myappend([H|T],L,[H|R]) :-
  myappend(T,L,R).

reverse([],X,X).
reverse([H|T],R,L) :-
  reverse(T,R,[H|L]).

palindrome(X) :-
  reverse(X,Y,[]),
Y == X.