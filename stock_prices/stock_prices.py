#!/usr/bin/python
#
# For this problem, we essentially want to find the maximum difference between the smallest
# and largest prices in the list of prices, but we also have to make sure that the max
# profit is computed by subtracting some price by another price that comes _before_ it;
#  it can't come after it in the list of prices.

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?
import argparse

# Store first entry as best possible check each item as loop and update if better


def find_max_profit(prices):
    current_min_price_so_far = min(prices[1], prices[0])
    max_profit_so_far = prices[1] - prices[0]
    loops = 0
    for price in range(1, len(prices) - 1):
        loops += 1

        current_price = prices[price]
        if max_profit_so_far < 0 and loops <= 1:
            max_profit_so_far = min(
                max_profit_so_far, current_price - current_min_price_so_far)
        else:
            max_profit_so_far = max(
                max_profit_so_far, current_price - current_min_price_so_far)
            current_min_price_so_far = min(
                current_min_price_so_far, current_price)
    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
