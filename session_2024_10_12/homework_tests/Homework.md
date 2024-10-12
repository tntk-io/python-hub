# Homework Tests

Create a file for the scripts called `scripts.py` and  another one for the tests called `scripts_test.py`.
Import the `script` module in `scripts_test.py`.

## Reverse List

Create a function called `reverse_list` which takes a list as a parameter and reverses it in place using two-pointer method.

### Testing

Create a test called `test_reverse_list` and test whether the function works as expected.
You can use [::-1] slicing for the expected result.

## Current Time

Create a function called `current_time`.
Make a request to the World Time API at https://worldtimeapi.org/api/ip.
This will return your local time based on your IP.
You can parse it as date time using the `datetime` library's `datetime` class's  `fromisoformat` function.

For simplicity, you can use UTC time (`utc_datetime` field). For getting the local time you can use `datetime.datetime.now(dt.timezone.utc)`.

Return the datetime object.

### Testing

Create a test called `test_current_time`.

Make 10 requests within a maximum of 30 seconds interval (sleep 1-3 seconds between every request made).
You can use the `time` library's `sleep` function to sleep.

Ensure that the time difference between your local date (`datetime.now()`) and the remote date is not more than 2 seconds.

## Cartesian Product

Implement a function called `cartesian` that takes two lists and returns their cartesian product
(list of tuples of all their possible permutations).

### Testing

Create a test called `test_cartesian`.

To test whether this method works you can use `product` from the `itertools` module.
The expected the result is the same as the list value of the `product` function once it's called with
the two lists passed to it.

Create two generators, the first one yields the lists and their expected result (using the product function)
in a tuple, where edge cases can be tested (e.g. empty lists, different data types mixed). The second generator
should yield 500 lists (with a length between 100 and 400, filled with random values) with their expected value.

Use these generators when you parameterize the test case.

Note that the @pytest.mark.parameterize expects one iterable, so you will have to [chain](https://docs.python.org/3/library/itertools.html#itertools.chain)
the two generators together to make it work.