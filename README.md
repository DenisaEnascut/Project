# Project 

# Problem 1 

# Text Processing and Sum Calculation Program

This program takes input text and performs a series of steps to calculate a final sum according to a specific algorithm. The algorithm consists of the following steps:

1. Conversion of uppercase letters to lowercase.
2. Removal of forbidden characters, retaining only lowercase letters, digits, and spaces.
3. Calculation of the frequency of unique characters in the text and sorting them in descending order of frequency.

After these steps are applied, the final sum is calculated as follows:
For each character in the text, its initial position in the unfiltered text is obtained. The index of the character is found in the sorted character list, and the initial position plus the found index is added to the total sum.

## How to Use the Program

1. Modify the `text` variable in the code with the text you want to process.
2. Run the program to obtain the result of processing the text.
3. The result will be displayed in the console.

## Example

Input text: "admitere Facultate Automatica si Calculatoare 2023"
Obtained result: 860

This example illustrates how the final sum is calculated based on the given text according to the specified algorithm.



# Problem 2


# Number to Words Conversion Program

This program converts positive integers into their word representation in Romanian, providing a human-readable format for numbers. It breaks down the number into groups of three digits, such as thousands, millions, billions, etc., and converts each group into words.

## How the Program Works

The program uses dictionaries to map digits and group names to their corresponding words in Romanian. It follows these steps to convert a number:

1. **Initialization:** Define dictionaries for digits (0-9) and group names (e.g., million, billion) in Romanian.

2. **Group Conversion:** The `converteste_mii` function converts a three-digit group into words, considering hundreds, tens, and units. It handles special cases for certain numbers (e.g., "o" for 1, "un" for 1, "două" for 2). It also considers conjunctions and agreements for correct grammar.

3. **Main Conversion Loop:** The main loop divides the input number into groups of three digits each. For each group, it converts the group into words using `converteste_mii`. It adds the group name to the result, taking into account plural forms and agreement based on the group index.

4. **Result:** The final word representation is constructed by combining the converted groups and their respective group names.

## How to Use the Program

1. Modify the `numar` variable in the code with the positive integer you want to convert.
2. Run the program to obtain the word representation of the number.
3. The result will be displayed in the console.

## Example

Number: 59876
Word Representation: "cincizeci și nouă mii opt sute șaptezeci și șase"

This example demonstrates how the program converts the given number into its word representation in Romanian.

## Considerations

- The program only works with positive integers.
- Make sure to modify the `numar` variable to test with different numbers.
- The program may not cover all specialized cases of the Romanian language and number naming.

Feel free to modify and adapt the code for your specific use case or language requirements.

