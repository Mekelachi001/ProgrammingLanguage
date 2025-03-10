vica Translated Language 🐱‍👤

How to run :
python converter.py [vica code filename] 

Tutorial:

#ADD I/O

This keyword #ADD A LIBRARY TO THE PROGRAM FOR NOW WE HAVE ONLY TWO LIBRARY I/O
AND MATH

I/O: you can use instructions like read and write 
MATH: still working on it


Start program:
START
The START keyword is used to start the program 
invoke the main function and is to be called after a function
a function can not be created within the start and end keyword

END
The End keyword is used at the end of the program

 Display Text to screen:
 WRITE [TEXT] OR [VARIABLE]:
 The write keyword is used for displaying text to a string 
 either plane text or text stored in a variable


Varable :
[DataType] [VariableName]


@@@@@ DataTypes in vica🐱‍👤
INT :
INT keyword is used to define a interger variable
Syntax: INT [VariableName]

STR 
STR keyword is used to define a string variable
Syntax: STR [VariableName]

FLOAT 
FLOAT keyword is used to define a floating point variable
Syntax: FLOAT [VariableName]

POINTER VARIABEL
Adding a * at the end of the varable type turns the variable to a pointer 

Collect input value:
READ [Text to be display when collecting text], [variable]

The Read keyword is used for reading data from user,it collect only two parameter
Text and Variable
variable  must have been created before this kwyword is called

FOR LOOP
FOR [variableName] ([Start interger],[Stop Integer])
commands or statements
ENDFOR

IF STATEMENT
SYNTAX: 
IF ([value] [condition] [value])
[condition]
ENDIF

[VALUE] the value can be a variable a string or an interger 
[condition] conditions can be
[Name]                  ""      [sign_to_use] 

equal to                ||          ==
not Equal to            ||          !=
Greater Than            ||          >
Less Than               ||          <
Less Than oo Equalto    ||          <=
Greater Than or Equalto ||          >=


[FUNC]  the function key word
Syntax : 
FUNC [TYPE] NAME (parameters ....)
statement
RETURN [VARIBLE OR TEXT]
CALLFUNC

