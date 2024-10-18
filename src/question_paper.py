Question 1: List Manipulation and Conditionals
You are given a list of integers. Write a function separate_and_sum(nums) that:

Separates the list into two lists: one containing all the even numbers and the other containing all the odd numbers.
Sums the values in both lists.
Returns the larger sum along with the list (even or odd) that had the larger sum.
If both sums are equal, return the even list and the sum.

For example:

python
Copy code
nums = [1, 2, 3, 4, 5, 6]
result = separate_and_sum(nums)
print(result)  # Output: ([2, 4, 6], 12)
Requirements:

Use list comprehensions for filtering even and odd numbers.
Use control flow (if, else) to determine which sum is larger.
Do not use built-in functions like sum() for the overall logic.
Question 2: String Manipulation and Loops
Write a function letter_histogram(word) that takes in a string word and returns a dictionary where the keys are the letters in the word, and the values are the number of times each letter appears.

For example:

python
Copy code
word = "banana"
result = letter_histogram(word)
print(result)  # Output: {'b': 1, 'a': 3, 'n': 2}
Then write another function max_frequency_letter(word) that:

Uses the letter_histogram() function to get the frequency of each letter.
Returns the letter that appears the most times in the string.
For example:

python
Copy code
word = "banana"
result = max_frequency_letter(word)
print(result)  # Output: 'a'
Requirements:

Use a loop to count the frequency of each character.
Use a dictionary to store and look up frequencies.
Implement logic to find the most frequent letter.
Question 3: Functions and Recursion
Write a recursive function reverse_string(s) that takes in a string s and returns the string in reverse order.

For example:

python
Copy code
s = "hello"
result = reverse_string(s)
print(result)  # Output: "olleh"
Then, extend this into a function is_palindrome(s) that checks if a given string is a palindrome (reads the same backward and forward) using recursion.

For example:

python
Copy code
s = "racecar"
result = is_palindrome(s)
print(result)  # Output: True
Requirements:

Avoid using Python slicing techniques for reversing the string.
Use recursion for both reversing and checking palindromes.
Question 4: Dictionary Operations and Looping
You are given a dictionary that contains the names of students as keys and their respective marks in various subjects as values in the form of another dictionary. Write a function calculate_average_marks(students) that:

Calculates the average marks for each student.
Returns a dictionary where the key is the student's name and the value is their average mark.
For example:

python
Copy code
students = {
    "Alice": {"Math": 80, "English": 75, "Science": 90},
    "Bob": {"Math": 70, "English": 85, "Science": 75},
    "Charlie": {"Math": 95, "English": 60, "Science": 85}
}
result = calculate_average_marks(students)
print(result)  
# Output: {"Alice": 81.67, "Bob": 76.67, "Charlie": 80.0}
Then, write another function top_student(students) that:

Uses the calculate_average_marks() function to determine the student with the highest average.
Returns the name of the top student.
For example:

python
Copy code
result = top_student(students)
print(result)  # Output: "Alice"
Requirements:

Use loops to traverse nested dictionaries.
Handle floating-point arithmetic for averaging the marks.
Notes:
Question 1 tests knowledge of list manipulation, conditionals, and logic.
Question 2 emphasizes string operations, dictionary usage, and loops.
Question 3 focuses on recursion and string manipulation logic.
Question 4 dives deep into dictionary operations, nested data structures, and problem-solving.
These questions are designed to be more challenging and align with intermediate/advanced topics, pushing you to think critically about Python data structures, control flow, recursion, and functional programming.
