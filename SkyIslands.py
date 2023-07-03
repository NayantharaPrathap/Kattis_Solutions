#Sky Islands
#N = # islands or nodes
#M = # bridges or paths
islands = []

def main():
    inp = input().split(" ")
    islands = [i for i in range((int)(inp[0])+1)]
    
    # Returns the root and compresses the entire path
    def _find(visited, val): 
        # Cycle back or already root
        if islands[val] != val or val in visited:
            islands[val] = _find(visited, islands[val])
        visited += [val]
        return islands[val]

    bridges = (int)(inp[1])
    for i in range(bridges):
        inp = input().split(" ")
        first, second = (int)(inp[0]),(int)(inp[1])
        # Trying to make sure links aren't overwritten
        old_root = _find([], islands[first])
        islands[first] = _find([], islands[second])
        islands[old_root] = islands[first]

    root = _find([], 1)
    separate = [str(i) for i in range(1, len(islands)) if not _find([], i) == root]
    if not separate:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
