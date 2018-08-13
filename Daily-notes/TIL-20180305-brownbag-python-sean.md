# Python

An introduction to Python, by @seanwiseman :sparkles:

These are my notes from Sean's brown bag on Python for beginners, March 5 (Sean has reviewed these notes)

Output: [a basic script](/Scripts/article.py) to call the eLife API for information about an article using the article ID

## To start

We need:

* A package manager:
 * npm [Install from web](https://www.npmjs.com/get-npm)
 * homebrew [Install from web](https://brew.sh/)
 * Python 3 [Install from web](https://www.python.org/downloads/) - here we're using v3.6.4, you'll want the Mac OS X 64-bit/32-bit installer in the list of files
* A terminal window open — search for 'terminal' in your desktop applications browser
* A text editor open — using notepad is problematic, try [Sublime](https://www.sublimetext.com/) (better for RAM) or [Atom](https://atom.io/) (open source but crashes) instead as they're designed for coding [I use the latter]

# Topics

1. [why use python?](why-use-python)
2. [variables](variables)
3. [collection types](collection-types)
4. [loops](loops)
5. [conditional statements](conditional-statements)
6. [functions](functions)
7. [imports](imports)

## why use python?

High-level programming language. More human-usable way to interact with the machine; the language does more behind the scenes.

Tends to help you produce better quality software because it is readable and extensible.

> some similarities to Perl, syntax, but better at things that Perl got stuck on

Developer productivity
Portability - generally executable across diff environments (not Mac specific)
Lots of libraries - others have already written functions to do tasks, so you can do a lot in very few lines
Enjoyment - it is an enjoyable language to use

No reasons not to use python!

eLife uses python for building standalone web apps and services; standalone components to provide information to consumers. e.g. 'lax': our article data is stored in a database, the python is used to store the data in the database and to return information when called via the API. Also used for simple tasks like deleting files.
Tends to be used as the instruction glue between a service and an outcome.

Simple workflow:
* create a text file with extension .py
* ask in terminal for python to execute it
'''python file.py'''
* python takes your .py and compiles it into byte code (.pyc) [it is an interpreted language] and then the python virtual machine (PVM) issues commands to your computer.

There is a standard way to format and style the code; to help others use it. Lots of online resources about this.

## variables

Every program needs some data. Python infers data type (duck typing; if it quacks it is a duck). Can lead to problems if you aren't aware what type you are passing in. Can define what you are entering to make it more clear (for larger scale programs).

Note variables are case-sensitive so check if camelCase or snake_case. Check the API docs to see (hope they're well documented!)

Python supports:
* str (string) = text

Use 'string'.

  create a string by assignment
  ```
  title = 'Some really Good Article'
  ```
> Now you can just use title in your program to return this string

  create by expression
  ```
  full_name = 'Sean' + ' ' + 'Wiseman'
  ```
> stores 'Sean Wiseman' as the fullname string

  Note leave single line comments in code using #

* int (integer) = numbers
Similar way to create integers. Not can just type figures as integers

```
number_one = 1
```
> number_one returns 1

```
sum = 25 + 35
```
> sum returns 60

* float (floating point decimal) = decimal numbers
* bool (boolean) = True or False

Cheap in memory, and clear, so good to use

Can assign or create with expression

```
published = True
```

Have to use Uppercase for first letter.

Not many types in comparison to other languages. Python does a lot of work in the background to work out the efficient way to use data.

### In practise
Start our script, article.py

```
# tell Python what string to use for your article ID
article_id = '33065'

# normally define a variable name in upper case if you expect it not to change, standard practise. Use lowercase where variables will change.
URL = 'https://api.elifesciences.org/articles/' + article_id
```

## collection types

Three types: list, dict (dictionary), tuple
Any type of value can be added, can be mixed type, could be variables (mostly are).

* Create a list using square brackets [ ]

```
items = []
```

To add an item to a list, use
```
items.append('Some Name')
```

To remove use .remove

```
items = ['Name1','Name2']
```
To retrieve something from the list, use the index (Python is zero-based, the first item is 0)

to retrieve first item:

```
items[0]
> Name 1
```

```
items[1]
>Name2
```


dict is a dictionary; use curly brackets {}. You will specify a key and a value attached to that key. Dictionaries always have entries in pairs. No order to these keys, just assigned by value you assign. Note that with Python >= 3.6 dictionaries maintain order.

Create:
```
article = {}
```

add
```
article['title'] = 'Some title'
```

delete - note tend not to delete items
```
del article['title']
```

To access a value from a dict, just print
```
print(article['title'])
```

A tuple is like a list but cannot add/remove items once defined/initialised. These are smaller in memory so make your program more performant/efficient. Use normal brackets ().

```
items = ('Some name', 123)
```
Also can refer by index of the values in the tuple.

Any type of value can be added, can be mixed type, could be variables (mostly are).
And can add a collection within a collection (nested) too.

### In practise

Add to our script:
```
# creating a tuple [collection] called FIELDS, won't change in contents so using capitalised variable name. Note use of camelCase.
FIELDS = ('title','impactStatement','doi')
```

## loops

To help you repeat something. Two types of loop: while and for.

### While

```
count = 0

while count <100:
  count += 1
```
is a loop that means: while count is less than 100, keep adding 1 to count.
Generally long-running loops. Waiting for something to become True, e.g while article is not published, do this; keep doing it until article is no longer not published (e.g. published).

### for

```
article_ids = [14570, 15605, 15780]

#loop through all article ids and print them
for article in article_ids:
  print(article)
```

Executing this would do actions in order. First time it executes, it would print 14570. Second time, print 15605, etc:

>> 14570
>> 15605
>> 15780

Can use to add logic.

Note important to use indentation in python, no {} to show where the statement starts and finishes, so must tab your action under your loop statement. Note text editor or IDE that is aware of python will know to indent or will show you if something looks wrong, like a spell check for code.

### In practise

Add a for loop to our script:

```
# add a for loop to print the information in FIELDS for each article. Here, 'field' is a temporary variable, a name for the information behind it.
for field in FIELDS:
    print(field)
```

Now that we have an action in our .py (print), we can execute it.

In terminal, navigate to directory where article.py is saved; then execute it by calling
```
python3 article.py
```
Note if you type python, it will execute in Python 2. Type python3 to execute in python 3!

Returns:
```
title
impactStatement
doi
```

## conditional statements

adding logic

If - if this is true, do this.

Can chain together supplementary statements too:
elif - else if this, do this
else - else do this (no other ifs)

e.g.
```
article_views = 1200

if article_views == 0:
  print('This article has not been viewed')
elif article_views > 1000:
  print('This is a popular article')
else:
  print('This article has been viewed')
```

note need to use == to say equal to a value (= is used for assigning)  

Two ifs would be independent. Using elif after if makes it dependent on first if. else is a catch-all for the last outcome.

Don't have to have elif or else. Can just have an if.

## functions

Making your code reusable and portable.

define using def

define a function called greet that takes in a value (name) and executes the print command.

```
def greet(name):
  print('Hello' + name)
```

Can use this function later.

## imports

standing on the shoulders of giants: likely to import code from others, to do jobs other people have already written.

```
import library as lib
```

to use requests, first need to install
e.g. install the requests library

use the python package manager pip (for python3, pip3)
Do this in command line (terminal)

```
pip3 install requests
```

If a permissions error, try using sudo in front of the command (not specific to python):

```
sudo pip3 install requests
```

Then in your script file, tell python you want access to it:

```
import requests
```

Add this at top of script.


Now refine script with a call to the API and amend fields loop for article fields

```
# I want requests library to get me article data from URL and convert to JSON
article = requests.get(URL).json()

# add a for loop to print the information in FIELDS for each article. Here, 'field' is a temporary variable, a name for the information behind it.
for field in FIELDS:
    print(article[field])
```


Now running our script, with article defined as 33065, returns:

```
Impact of the scale-up of piped water on urogenital schistosomiasis infection in rural South Africa
Scale-up of safe water supplies decreases a child's risk of urogenital schistosomiasis infection by eight-fold in a typical rural African population.
10.7554/eLife.33065
```
