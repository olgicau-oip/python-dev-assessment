def filter_and_sort_evens(numbers):
    """
    Takes a list of integers and returns a new list containing only the even numbers,
    sorted in ascending order.
    
    Args:
        numbers: A list of integers
        
    Returns:
        A sorted list of even numbers in ascending order
    """
    evens = [num for num in numbers if num % 2 == 0]
    return sorted(evens)


def count_character_frequency(text):
    """
    Takes a string and returns a dictionary with character frequencies.
    Counting is case-insensitive (e.g., 'H' and 'h' both count towards 'h').
    
    Args:
        text: A string to analyze
        
    Returns:
        A dictionary where keys are lowercase characters and values are their frequencies
    """
    frequency = {}
    for char in text.lower():
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


# Example calls to test the functions
if __name__ == "__main__":
    # Test filter_and_sort_evens
    print("Testing filter_and_sort_evens:")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = filter_and_sort_evens(numbers)
    print(f"Input: {numbers}")
    print(f"Output: {result}")
    print()
    
    # Test count_character_frequency
    print("Testing count_character_frequency:")
    text = "Hello World"
    result = count_character_frequency(text)
    print(f"Input: {text}")
    print(f"Output: {result}")
