def minimum_steps_to_equalize(n, a, b):
    min_a = min(a)  # Find the minimum value in array 'a'
    steps = 0

    for i in range(n):
        # Calculate the difference required to make a[i] equal to min_a
        diff = a[i] - min_a
        
        # Check if it's possible to reduce a[i] to min_a using b[i]
        if diff % b[i] != 0:
            return -1  # Not possible to make all values equal
        
        # Add the number of steps required for this element
        steps += diff // b[i]
    
    return steps

# Input reading
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Output the result
result = minimum_steps_to_equalize(n, a, b)
print(result)
