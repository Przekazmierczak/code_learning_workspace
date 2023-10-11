import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> NVP | NVP Conj NVP | NVP Conj VP NP
NVP -> NP VP | NVP NP | NVP Adv
NP -> AdjNP | P AdjNP | Det AdjNP | P Det AdjNP | NP NP
AdjNP -> N | Adj AdjNP
VP -> V | Adv V | V Adv | V NP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # Download necessary tokenizer data
    nltk.download('punkt')

    # Get list of words
    sentence_list = nltk.word_tokenize(sentence.lower())

    # Remove any word that does not contain at least one alphabetic character
    # Iterate through words in the sentence
    for word in sentence_list:
        # Flag showing if the word contains at least one alphabetic character
        flag = False
        # Iterate through characters in the word
        for character in word:
            # If the character is the alphabetic character break loop
            if character.isalpha():
                flag = True
                break
        # If word that does not contain at least one alphabetic character remove it from sentence_list
        if flag == False:
            sentence_list.remove(word)

    return sentence_list

def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # Create an empty list for all noun phrase chunks in the sentence tree
    np_list = []
    # Get subtrees of the input tree
    subtrees = tree.subtrees()
    # Iterate through the subtrees
    for tree in subtrees:
        # Check if the label of the current subtree is "NP"
        if tree.label() == "NP":
            # Create a variable to indicate if the current subtree contains "NP" labels within itself
            contains_np = False

            # Iterate through subtrees of the current subtree
            for subtree in tree.subtrees():
                # Check if the subtree is not current tree and has a "NP" label
                if subtree != tree and subtree.label() == "NP":
                    # If yes, change contains_np to True and break out of the loop
                    contains_np = True
                    break

            # If the subtree does not contain "NP" labels within itself, add it to the np_list
            if not contains_np:
                np_list.append(tree)

    # Return the list of all noun phrase chunks in the sentence tree
    return np_list


if __name__ == "__main__":
    main()
