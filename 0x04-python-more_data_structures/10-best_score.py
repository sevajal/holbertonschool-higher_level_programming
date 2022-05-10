#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max_score = {v: k for k, v in a_dictionary.items()}
        return max_score[max(max_score)]
    else:
        return (None)
