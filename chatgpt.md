# Chat GPT Prompts & Responses

## Anthony

Prompt:
 ```py
 def calculate_score(combination):
    """
    Calculates the score depending on the combination of 6 randomly generated numbers in a tuples
    :param combination: tuple of 6 integers representing different dice combinations
    :return: An integer representing a score
    """
    combination = Counter(combination)
 ```

Response:

```py
from collections import Counter

def calculate_score(combination):
    """
    Calculates the score depending on the combination of 6 randomly generated numbers in a tuples
    :param combination: tuple of 6 integers representing different dice combinations
    :return: An integer representing a score
    """
    counts = Counter(combination)
    score = sum(counts.keys()) * sum(counts.values())
    return score
```

Follow-up:

Can you write a python dictionary that contains the different score combinations in the game "ten thousand"?

Response:

```py
scores = {
    "1": 100,
    "5": 50,
    "3 of a kind": {
        "1": 1000,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500,
        "6": 600
    },
    "4 of a kind": {
        "1": 2000,
        "2": 400,
        "3": 600,
        "4": 800,
        "5": 1000,
        "6": 1200
    },
    "5 of a kind": {
        "1": 3000,
        "2": 600,
        "3": 900,
        "4": 1200,
        "5": 1500,
        "6": 1800
    },
    "6 of a kind": {
        "1": 4000,
        "2": 800,
        "3": 1200,
        "4": 1600,
        "5": 2000,
        "6": 2400
    },
    "straight": 1500
}
```