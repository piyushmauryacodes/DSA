from collections import deque

# Create a deque
line = deque(["Alice", "Bob", "Charlie"])

# Add to both ends
line.append("David")        # Adds to the right
line.appendleft("Zara")     # Adds to the left

print(line)  # Output: deque(['Zara', 'Alice', 'Bob', 'Charlie', 'David'])

# Remove from both ends
line.pop()       # Removes 'David'
line.popleft()   # Removes 'Zara'