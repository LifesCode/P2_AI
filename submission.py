import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple

############################################################
# Custom Types
# NOTE: You do not need to modify these.

"""
You can think of the keys of the defaultdict as representing the positions in
the sparse vector, while the values represent the elements at those positions.
Any key which is absent from the dict means that that element in the sparse
vector is absent (is zero).
Note that the type of the key used should not affect the algorithm. You can
imagine the keys to be integer indices (e.g., 0, 1, 2) in the sparse vectors,
but it should work the same way with arbitrary keys (e.g., "red", "blue", 
"green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]


############################################################
# Problem 4a

def find_alphabetically_first_word(text: str) -> str:
    """
    Given a string |text|, return the word in |text| that comes first
    lexicographically (i.e., the word that would come first after sorting).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() handy here. If the input text is an empty string, 
    it is acceptable to either return an empty string or throw an error.
    """
    # the string is divided into a list of components and sorted. then the firs element (index 0) is returned if the
    # argument ([text]) is not an empty string. Otherwise it returns an empty string
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return sorted(text.split(" "))[0] if text else ""
    # END_YOUR_CODE


############################################################
# Problem 4b

def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return ((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)**0.5
    # END_YOUR_CODE


############################################################
# Problem 4c
def mutate_sentences(sentence: str) -> List[str]:
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be "similar" to the original sentence if
      - it has the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the
        original sentence (the words within each pair should appear in the same
        order in the output sentence as they did in the original sentence).
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more
        than once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
                (Reordered versions of this list are allowed.)
    """
    # BEGIN_YOUR_CODE (our solution is 17 lines of code, but don't worry if you deviate from this)
    def find_all_paths2(graph, key, path, max_words, paths=[]):  # recursive search of a graph to find all sentences
        if len(path.split(" ")) == max_words + 1:  # if sentence has same word number as original, it should stop
            paths.append(path)
            return path.strip()
        path += f"{key} "  # add next word to the sentence
        for key2 in graph[key]:  # must go to all possible nodes.
            return find_all_paths2(graph, key2, path, max_words, paths)

    sentence, words = sentence.split(" "), {}  # extracting all words from sentence and initializing words dictionary
    for current_index, word in enumerate(sentence[:-1]):  # creates a dictionary where values are following nodes
        if word in words and sentence[current_index+1] not in words[word]:
            words[word].append(sentence[current_index+1])
        else:
            words[word] = [sentence[current_index+1]]
    words[sentence[-1]], paths = [] if sentence[-1] not in words.keys() else words[sentence[-1]], []
    for key in list(words.keys())[:-1]:
        if path:=find_all_paths2(words, key, "", len(sentence)):
            paths.append(path)
    return [" ".join(sentence)]+paths
    # END_YOUR_CODE


############################################################
# Problem 4d

def sparse_vector_dot_product(v1: SparseVector, v2: SparseVector) -> float:
    """
    Given two sparse vectors (vectors where most of the elements are zeros)
    |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.

    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return sum([float(v1[v1_pos]) * float(v2[v2_pos]) for v1_pos in v1.keys() for v2_pos in v2.keys() if v1_pos == v2_pos])
    # END_YOUR_CODE


############################################################
# Problem 4e

def increment_sparse_vector(v1: SparseVector, scale: float, v2: SparseVector) -> None:
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    If the scale is zero, you are allowed to modify v1 to include any
    additional keys in v2, or just not add the new keys at all.

    NOTE: This function should MODIFY v1 in-place, but not return it.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    for v1_pos in v1.keys():
        for v2_pos in v2.keys():
            if v1_pos == v2_pos:
                v2[v1_pos] = v1[v1_pos] + scale * v2[v2_pos]
            else:
                v2[v2_pos] = v2[v2_pos] * scale
    # END_YOUR_CODE


############################################################
# Problem 4f

def find_nonsingleton_words(text0: str) -> Set[str]:
    """
    Split the string |text| by whitespace and return the set of words that
    occur more than once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    return set([word for word in text0.split(" ") if text0.split(" ").count(word) > 1])
    # END_YOUR_CODE


# print(find_alphabetically_first_word("raffaele foi feito para programar"))
# print(euclidean_distance((1, 1), (10, 10)))
# print(mutate_sentences("mouse the cat and the mouse"))
# print(mutate_sentences("I know what I want"))
# print(find_nonsingleton_words("the cat and the mouse cat"))
# print(sparse_vector_dot_product(collections.defaultdict(float, {'a': 5}), collections.defaultdict(float, {'b': 2, 'a': 3})))
v = collections.defaultdict(float, {'a': 5})
print(increment_sparse_vector(v, 2, collections.defaultdict(float, {'b': 2, 'a': 3})))
