# Introduction to Python

Welcome to the "Introduction to Python" lesson! This lesson is designed to provide you with a solid foundation in Python programming. By the end of this lesson, you will have a good understanding of Python's basic concepts and be able to write simple Python programs.

## Table of Contents
1. [Introduction to Thonny](#introduction)
2. [Introduction to Python](#introduction)
3. [Math Wwth Python](#introduction)
4. [Strings](#introduction)
5. [Variables](#introduction)
6. [Errors](#introduction)
7. [Booleans](#introduction)
8. [Lists](#introduction)
9. [Logic](#introduction)
10. [Loops](#introduction)
11. [Functions](#introduction)
12. [Input](#introduction)
13. [Modules](#introduction)
14. [Additional Resources](#introduction)

## 1. Introduction to Thonny

### Thonny
**Thonny** is a Python Integrated Development Environment (IDE) for learning and teaching programming that can make program visualization a natural part of the beginners' workflow.

- A quick tour of Thonny (video)

### Additional Resources for Thonny
Thonny is available on a variety of platforms. The installation files are available for download [here](https://thonny.org) (opens in a new tab).

## 2. Introduction to Python

### What is Python?

Python is a programming language used for building web sites, scripting, other applications such as games and music/video editors, and lots more.

If you've never done any programming before, Python is a great language to begin with! Python was designed with readability in mind, making it the perfect starting point for learning about basic coding concepts.

### What is Programming?

But before we start learning about the Python programming language, let's talk a little about what programming is.

So what do we mean when we talk about programming?
A problem to solve

Every program begins with a problem you want to solve. That problem could be as simple as needing to do some math homework, or as complex as giving people around the world a way to talk to one another.
A solution to the problem

The solution to that problem is referred to as an algorithm (and we'll talk about that more in a few minutes).
The solution translated into a computer language

And finally, that solution is translated into a programming language, like Python, that the computer can understand.
That package of code that's run on a computer is called a program.

### What is a Computer?

So what about computers? You probably already have a good idea of what they are and what they can do.  

A computer is an electronic device that can receive data as input, has the ability to store and process that data, and produce output. Normally, computers operate by running programs.  A program is a detailed set of instructions written in a special language that tells a computer what to do with pieces of information, or data.

Computers come in a lot of different forms. You might have a laptop, or a PC. But did you know that your phone might also be a computer? Or maybe you have a game console - that's a computer too.

### What is an Algorithm?
All of those instructions we saw on the last page are similar to what we call algorithms.  The word 'algorithm' is just a fancy name for a series of steps to solve a problem or complete a tasks.  They're a lot like recipes, with specific steps to follow, and can be written using language that humans can understand. While an algorithm could be written to be understood by a human, once algorithms are converted into a special language that can be understood by a computer, it becomes a program. One of these programming languages is Python.

## 3. Math with Python
Now it's time to start writing some instructions for computers!

The first thing you need to do is open the program called Thonny. Thonny is a program that allows you to write programs in Python. If you've set up your Smart Module that came with the Smart Rover, Thonny should be on your desktop or in your Applications folder.

To do math in Python, we will use the `print()` command to tell Python to "print" the answer to the screen. Then, we will insert the math problem we want to complete in parentheses after the print command.

So our first program will look like this in Thonny:
`print(1+2)`

Once we enter this and then click the run button, the answer will display in the shell window at the bottom of the screen in Thonny.

Notice that the print command is not capitalized.

Go ahead and type the following expressions one at a time. After each one, hit the Enter key and see what happens.

`print(1 + 2)`

`print(12 - 3)`

`print(9 + 5 - 15)`

### Operators 
We're using some symbols you probably already know - the plus and minus signs. In the programming world, we call these operators.There are several more symbols, or operators that can be used.For division, we use a slanted line, called a forward slash. And for multiplication, we use a star symbol, called an asterisk.
|Name        |Symbol  |
|------------|--------|
|add         |+       |
|subtract    |−       |
|divide      |/       |
|multiply    |*       |

Let's try a few of these expressions and see what happens.

`print(6 * 5)`

`print(6 / 2)`

`print(10 * 5 * 3)`

When you finish typing these examples, feel free to try some of your own using different numbers and operators.

### Float
Let's try some more division problems:

`print(8 / 4)`

`print(20 / 7)`

`print(10 / 3)`

Are you getting the results you expect?  Are your answers all coming back as decimal numbers?

In Python, and in many other programming languages, a decimal number is called a float.  Here are some examples of decimal numbers, or floats:

10.0
17.31
2.5346

When we type a math expression using division, Python gives a float back to us as a response - the answer will always be some sort of decimal number. Python uses floats by default because it wants to give us the most accurate answer possible.

`print(10/3)` returns 3.3333333333333335

`print(10/2)` returns 5.0

The following are examples of integers - or whole numbers: 9, -55, 346

If we want Python to return an integer instead of a float, we can use the built-in Python function, called round(). Type the word print as before and then, inside parentheses, type round along with the expression you want to solve. Note that the expression still appears inside its own set of parentheses. Be sure to close both sets of parentheses at the end.one of the division expressions and hit the Enter key.

`print(round(10/3))` returns 3

`print(round(10/2))` returns 5

The rule to remember is that if by default Python answers division problems with floats.  If you want the result as an integer, you have to use the built-in function round().

### Comparison Operators 

In Python, we can do a lot of things with numbers besides just adding or dividing.

What if we need to find out if one number is larger than another? Or if one number is equal to another? Suppose you're making a video game with Python - you might want to do something like this to compare scores between two players, for example.

Well, here are some more symbols (or operators) that we can use. These are called comparison operators.

|Operator        |Meaning  |
|------------|--------|
|==	|Equal to|
|!=	|Not equal to|
|<	|Less than|
|>	|Greater than|
|<=	|Less than or equal to|
|>=	|Greater than or equal to|

Later on, you'll see some examples of how these can be used in programming. But for now, let's look at how these comparisons work.

### Variables

Now let's look at another way of working with data in Python - something called a variable.  Suppose you use a math expression to calculate a value. We've done this already. It's pretty simple, right?

Let's try this example. Type `print(6 * 6)` and hit Enter and then run the program.

The value you get back should be 36.  But what if you want to use that value again?  You could type `print(6 * 6)`, but if you were writing a program you might have to type that a lot.

Luckily, Python gives us an easier way to do it. You can give your value a name, then you can use that name over and over again.  Take a look at our next example. Here we're using the name 'puppies' then saying that puppies is equal to 6 times 6.

Go ahead and type the example below exactly as it's written here, press Enter and then run the program.

`puppies = 6 * 6`

We're assigning the value of 6 times 6 to a variable called puppies. You shouldn't get any answer back - we haven't asked for one yet. But on line 2 of your program, type `print(puppies)`, press Enter and then run the program. Do you see your value this time?

Notice that in our example the word puppies does not have any quotes around it.  If it had quotes around it, Python would treat it like a string.  Without quotes, Python knows that it's a variable.

Once you make a variable, there may be a need to give it a new value.

Try typing this example. You're making a variable with the name color, then giving it the string "yellow" as a value.

`color = "yellow"`

`print(color)`

When you run the program, Python will return the value of your variable, "yellow".

Now let's give color a new value. Continue in the same program and add this second example as it's written - remember that the variable doesn't have quotes around it, but the new value, "red", does have quotes because it's a string:

`color = "red"`

`print(color)`

When you run the program, you will see the original value followed by the new value.

Here are some of the rules to remember about variables:

Calculate once, keep the result to use later
The first thing to remember is that you can use variables to store values. You only have to do the calculation once, but you can store the result to use later.

Keep the same name, change the value
The second thing to note is that you can keep the same name for your variable, but assign it different values.

### Indexes

We talked earlier about how strings can be made up of characters, like letters or numbers, or even punctuation marks.  Each of those characters has a position in the string, and that position is called an index.

Let's look at the example we have here. This concatenated string is the word "Hello", and it's made up of five characters - five letters.

`print("H" + "e" + "l" + "l" + "o")` returns "Hello"

We could start counting to identify the position of each letter. But here's something interesting to know about Python - instead of counting from one, we're going to start counting from zero.

H e l l o
0 1 2 3 4

So in our example, the letter 'H' has an index of zero, the letter 'e' has an index of one, and so on.  It's pretty easy to figure out indexes when we can count by hand. Now let's try doing it programmatically (that is, using Python).

Try the first example. At your prompt, type the word print, then inside parentheses, the word "Hello" in quotes, and finally these square brackets with the number zero inside. Then hit Enter.

`print("Hello"[0])`

Since we're asking for the character in this string with an index of zero, Python returns the letter 'H'.

Now let's try the second example, asking Python for the character with an index of 4.

`print("Hello"[4])`

Did you get the letter 'o'? Let's see why.

H e l l o
0 1 2 3 4

If we start at the beginning of the string, the letter 'H' is at index, or position, zero. Then index 1 is the letter 'e', indexes 2 and 3 are 'l'. And index 4 is the letter 'o'.

Okay, let's try a longer example:
`print("Hey, Bob!"[4])`

Did Python return anything? Are you sure? Count by hand and see what character is at index 4.  Remember to start with zero - that's the letter 'H'. Index 1 is the letter 'e', 2 is the letter 'y', 3 is the comma, and 4 is the space. Could that be what Python returned?

Okay, one last example. We already know that we can enter an index number inside the square brackets to find its matching character in the string.  But we can also do math inside those square brackets.

`print("Hey, Bob!"[6-1])`

Here we're subtracting 1 from 6. That comes out to 5. What is the character at index 5 in this string?

Here are the rules to remember about indexes of strings.

Each character in a string has a position, and that position is called its index.
In Python - and in many other programming languages - we start counting indexes at zero (instead of one).
All the characters in a string are counted - even spaces.
Operators

Remember those operators we used for doing math? Well, we can also use some of them to do things with strings.

|Name        |Symbol  |
|------------|--------|
|add         |+       |
|subtract    |−       |

Here's a new word: **concatenate.** Concatenation is a little bit like adding - we use it to put strings together side by side.  And multiplying controls how many times we show a string.

Try typing these examples and see what Python gives you:
Try multiplying: `print("HAHA" * 250)`
Try concatenating: `print("Hi" + "there!")`

### 4. Strings
Since we have covered the basics of math in Python, it’s time to discuss a different type of data called strings.  When we use the word string in programming, we're talking about characters, like letters or symbols, or a bunch of characters put together, like words.

But maybe the best way to explain what a string is would be to show some examples.
Try typing these two examples exactly as they're written, with quotes around them, and see what you get:

`print("puppy dog")`

`print("Hello!")`

Now try typing this example without quotes and hit Enter: 

`print(apple)`

What’s the result? Did you get an error message? We will discuss  these error messages a little later on, but for now we've learned a new rule about Python and strings:

**Rule:** If you want Python to read a string, it must be inside quotes.

Try some of these other examples:

`print("apple")`

`print("What's for dinner?")`

`print("3 + 5")`

It looks like numbers, or math expressions, can also be strings - as long as they're inside quotes!

There's one other thing you might have noticed. See that second-to-last example, the one asking "What's for dinner?" ?  That string has a single quote, or an apostrophe, inside it. And that's fine, because the quotes on the outside are double quotes.

But you can also wrap a string in single quotes - Python treats both of these expressions the same way:

`print('banana')`

`print("banana")`

Suppose you have a string with an apostrophe in it. If you want to put that inside single quotes, you can escape the apostrophe - that is, tell Python that you meant for it to be part of the string:

`print('What\'s for dinner?')` returns "What's for dinner?"

However, `print('What's for dinner?')` returns SyntaxError: invalid syntax because Python thinks the apostrophe is supposed to be the end of the string.

#### Operators
Remember those operators we used for doing math? Well, we can also use some of them to do things with strings.
|Name        |Symbol  |
|------------|--------|
|add         |+       |
|subtract    |−       |

Here's a new word: **concatenate.** Concatenation is a little bit like adding - we use it to put strings together side by side.  And multiplying controls how many times we show a string. Try typing these examples and see what Python gives you.

Try multiplying:
`print("HAHA" * 250)`

Try concatenating:
`print("Hi" + "there!")`

### Indexes
We talked earlier about how strings can be made up of characters, like letters or numbers, or even punctuation marks.  Each of those characters has a position in the string, and that position is called an index.

Let's look at the example we have here. This concatenated string is the word "Hello", and it's made up of five characters - five letters.

`print("H" + "e" + "l" + "l" + "o")` returns "Hello"

We could start counting to identify the position of each letter. But here's something interesting to know about Python - instead of counting from one, we're going to start counting from zero.

H e l l o
0 1 2 3 4

So in our example, the letter 'H' has an index of zero, the letter 'e' has an index of one, and so on.  It's pretty easy to figure out indexes when we can count by hand. Now let's try doing it programmatically (that is, using Python).

Try the first example. At your prompt, type the word print, then inside parentheses, the word "Hello" in quotes, and finally these square brackets with the number zero inside. Then hit Enter.

`print("Hello"[0])`

Since we're asking for the character in this string with an index of zero, Python returns the letter 'H'.
Now let's try the second example, asking Python for the character with an index of 4.

`print("Hello"[4])`

Did you get the letter 'o'? Let's see why.

H e l l o
0 1 2 3 4

If we start at the beginning of the string, the letter 'H' is at index, or position, zero. Then index 1 is the letter 'e', indexes 2 and 3 are 'l'. And index 4 is the letter 'o'.

Okay, let's try a longer example:
`print("Hey, Bob!"[4])`

Did Python return anything? Are you sure? Count by hand and see what character is at index 4.  Remember to start with zero - that's the letter 'H'. Index 1 is the letter 'e', 2 is the letter 'y', 3 is the comma, and 4 is the space. Could that be what Python returned?

Okay, one last example. We already know that we can enter an index number inside the square brackets to find its matching character in the string.  But we can also do math inside those square brackets.

`print("Hey, Bob!"[6-1])`

Here we're subtracting 1 from 6. That comes out to 5. What is the character at index 5 in this string?
Here are the rules to remember about indexes of strings.

Each character in a string has a position, and that position is called its index.
In Python - and in many other programming languages - we start counting indexes at zero (instead of one).
All the characters in a string are counted - even spaces.

### Variables

Now let's look at another way of working with data in Python - something called a variable.  Suppose you use a math expression to calculate a value. We've done this already. It's pretty simple, right?

Let's try this example. Type `print(6 * 6)` and hit Enter and then run the program.

The value you get back should be 36.  But what if you want to use that value again?  You could type `print(6 * 6)`, but if you were writing a program you might have to type that a lot.

Luckily, Python gives us an easier way to do it. You can give your value a name, then you can use that name over and over again.  Take a look at our next example. Here we're using the name 'puppies' then saying that puppies is equal to 6 times 6.

Go ahead and type the example below exactly as it's written here, press Enter and then run the program.
`puppies = 6 * 6`

We're assigning the value of 6 times 6 to a variable called puppies. You shouldn't get any answer back - we haven't asked for one yet. But on line 2 of your program, type `print(puppies)`, press Enter and then run the program. Do you see your value this time?

Notice that in our example the word puppies does not have any quotes around it.  If it had quotes around it, Python would treat it like a string.  Without quotes, Python knows that it's a variable.

**Once you make a variable, there may be a need to give it a new value.**

Try typing this example. You're making a variable with the name color, then giving it the string "yellow" as a value.

`color = "yellow"`

`print(color)`

When you run the program, Python will return the value of your variable, "yellow".

Now let's give color a new value. Continue in the same program and add this second example as it's written - remember that the variable doesn't have quotes around it, but the new value, "red", does have quotes because it's a string:

`color = "red"`

`print(color)`

When you run the program, you will see the original value followed by the new value.

Here are some of the rules to remember about variables:

Calculate once, keep the result to use later
The first thing to remember is that you can use variables to store values. You only have to do the calculation once, but you can store the result to use later.

Keep the same name, change the value
The second thing to note is that you can keep the same name for your variable, but assign it different values.
