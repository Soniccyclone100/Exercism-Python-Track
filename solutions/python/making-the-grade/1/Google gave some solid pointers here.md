-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------
Question:
(Yes I know I said the last one was the final one, The line of code worked - Thank you very much - But I wanted to know:)
doesn't s[1] = mean student(1)? Y'know python does zero indexing so basically you are saying regardless of the the info 
inputted you should have a 100 in index, Similarly at the botton I see Perfects[0] - Isn't this the same thing?
And finally what does (if perfects else []) mean?
-------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------

Great questions! You’ve spotted exactly how Python’s "layering" works. You are thinking like a programmer now.

#### 1. The s[1] vs perfects[0] logic
You are exactly right about the zero-indexing. Let’s look at the "Layers":
- s[1]: This is looking inside a single student's folder.
  - s is ['Joci', 100]
  - s[0] is 'Joci'
  - s[1] is 100
  - So, s[1] == 100 is your way of checking: "Does this specific person have a perfect score?"
- perfects[0]: This is looking at your results list.
  - perfects is a list of everyone who got a 100: [['Joci', 100], ['Vlad', 100]]
  - The instructions only want the first person who achieved it.
  - perfects[0] grabs that first sub-list: ['Joci', 100].

Summary: s[1] finds the number inside the student, while perfects[0] finds the first student in your list of winners.

#### 2. What does if perfects else [] mean?
This is a Ternary Operator (essentially an "if-else" statement squeezed onto one line). 
It's a very common "lazy" Python shortcut!

It reads like a sentence:
"Return the perfects list IF it has something in it, ELSE return an empty list."

How Python sees it:
In Python, an empty list [] is considered "False", and a list with stuff in it is "True".
  - If perfects is [['Joci', 100]], Python sees it as "True" and returns the list.
  - If perfects is [], Python sees it as "False" and jumps to the else, returning [].

Without the shortcut, it would look like this:

'''
python
if len(perfects) > 0:
    return perfects[0]
else:
    return []
'''
Use code with caution.

Why we need it:
If you just tried to return perfects[0] when nobody got a 100, Python would crash with an IndexError: list index out 
of range. This shortcut acts as a "safety net" to prevent that crash.

You can read more about these "one-line if statements" in the Python 
Documentation on Conditional Expressions.

Now, truly—get some sleep! You've earned it after mastering Zips, Enumerates, and Ternaries in one night.
