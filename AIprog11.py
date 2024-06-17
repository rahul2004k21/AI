from constraint import Problem, AllDifferentConstraint

def map_coloring():
    problem = Problem()

    variables = ['WA', 'NT', 'SA', 'QL', 'NSW', 'VIC', 'TAS']
    colors = ['red', 'green', 'blue']

    for variable in variables:
        problem.addVariable(variable, colors)

    problem.addConstraint(AllDifferentConstraint(), variables)
    problem.addConstraint(lambda wa, nt: wa != nt, ('WA', 'NT'))
    problem.addConstraint(lambda wa, sa: wa != sa, ('WA', 'SA'))
    problem.addConstraint(lambda nt, sa: nt != sa, ('NT', 'SA'))
    problem.addConstraint(lambda nt, ql: nt != ql, ('NT', 'QL'))
    problem.addConstraint(lambda nt, sa: nt != sa, ('NT', 'SA'))
    problem.addConstraint(lambda sa, ql: sa != ql, ('SA', 'QL'))
    problem.addConstraint(lambda sa, nsw: sa != nsw, ('SA', 'NSW'))
    problem.addConstraint(lambda sa, vic: sa != vic, ('SA', 'VIC'))
    problem.addConstraint(lambda nsw, ql: nsw != ql, ('NSW', 'QL'))
    problem.addConstraint(lambda nsw, vic: nsw != vic, ('NSW', 'VIC'))

    solution = problem.getSolution()
    return solution

if __name__ == "__main__":
    solution = map_coloring()
    print("Map Coloring Solution:")
    for region, color in solution.items():
        print(f"{region}: {color}")
