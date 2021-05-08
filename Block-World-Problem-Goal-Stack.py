tab = []
result = []
problem = ["c", "a", "e", "d", "b"]
goalList = ["a", "b", "c", "d", "e"]

def parSolution(N):
    for i in range(N):
        if goalList[i] != result[i]:
            return False
    return True


def Onblock(index, count):

    if count == len(goalList)+1:
        return True

    block = tab[index]

    result.append(block)
    print(result)
    if parSolution(count):
        print("Valid Step - Pushing Result Soln ")
        tab.remove(block)
        Onblock(0, count + 1)
    else:
        print("Invalid Step - Back To Tab")
        result.pop()
        Onblock(index+1, count)


def Ontab(problem):

    if len(problem) != 0:
        tab.append(problem.pop())
        Ontab(problem)
    else:
        return True


def goal_stack_planing(problem):
    Ontab(problem)
    if Onblock(0, 1):
        print(result)

if __name__ == "__main__":
    
    print("Initial -> Goal")
    for k, j in zip(goalList, problem):
        print(j+"          "+k)
    goal_stack_planing(problem)
    print("\nFinal Result Solution:")
    print(result)
