#Criteria 8
# We need to test 2 paths : one for which all the conditions are True and another for which all the conditions are wrong

import sys
sys.path.insert(0,sys.path[0][:len(sys.path[0])-12])

from Control_Graphs.CG_Project_Example import CG_Project_Example
from control_graph import apply_path, find_vertice_with_label, Graph
from test_generation import test_generation

def all_conditions(CG, L, T):
    """The arguments are a control graph (CG), the list of paths that should 
    be visited to validate the criteria (L),and a data set of variables(T). It 
    checks if the criteria all_conditions is validated."""
    to_visit = list(L)
    not_visited = list(L)
    for t in T:
        p = apply_path(CG, t)[0]
        if p in not_visited:
            not_visited.remove(p)
    Graph.coverage_criteria2(to_visit, "not_visited", not_visited)
    if not_visited:
        print('test failed')
    else:
        print('test passed')



def all_conditions_passed(CG):
    """A specific data set that validates the criteria"""
    T = [
        {'X':-1},
        {'X':10}
        ]
    
    L = [[1,2,4,5,"exit"], [1,3,4,6,"exit"]]

    all_conditions(CG, L, T)

def all_conditions_failed(CG):
    """A specific data set that invalidates the criteria"""
    #A requirement to pass the test is to have X=-1 as initial value
    T = [
        {'X':-5}
        ]

    L = [[1,2,4,5,"exit"], [1,3,4,6,"exit"]]

    all_conditions(CG, L, T)

def generate_data_set(CG):
    L = [[1,2,4,5,"exit"], [1,3,4,6,"exit"]]
    for path in L:
        print(test_generation(CG,path))

if __name__=="__main__":
    print("Criteria 1 - all assigned")
    print("Control Graph is CG_Project_Example")
    print("\n")
    CG1 = CG_Project_Example()
    CG2 = CG_Project_Example()  
    all_conditions_passed(CG1)
    print("\n")
    all_conditions_failed(CG2)
    print("\n")
    print("Automatic generation of data set that validate the criteria:")
    generate_data_set(CG1)

    
