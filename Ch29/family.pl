male(zsf).
male(zfy).
male(zff).
male(lzw).
male(jerry).
male(rob).

female(llz).
female(dd).
female(me).
female(kris).
female(kathlene).
female(bon).

parent(zsf,zfy).
parent(zsf,zff).
parent(llz,me).
parent(lzw,dd).
parent(zfy,me).
parent(kris,kathlene).
parent(kris,bon).
parent(john,rob).
parent(john,jerry).

brother(X,Y):- 
	male(X),
	male(Y),
	parent(A,X),
	parent(A,Y),
	not(X=Y).

siseter(X,Y):- 
	female(X),
	female(Y),
	parent(A,X),
	parent(A,Y),
	not(X=Y).

son(S,P):-
	parent(P,S),
	male(S).

daughter(X,Y):-
	parent(Y,X),
	female(Y).

married(X,Y):-
	parent(X,A),
	parent(Y,A),
	not(X=Y).

ancestor(X,Y):-
	parent(X,Y).

ancestor(X,Y):-
	parent(X,A),
	parent(A,Y).

mother(X,Y):-
	parent(X,Y),
	female(X).