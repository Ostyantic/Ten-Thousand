# Chat GPT Prompts & Responses

## Danner prompts & results

> **Question:** 
> how to create a counter from this score combination when the integers will be in a list 

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
    "straight": 1500 }

```py
def count_score(dice):
    counter = 0
    if sorted(dice) == [1, 2, 3, 4, 5, 6]:
        counter += scores["straight"]
        return counter
    for key in ["6 of a kind", "5 of a kind", "4 of a kind", "3 of a kind"]:
        for value in dice:
            if dice.count(value) >= int(key[0]):
                counter += scores[key][str(value)]
                dice = [x for x in dice if x != value]
                if key == "6 of a kind":
                    dice = []
                break
    for value in dice:
        counter += scores[str(value)]
    return counter
```
