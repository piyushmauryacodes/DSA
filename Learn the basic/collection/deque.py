from collections import deque
# Equivalent to std::deque or LinkedList in Java. While a standard Python list is great for adding/removing from the end (O(1)), it is very slow for adding/removing from the front (O(n)). A deque allows O(1) appends and pops from both ends.
# Create a deque


line = deque(["Alice", "Bob", "Charlie"])

# Add to both ends
line.append("David")        # Adds to the right
line.appendleft("Zara")     # Adds to the left

print(line)  # Output: deque(['Zara', 'Alice', 'Bob', 'Charlie', 'David'])

# Remove from both ends
line.pop()       # Removes 'David'
line.popleft()   # Removes 'Zara'