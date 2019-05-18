#!python

from trie import Trie
import datetime
import pickle
from stopwatch import StopWatch

stopwatch = StopWatch()


def find_call_cost(phone_numbers: [str], trie: Trie) -> [str]:
    """
    Given list of phone numbers and trie will return
    list of costs for calling numbers

    Params:
    phone_numbers: array of strings that are phone numbers
    phone number format --> +19131232342

    trie: a trie containing phone number prefix, cost data
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

    Params:
    data_file_path: string of path to file with
    phone number prefix, cost data
    """
    # get number prefixes and costs from
    # lines = numbers_and_costs_from(data_file_path)

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
    print("This should take roughly a minute...")

    # =============== Uncomment to benchmark building the trie =============
    #
    # stopwatch.mark("Starting to build trie")
    # trie = build_cost_trie(data_file_path)
    #
    # stopwatch.mark("Starting to pickle")
    # pickle.dump(trie, open('trie.pickle', 'wb'))
    #
    # ======================================================================

    stopwatch.mark("Unpickling Trie:")
    trie = pickle.load(open('trie.pickle', 'rb'))

    stopwatch.mark("Reading 10,000 phone numbers from file:")
    phone_numbers = open("data/phone-numbers-10000.txt").read().splitlines()

    stopwatch.mark(f"Getting costs for {len(phone_numbers)} phone numbers:")
    find_call_cost(phone_numbers, trie)

    # ===== Uncomment to benchmark writing the costs to results file =======
    #
    # with open('data/results-3.txt', 'w') as out:
    #     numbers = (number for number in open(
    #         'data/phone-numbers-10000.txt').read().splitlines())
    #     for number in numbers:
    #         cost = trie.search(number)
    #         out.write(f'{number},{cost}\n')
    #
    # ======================================================================

    stopwatch.end()  # Can whoever grades this help me figure out why my stopwatch
    # output is delayed until the whole program is finished ??? I programmed it to
    # print during each mark's execution :(
