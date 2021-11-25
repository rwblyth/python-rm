Python 3.8.10 (default, Sep 28 2021, 16:10:42) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World!")
Hello World!
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> pint("Hello World!")
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#1>", line 1, in <module>
NameError: name 'pint' is not defined
>>> print("I LOVE MY HONEY!")
I LOVE MY HONEY!
>>> 
======================= RESTART: /home/rob/Hello World.py ======================
Hello World!
>>> 2+2
4
>>> 2-2
0
>>> 2/2
1.0
>>> 1+2*3
7
>>> bananas=5
>>> bananasEaten=2
>>> 4
>>> 
>>> 
>>> bananas=5
>>> bananasEaten=2
>>> bananas-bananasEaten
3
>>> bananas=10
>>> bananas-bananasEaten
8
>>> bananas=2
>>> bananas-bananasEaten
0
>>> bananas=2
>>> bananasEaten=0
>>> bananas-bananasEaten
2
>>> bananasEaten=8
>>> bananas-bananasEaten
-6
>>> rum shots=10
SyntaxError: invalid syntax
>>> rumshots=10
>>> shotstaken=4
>>> rumshots-shotstaken
6
>>> rumshots=12
>>> shotsTaken-6
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#29>", line 1, in <module>
NameError: name 'shotsTaken' is not defined
>>> rumshots=12
>>> shotsTaken=6
>>> runshots-shotsTaken
Traceback (most recent call last):
  File "/usr/lib/python3.8/idlelib/run.py", line 559, in runcode
    exec(code, self.locals)
  File "<pyshell#32>", line 1, in <module>
NameError: name 'runshots' is not defined
>>> rumshots=12
>>> shotsTaken=6
>>> rumshots-shotsTaken
6
>>> name=input("What is your name?")
What is your name?Rob
>>> print(name)
Rob
>>> name=input("what is you name?")
what is you name?rabena
>>> print(name)
rabena
>>> 