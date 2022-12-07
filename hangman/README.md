# Hangman

You have a list of words and select one for each round. You provide dashes like this (_ _ _ _ _ _).

The number of dashes should equal the number of letters in the selected word.

Allow the user to guess the word letter by letter.

The user has 6 opportunities. When a user enters a letter from the word, you display the location in the word where the character can be located (e.g. If the word is banana and the user typed "a," the output should be something like this _ a _ a _ a).

But if it isn't in the word, you reduce the user's chances by 1 until the user has no chances left.

## Recommendations
- Employ the concepts of functions
- Use Python language