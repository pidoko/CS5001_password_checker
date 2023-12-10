# Final Project Report

* Student Name: Peter Idoko
* Github Username: pidoko
* Semester: Fall 2023
* Course: CS 5001

## Description 
I created a password generator that supports user or automatic generation. For the automatic generator the passwords have a minimum of 12 characters, and for the user generated passwords there are multiple checks to ensure a minimum entropy of 72.

I completed this project because I use 1Password everyday and I am interested in how they created their password generator feature.

## Key Features
Key features include a check against a password dictionary containing 1 million of the most common online passwords to ensure that the user does not create one of those passwords. 

Another feature is the entropy calculation provided at the end which is a measure of the password complexity based on the number of permutations. Also, there is another calculation for the estimated time to crack the password using a brute-force algorithm that completes password attemps at a frequency of 3.5GHz.

There are six checks when the user is typing their password to ensure that they create a password of at least an entropy of 72. These checks are for the lack of uppercase letters, lowercase letters, numbers, special characters, minimum length of 12, and uniqueness. 

## Guide
To run the project using Visual Studio, open the generator file, then hit Run at the top of the screen or right-click the generator.py file in the explorer pane and select "Run in interactive mode". Then, following the terminal prompts type and hit Return to interact with the program.

## Installation Instructions
Open the CS5001_password_checker folder in Visual Studio, then run pip install -r requirements.txt in the Terminal, then right-click the driver.py file in the Explorer pane in VS Studio and select Run in Interactive Window.

## Code Review
The main function in driver.py handles the user interactions such as prompts to collect input or relay messages as shown by the input and print functions.

The generator.py file contains almost all the functions and one of highlight is clean_word which recursively removes punctuation from a word, and reduces it to lower case.

This is the string of punctuation characters to remove
```python
punctuation_set = "!#$%&'()*+,-./:;<=>?@][^_`{|}~ .— " + '"'
```
This is to recursively skip any character found in the punctuation_set variable and turn the remaining characters to lowercase.
```python
if word[0] in punctuation_set:
        return clean_word(word[1:]).casefold()  # skip word if in set
    return (word[0].casefold() + clean_word(word[1:])).casefold()
```

### Major Challenges
Key aspects I struggled on was checking whether the password typed was already in the dictionary containing one million most common passwords because I wanted to catch variations of the easy password with a check when there are no punctuations and numbers.

Also, I initially struggled on figuring out how to publish the password checker program as a web app, but with help it was solved.

## Example Runs
I documented running the project using text output.

## Testing
I created a test file for generator.py and ran tests for edge cases to ensure the code was correct. 

## Missing Features / What's Next
What I would like to do if I had the time is add a feature to generate user-friendly passwords that still meet the minimum entropy requirements such as "jumper-whole_shorts@2007" rather than "adpjg&S89*^%4".

I also would improve the Flask app so that it was a more responsive webpage to interest people about the topic of setting secure passwords.

## Final Reflection
I started off this course with uncertainty whether I could make it in an intensive programming course but the course delivery, teaching quality and university support have been great at ensuring that I understood the concepts. I learned about inclusive design in programming and the importance of starting early to consider inclusive design because typically more people benefit from these designs. I need to learn more about abstract data types so I will be revisiting those modules soon. 

Key takeaways are to keep it simple and think inclusively.