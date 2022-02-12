from hashlib import sha1
import numpy as np
import pandas as pd
import re

def hasher(solution):
    print(solution)
    return sha1(solution.encode("utf8")).hexdigest()

def ex1_2_1(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "7f7095dfe8b4cbb3ef5c2f85f07cc7512fa74a9b"
        else False
    )

def ex1_2_2(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "5937be735d9b8ae6b202c185d102a32fc9b9cc8c"
        else False
    )

def ex1_4_1(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "041233f9c62e5099e8a946b5e0c1102c760bd8e9"
        else False
    )

def ex1_4_2(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "11564be7063d3d78051233c77477d3e6186816ff"
        else False
    )

def ex1_4_3(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "8c320c4a6843a2f27f640afc2fa3c16b1894c53a"
        else False
    )

def ex1_4_4(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "435dd914dbd40d2c073a4bf63d5ab3f9ebe0dea9"
        else False
    )

def ex1_4_5(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "5ba00551175c8ae038f7143416fa6da642acfd6f"
        else False
    )

def ex1_4_6(solution):
    return (
        True
        if sha1(str(solution).encode("utf8")).hexdigest()
        == "99b6fb877dc6820343b4dc0eff76c1f9aae7370f"
        else False
    )



def run_all_autograded_tests(tests, results):
    with open("lab1.ipynb", encoding="utf-8") as f:
        total_autogrades = re.findall("rubric={autograde:(\d).*}", f.read())
    print(f"Autograded questions passed: {sum(results)} / {len(total_autogrades)}")
    print(
        f" Autograded points achieved: {sum([int(digit) for r, digit in zip(results, total_autogrades) if r])} / {sum([int(digit) for digit in total_autogrades])}"
    )
    if sum(results) < len(total_autogrades):
        print("")
        [
            print(f"FAILED: {test}")
            for (test, result) in zip(tests, results)
            if not result
        ]
