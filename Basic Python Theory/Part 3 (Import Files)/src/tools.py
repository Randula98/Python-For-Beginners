import random

def power(base , pow):
    answer = 1
    for index in range(pow):
        answer = answer * base

    return answer

def percentage(value , total):
    percentage = (value / total) * 100
    return percentage