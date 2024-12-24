import itertools

class Connection:
    def __init__(self, comp1:str, comp2:str):
        self.__computer1 = comp1
        self.__computer2 = comp2

    @classmethod
    def comp_sig(cls, comp1, comp2):
        nodes = [comp1, comp2]
        nodes.sort()
        return "-".join(nodes)


    def __contains__(self, key):
        return key in (self.__computer1, self.__computer2)


    def __str__(self):
        return f"{self.__computer1} <-> {self.__computer2}"


    def __eq__(self, other):
        return self.signature == other.signature


    @property
    def signature(self):
        return Connection.comp_sig(self.__computer1, self.__computer2)



class NetworkAnalyzer:
    def __init__(self, input_file:str):
        self.__input_file = input_file

        self.__computers = set()
        self.__connections = {}
        self.__read_input_file()


    def __read_input_file(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                # de-co
                comp1, comp2 = line.strip().split("-")
                self.__computers.add(comp1)
                self.__computers.add(comp2)
                conn = Connection(comp1, comp2)
                self.__connections[conn.signature] = conn



    def analyze(self):
        count = 0

        # All combinations of 3 computers
        combos = itertools.combinations(self.__computers, 3)

        found_sets = []
        for conn_set in combos:
            # conn_set => ('yn', 'wq', 'de')

            # All combos of each of the 3 computers
            # conns => [('ka', 'co'), ('ka', 'cg'), ('co', 'cg')]
            assert len(list(conn_set)) == 3
            conns = itertools.combinations(conn_set, 2)

            found = True
            for comps in conns:
                signature = Connection.comp_sig(comps[0], comps[1])
                if signature not in self.__connections:
                    found = False
                    break

            if found:
                lan_set = list(conn_set)
                lan_set.sort()
                found_sets.append(lan_set)

        # Find all lan sets that have a computer that start with "t"
        # t_sets = filter(lambda fset: "t" in "".join(fset), found_sets)
        # count = len(list(t_sets))

        for lan_set in found_sets:
            for comp_name in lan_set:
                if comp_name.startswith("t"):
                    count += 1
                    # Exit as soon as 1 is found, don't count any single set
                    # more than once
                    break

        return count








#
