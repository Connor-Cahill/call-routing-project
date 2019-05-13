#!python

from trie import Trie
import datetime
import pickle
from stopwatch import StopWatch

stopwatch = StopWatch()


def clean_input(phone_number: str) -> str:
    pass


def find_call_cost(phone_numbers: [str], trie: Trie) -> [str]:
    """
    Given a list of phone numbers that
    """
    costs_list = []
    # iterate over phone numbers
    # running trie search command on each one
    # append the cost returned from search class into cost list
    for number in phone_numbers:
        num = number[1:]
        cost = trie.search(num)
        costs_list.append(cost)

    return costs_list


def build_cost_trie(data_file_path: str) -> Trie:
    """
    Given path to data file will return a trie
    with cost of prefix
    """
    # get number prefixes and costs from
    #lines = numbers_and_costs_from(data_file_path)

    trie = Trie()
    # iterates through list of phone number prefixes
    # inserting them into our trie
    # line contains cost and phone number

    stopwatch.mark("Tokenizing input")
    with open(data_file_path, 'r') as f:
        lines = (l.split(',') for l in f.readlines())

    stopwatch.mark("Building cost trie")
    for num, cost in lines:
        trie.insert(num[1:], float(cost))

    return trie


if __name__ == '__main__':

    data_file_path = 'data/route-costs-10000000.txt'

    # stopwatch.mark("Starting to build trie")
    # trie = build_cost_trie(data_file_path)

    # stopwatch.mark("Starting to pickle")
    # pickle.dump(trie, open('trie.pickle', 'wb'))

    # stopwatch.mark("Reading test input numbers")

    #stopwatch.mark("Unpickling Trie:")
    trie = pickle.load(open('trie.pickle', 'rb'))

    stopwatch.mark("Reading test input")

    numbers = (number for number in open(
        'data/phone-numbers-1000.txt').readlines())

    #stopwatch.mark("Test with 1,000 numbers:")
    with open('data/results.txt', 'w') as out:
        for number in numbers:
            cost = trie.search(number)
            out.write(f'{number},{cost}\n')

    # stopwatch.end()
