**Task 1.1**

JSP structure diagrams help to design a program, as it gives a structure of the data the intended program will handle.



**Task 1.2**

*: Repetition

°: Selection



**Task 1.3**

```pseudocode
WHILE EndOfFile = FALSE
	CALL ReadSalary()
	IF Salary > 50
		THEN
			IF Salary >= 90
				THEN
					Role ← ProjectManager
				ELSE
					Role ← LeadDeveloper
			ENDIF
		ELSE
			Role ← Manager
	ENDIF
ENDWHILE
```



**Task 1.4**

```
		

		Salary Classification

				|

			Identify Role *

				|

	|						|

Read Salary				Salary>50

							|

				|False				|True

		Assign Manager °			Salary>70

									|

							|False		|True

			Assign Lead Developer		Salary>=90

											|

								|False				|True

					Assign Consultant		Assign Project Manager



```



**Task 1.5**

```pseudocode
WHILE TRUE
	CALL ReadSalary()
	IF Salary > 50
		THEN
			IF Salary > 70
				THEN
					IF Salary >= 90
						THEN
							Role ← 'Project Manager'
						ELSE
							Role ← 'Consultant'
					ENDIF
				ELSE
					Role <- 'Lead Developer'
			ENDIF
		ELSE
			Role <- 'Manager'
	ENDIF
ENDWHILE
```





**Task 1.6**

```python
def deterRole(salary):
  role = ''
  if salary < 50:
    role = 'Manager'
  elif 50 < salary <= 70:
    role = 'Lead Developer'
  elif 70 < salary < 90:
    role = 'Consultant'
  else:
    role = 'Project Manager'
  return role
```



