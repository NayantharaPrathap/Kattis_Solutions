def calculate_salary(dictionary, job_description):
    salary = 0
    for word in job_description.split():
        if word in dictionary:
            salary += dictionary[word]
    return salary

def main():
    # Input
    m, n = map(int, input().split())  # Number of words in the dictionary, number of job descriptions
    
    # Parse Hay Point dictionary
    hay_point_dict = {}
    for _ in range(m):
        word, value = input().split()
        hay_point_dict[word] = int(value)
    
    # Process job descriptions
    for _ in range(n):
        job_description = ''
        line = input()
        while line != '.':
            job_description += line.lower() + ' '
            line = input()
        
        # Calculate salary for the current job description
        salary = calculate_salary(hay_point_dict, job_description)
        print(salary)

if __name__ == "__main__":
    main()
