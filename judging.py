def max_consistent_results(n, domjudge_results, kattis_results):
    consistent_count = 0
    domjudge_count = {}
    kattis_count = {}
    
    # Count the frequency of each result in both systems
    for result in domjudge_results:
        domjudge_count[result] = domjudge_count.get(result, 0) + 1
    
    for result in kattis_results:
        kattis_count[result] = kattis_count.get(result, 0) + 1
    
    # Iterate through the results and find the maximum consistent count
    for result in domjudge_count:
        consistent_count += min(domjudge_count[result], kattis_count.get(result, 0))
    
    return consistent_count

def main():
    n = int(input())  # Number of submissions
    
    # Read DOMjudge results
    domjudge_results = [input() for _ in range(n)]
    
    # Read Kattis results
    kattis_results = [input() for _ in range(n)]
    
    # Calculate the maximum number of consistent results
    max_consistent = max_consistent_results(n, domjudge_results, kattis_results)
    
    print(max_consistent)

if __name__ == "__main__":
    main()
