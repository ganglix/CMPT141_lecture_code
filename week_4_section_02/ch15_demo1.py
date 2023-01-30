# Demo pycharm debugger - modified function from ex 5 (with branching and function in function)
# step over, step into, variable inspection, breakpoint
def cost_phone_call(call_duration):
    """
    computes the cost of a phone call
    call_duration: length of phone call in minutes
    return: total cost of phone call after all fees applied
    """

    # base cost of call
    cost = 0.35

    if call_duration < 10:
        # compute cost of call in first ten minutes
        cost = cost + call_duration * 0.50
    else:
        # compute cost of call in first ten minutes
        cost = cost + 10 * 0.50

        # compute cost of call after first ten minutes
        # (only counts full minutes)
        remaining_duration = call_duration - 10.0
        cost = cost + remaining_duration / 1 * 0.25

    # discount from plan deducts 10% from total cost
    cost = cost * 0.9
    from be_nice import greeting
    greeting()
    return cost


# test case
inputs = 11.15
expected_outputs = 5.04

bill = cost_phone_call(inputs)
if bill != expected_outputs:
    print(f"Fault found!, input: {inputs}, expected: {expected_outputs}, got: {bill}")
