/* Task 29.01 */
capital_city(paris).
capital_city(berlin).
capital_city(cairo).

/* Task 29.03 */
male(aaa).
male(bbb).
male(ccc).

parent(bbb,aaa).
parent(ccc,bbb).

father(F,C) :- 
	male(F),
	parent(F,C).


/* Task 29.04 */
ancestor(A, B) :- 
	parent(A,B).
ancestor(A,B) :- 
	parent(A,X),
	ancestor(X,B).


/* Task 29.05 */
/* 120 */
