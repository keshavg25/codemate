class AlgorithmTemplates:
    
    @staticmethod
    def factorial():
        return '''def factorial(n):
    """
    Calculate the factorial of a number.
    Time Complexity: O(n)
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 7: {factorial(7)}")'''
    
    @staticmethod
    def fibonacci():
        return '''def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    Time Complexity: O(n)
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq

# Example usage
print(f"First 10 Fibonacci numbers: {fibonacci(10)}")'''
    
    @staticmethod
    def palindrome():
        return '''def is_palindrome(text):
    """
    Check if a string is a palindrome.
    Time Complexity: O(n)
    """
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]

# Example usage
test_words = ["racecar", "hello", "A man a plan a canal Panama"]
for word in test_words:
    result = "✓ Palindrome" if is_palindrome(word) else "✗ Not a palindrome"
    print(f"{word}: {result}")'''
    
    @staticmethod
    def bubble_sort():
        return '''def bubble_sort(arr):
    """
    Sort array using Bubble Sort algorithm.
    Time Complexity: O(n²) - Not recommended for large datasets
    """
    n = len(arr)
    arr = arr.copy()
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example usage
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted: {sorted_arr}")'''
    
    @staticmethod
    def merge_sort():
        return '''def merge_sort(arr):
    """
    Sort array using Merge Sort algorithm.
    Time Complexity: O(n log n) - Efficient for large datasets
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example usage
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted: {sorted_arr}")'''
    
    @staticmethod
    def binary_search():
        return '''def binary_search(arr, target):
    """
    Search for target in sorted array using Binary Search.
    Time Complexity: O(log n)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage
sorted_array = [11, 12, 22, 25, 34, 64, 90]
target = 25
index = binary_search(sorted_array, target)
print(f"Array: {sorted_array}")
print(f"Searching for {target}: Found at index {index}" if index != -1 else f"Not found")'''