from bisect import bisect_left, bisect_right

def card_count_in_ranges():
    # Read the number of cards
    n = int(input().strip())
    
    # Read the card values and sort them for efficient range querying
    cards = list(map(int, input().strip().split()))
    cards.sort()
    
    # Read the number of queries
    q = int(input().strip())
    
    # Process each query
    results = []
    for _ in range(q):
        a, b = map(int, input().strip().split())
        
        # Use binary search to find the count of cards in the range [a, b]
        left_index = bisect_left(cards, a)
        right_index = bisect_right(cards, b)
        
        # The number of cards in the range [a, b] is the difference of indices
        count = right_index - left_index
        results.append(count)
    
    # Output all results, one per line
    print("\n".join(map(str, results)))

# Call the function to execute
card_count_in_ranges()
