def get_cost_dict(costs_file_path: str) -> dict:
    """
    Given path to costs data file will return a dictionary
    with phone number prefix, cost pair

    Params:
    costs_file_path: path to file (string)
    """
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
    """
    Returns cost of calling given number.
    If the number is not found, returns 0.0

    Params:
    costs_dict: dictionary containing phone number prefix, costs
    key value pair

    number: phone number that will be searching for cost for
    """
    while number not in costs_dict and len(number) > 0:
        number = number[:-1]

    return float(costs_dict[number]) if len(number) > 0 else 0.0


def get_all_costs(costs_dict, input_file_path: str, output_file_path: str):
    """
    Will return costs for all phone numbers in input file

    Params:
    costs_dict: dictionary containing number prefix, cost data

    input_file_path: path to input file with valid phone numbers (string)
    # Format (+1913123434)

    output_file_path: path to to file where outputted phonenumber, cost
    data will be written
    """

    with open(input_file_path) as f:
        test_numbers = f.read().splitlines()

    with open(output_file_path, 'w') as out:
        for number in test_numbers:
            cost = search_number(costs_dict, number)
            out.write(f'{number},{cost}\n')


if __name__ == '__main__':
    from stopwatch import StopWatch
    watch = StopWatch()

    watch.mark("Compiling 10,000,000 route costs into dictionary:")
    costs_dict = get_cost_dict("data/route-costs-10000000.txt")

    watch.mark("Getting costs for 1,000 numbers and storing in results file:")
    get_all_costs(costs_dict,
                  'data/phone-numbers-1000.txt',
                  'data/results-2.txt')
    watch.end()
