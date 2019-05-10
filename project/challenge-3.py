#!python

from trie import Trie


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
    with open(data_file_path) as file:
        lines = file.read().splitlines()

    trie = Trie()
    # iterates through list of phone number prefixes
    # inserting them into our trie
    # line contains cost and phone number
    for line in lines:
        num, cost = line.split(',')
        print(num)
        trie.insert(num[1:], cost)

    print('BELOW IS THE GOODS')
    print(trie)
    return trie


if __name__ == '__main__':
    with open('../data/route-costs-100.txt') as file:
        phone_numbers = [line.split(',')[0] for line in file.read().splitlines()]
    trie = build_cost_trie('../data/route-costs-100.txt')
    print(trie)
    print(find_call_cost(phone_numbers, trie))

