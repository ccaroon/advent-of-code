from invoke import task

from garden import Garden

@task
def part1(ctx, input_file="garden-plot.map"):
    """Day 12 // Part 01"""

    print(part1.__doc__)

    garden = Garden(input_file)
    fencing_cost = garden.calculate_fencing()

    print(f"""
-> Input File: {input_file}
-> Plant Types: {garden.plant_types}
-> Regions: {len(garden.regions)}
-> Fencing Cost: ${fencing_cost}
""")


@task
def part2(ctx, input_file="garden-plot.map", debug=False):
    """Day 12 // Part 02"""

    print(part2.__doc__)

    garden = Garden(input_file, debug=debug)
    fencing_cost = garden.calculate_fencing(with_discount=True)


    print(f"""
-> Input File: {input_file}
-> Plant Types: {garden.plant_types}
-> Regions: {len(garden.regions)}
-> Fencing Cost: ${fencing_cost}
""")
