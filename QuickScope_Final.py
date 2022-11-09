#QuickScope Final Solution
from dataclasses import dataclass
from collections import defaultdict

@dataclass
class Var:
    
    type: str
    depth: str
    name: str

class MultipleDecExcept(Exception):
    pass

def solution(n):
    full_v = defaultdict(list)
    for_all = defaultdict(lambda: "UNDECLARED")
    v_depth = defaultdict(list)
    depth = 0
    for x in range(n):
        command = input().split()
        if command[0] == "TYPEOF":
            v = command[1]
            print(get_type(v, for_all))
        elif command[0] == "DECLARE":
            v, type = command[1:]
            for_all[v] = type
            
            try:
                add_variable(v, type, depth, full_v, v_depth)
            except MultipleDecExcept:
                print("MULTIPLE DECLARATION")
                return
            
        elif command == ["{"]:
            depth += 1
        elif command == ["}"]:
            closed_scope(depth, for_all, full_v, v_depth)
            depth -= 1


def get_type(v, for_all):
    return for_all[v]


def add_variable(v, type, depth, full_v, v_depth):
    if full_v[v]:
        if full_v[v][-1].depth is depth:
            raise MultipleDecExcept()
    full_v[v].append(Var(name=v, type=type, depth=depth))
    v_depth[depth].append(v)


def closed_scope(depth, for_all, full_v, v_depth):
    for v in v_depth[depth]:
        val = full_v[v]
        val.pop()
        for_all[v] = val[-1].type if val else "UNDECLARED"
        full_v[v] = val
    v_depth[depth] = []


if __name__ == "__main__":
    n = int(input())
    solution(n)
