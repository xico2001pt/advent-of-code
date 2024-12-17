import time


def measure_time(func, *args, **kwargs):
    """
    Measures the execution time of a function.

    Args:
        func (callable): The function to measure.
        *args: Positional arguments for the function.
        **kwargs: Keyword arguments for the function.

    Returns:
        tuple: A tuple containing the result of the function and the execution time.
    """
    start_time = time.time()
    result = func(*args, **kwargs)  # Execute the function with provided arguments
    end_time = time.time()
    elapsed_time = end_time - start_time

    return result, elapsed_time
