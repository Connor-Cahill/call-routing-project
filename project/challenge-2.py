def get_cost_dict(costs_file_path):
    with open(costs_file_path, 'r') as f:
        numbers_costs = (l.split(',') for l in f.read().splitlines())
    costs = {}
    for number, cost in numbers_costs:
        if number in costs:
            if cost > costs[number]:
                continue  # Don't reassign to greater cost

        costs[number] = cost
    return costs


def search_number(costs_dict: dict, number: str) -> float:
    """Returns cost of calling given number. If the number is not found, returns 0.0"""
    while number not in costs_dict and len(number) > 0:
        number = number[:-1]

    return float(costs_dict[number]) if len(number) > 0 else 0.0


def get_all_costs(costs_dict, input_file_path: str, output_file_path: str):

    test_numbers = open(input_file_path).read().splitlines()

    with open(output_file_path, 'w') as out:
        for number in test_numbers:
            cost = search_number(costs_dict, number)
            out.write(f'{number},{cost}\n')


if __name__ == '__main__':
    costs_dict = get_cost_dict("data/route-costs-10000000.txt")
    get_all_costs(costs_dict,
                  'data/phone-numbers-1000.txt',
                  'data/results-2.txt')
