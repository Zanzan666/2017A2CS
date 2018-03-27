# Chapter 29 Exam-style Questions

## 1

### a

#### i

```prolog
cityin(london, uk).
```

#### ii

```prolog
iVisited(strasbourg).
```

### b

```prolog
chile, argentina
```

### c

```prolog
countriesIVisited(Country) :-
	iVisited(City),
	cityIn(City,Country).
```

## 2

### a

#### i

clause 01

#### ii

clause 15

### b

#### i

Who=jack.

#### ii

False

#### iii

False

###  c

#### i

```prolog
qualifiedDriver(Driver,car).
```

#### ii

```prolog
theoryOnly(X) :-
	passedTheoryTest(X),
	not(passedDrivingTest(X)).
```

### d

Clause 11 (true), clause 01 (instantiates L as 18), clause 05 (instantiates A as 17), clause 15 ( A >= L is false) result is false.