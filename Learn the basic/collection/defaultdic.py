from collections import defaultdict

# Create a defaultdict where the default value is an empty list
grouped_items = defaultdict(list)

# We can append directly without checking if the key exists!
grouped_items["fruits"].append("apple")
grouped_items["fruits"].append("banana")
grouped_items["veggies"].append("carrot")

print(grouped_items) 
# Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'veggies': ['carrot']})
