def doorbell_system():
    # Read the number of residents who are home
    n = int(input().strip())
    
    # Dictionary to store residents' names
    residents = {}
    
    # Read the residents' names and store them in the dictionary
    for _ in range(n):
        full_name = input().strip().split()
        # Add to the dictionary with the first name as key and the full name as value
        residents[full_name[0]] = ' '.join(full_name)
    
    # Read the number of queries
    q = int(input().strip())
    
    # Process each query
    for _ in range(q):
        query_name = input().strip()
        if query_name in residents:
            full_name = residents[query_name]
            if len(full_name.split()) == 1:
                # If only one given name, respond with 'Jebb'
                print("Jebb")
            else:
                # If two given names, respond with the corrected full name
                print(f"Neibb en {full_name} er heima")
        else:
            # If the resident is not home, respond with 'Neibb'
            print("Neibb")

# Execute the function
doorbell_system()
