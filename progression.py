from typing import List, Tuple


def get_progression_details(arr: List) -> Tuple:
    progression = set()
    added_val = None
    for x in arr:
        if x not in progression:
            progression.add(x)
        else:
            added_val = x
    max_val = max(progression)
    min_val = min(progression)
    d = int((max_val - min_val) / (len(progression) - 1))
    return min_val, max_val, d, added_val


if __name__ == "__main__":
    print(
        "Boundaries: from {} to {};\nStep: {};\nAdded value: {}".format(
            *get_progression_details([2, 4, 6, 8, 11, 4])
        )
    )
