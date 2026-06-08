def calculate_average(numbers):
    """Calculate the average of a list of numbers.

    Returns None for an empty list to avoid ZeroDivisionError.
    """
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]

    try:
        return total / len(numbers)
    except ZeroDivisionError:
        print("Warning: Cannot calculate average of an empty list.")
        return None


def get_list_element(my_list, index):
    """Return the element at the given index from my_list.

    Handles IndexError and TypeError gracefully and returns None on error.
    """
    if not isinstance(my_list, list):
        print("Error: Provided value is not a list.")
        return None

    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
        return None


if __name__ == "__main__":
    # Examples for calculate_average
    data1 = [10, 20, 30]
    data2 = [5, 7, 9, 11]
    data3 = []

    print("Testing calculate_average:")
    print(f"data1: {data1} -> average: {calculate_average(data1)}")
    print(f"data2: {data2} -> average: {calculate_average(data2)}")
    print(f"data3: {data3} -> average: {calculate_average(data3)}")
    print()

    # Examples for get_list_element
    sample_list = ["apple", "banana", "cherry"]
    print("Testing get_list_element:")
    print(f"Valid index 1: {get_list_element(sample_list, 1)}")
    print(f"Out-of-bounds index 5: {get_list_element(sample_list, 5)}")
    print(f"Incorrect type input: {get_list_element('not a list', 0)}")
