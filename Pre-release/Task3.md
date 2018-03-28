

**Task 3.1**

```prolog
character(habib).
charcater_type(habib,explorer).
has_skill(habib,timetravel).
pet(habib,fish).
```



**Task 3.2**

```prolog
onlyPet(C,P) :-
	character(C),
	animal(P).
```



**Task 3.3**

```prolog
character(a).
character(b).
animal(cat).
animal(dog).
pet(a,cat).
pet(b,dog).
has_skill(a,walk).
has_skill(b,run).
```



**Task 3.4**

```prolog
X = princess.
X = jim.
X = invisibility.
X = jim.
```



**Task 3.5**

```prolog
pet(jim,X).

has_skill(X,fly).

skill(X).

type_pet(T,P) :-
	character_type(C,T),
	pet(C,P).
type_pet(princess,X).
```

