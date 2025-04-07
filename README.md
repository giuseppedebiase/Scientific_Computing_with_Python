# Scientific Computing with Python
Projects from the freeCodeCamp's course "[Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/)"

## Projects  
Two kinds of projects in this repo:  
 * "Learn X by Building Y": This are guided exercises where FCC teaches Python concepts.  
 * "Certification Project: Build X": Projects that you must submit to earn the certification. FCC gives you a (almost) blank IDE. 

List of Certification Projects:  
 * [Arithmetic Formatter Project](https://github.com/giuseppedebiase/Scientific_Computing_with_Python#certification-project-build-an-arithmetic-formatter-project)
 * [Time Calculator Project](https://github.com/giuseppedebiase/Scientific_Computing_with_Python#certification-project-build-a-time-calculator-project)
 * [Budget App Project](https://github.com/giuseppedebiase/Scientific_Computing_with_Python#certification-project-build-a-budget-app-project)
 * Polygon Area Calculator Project
 * Probability Calculator Project
  
[Learn String Manipulation by Building a Cipher](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/1_vigenere.py)  
[Learn How to Work with Numbers and Strings by Implementing the Luhn Algorithm](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/2_luhn.py)  
[Learn Lambda Functions by Building an Expense Tracker](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/3_expense_tracker.py)  
[Learn Python List Comprehension by Building a Case Converter Program](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/4_case_converter.py)  
[Learn the Bisection Method by Finding the Square Root of a Number](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/5_square_root.py)

### [Certification Project: Build an Arithmetic Formatter Project](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/6_cert_arithmetic_formatter.py)
**Assignement**  
Students in primary school often arrange arithmetic problems vertically to make them easier to solve. For example, "235 + 52" becomes:
```
  235
+  52
-----
```
Finish the `arithmetic_arranger` function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side. The function should optionally take a second argument. When the second argument is set to `True`, the answers should be displayed.  

**Example**  
Function call:  
```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
```
Output:  
```python
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
```

Function Call:  
```python
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
```
Output:
```python
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
```

**Rules**  
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.  
Situations that will return an error:
  * If there are too many problems supplied to the function. The limit is five, anything more will return: `'Error: Too many problems.'`
  * The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: `"Error: Operator must be '+' or '-'."`
  * Each number (operand) should only contain digits. Otherwise, the function will return: `'Error: Numbers must only contain digits.'`
  * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: `'Error: Numbers cannot be more than four digits.'`

If the user supplied the correct format of problems, the conversion you return will follow these rules:
  * There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
  * Numbers should be right-aligned.
  * There should be four spaces between each problem.
  * There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

[Learn Regular Expressions by Building a Password Generator](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/7_password_generator.py)  
[Learn Algorithm Design by Building a Shortest Path Algorithm](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/8_shortest_path.py)  
[Learn Recursion-by Solving the Tower of Hanoi Puzzle](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/9_recursive_hanoi.py)  
[Learn Data Structures By Building the Merge Sort Algorithm](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/10_merge_sort.py)  

### [Certification Project: Build a Time Calculator Project](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/11_cert_time_calculator.py)  
Python script that takes a start time in the 12-hour clock format (ending in AM or PM) and a duration time that indicates the number of hours and minutes,
adds them and return the results. The function can optionally take a day of the week as a third parameter and, when this is given, the output should display
the day of the week of the result.  

[Learn Classes and Objects by Building a Sudoku Solver](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/12_sudoku_solver.py)  
[Learn Tree Traversal by Building a Binary Search Tree](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/13_binary_search_tree.py)  

### [Certification Project: Build a Budget App Project](https://github.com/giuseppedebiase/Scientific_Computing_with_Python/blob/main/Projects/14_cert_budget_app.py)
