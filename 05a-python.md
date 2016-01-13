# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Lists are tuples are both sequences of values, values which can vary from strings, integers, variables, booleans, other lists, other tuples, and more. They both are indexed by integers. The main difference between the two is that lists are mutable. Lists are enclosed by [] which is what makes them lists. Tuples on the other hand use () which are optional, for example, 1,2,4,5,2 is a tuple just like (1,6,1,5,2).

Tuples and not lists work as keys in dictionaries because tuples can be used in the hash function and lists can't.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Lists and sets are both sequences of values. They differ in that sets can only contain unique values, are also unordered, and can contain hashable items. 

list example [1,2,1,2,4,5,3,4,2]

set example [1,2,4,5,3]

You can't find an element in a set via index like you can with lists.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is a command to create a short and anonymous function, it works just like a function except you do not assign a function name. It's a more convenient way to create functions in python and preferrable to defining functions when you need to use a certain function only once.

Example1:

my_list = range(16)

filter(lambda x: x % 3 == 0, my_list)

Example2:

sorted("Here is my answer for This Question".split(),  key=str.lower)


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.



---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





