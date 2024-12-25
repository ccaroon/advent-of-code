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


    @property
    def nodes(self):
        return (self.__computer1, self.__computer2)


    def __contains__(self, key):
        return key in (self.__computer1, self.__computer2)


    def __str__(self):
        return f"{self.__computer1} <-> {self.__computer2}"


    def __eq__(self, other):
        return self.signature == other.signature


    # TODO: rename to id or code or ?????
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


    def __find_sets(self, size):
        # All combinations of `size` computers
        combos = itertools.combinations(
            self.__computers,
            size
        )

        found_sets = []
        count = 0
        for conn_set in combos:
            count += 1

            if count % 1_000_000 == 0:
                print(f"...{size} | {count}")
            # conn_set => ('yn', 'wq', 'de')
            # print(list(conn_set))

            # All combos of each of the 3 computers
            # conns => [('ka', 'co'), ('ka', 'cg'), ('co', 'cg')]
            # assert len(list(conn_set)) == 3
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
                print(f"...found a set [{len(found_sets)}]")
                if len(found_sets) > 1:
                    break

        return found_sets



    def decode_passwdX(self):
        passwd = ""

        largest_size = 0
        largest_set = None
        # for size in range(len(self.__computers), 0, -1):
        for size in range(0,10):
            print(f"=> Trying {size}...")
            found_sets = self.__find_sets(size)
            # print(f"Found Sets: {len(found_sets)}")

            if len(found_sets) == 1:
                if size > largest_size:
                    largest_size = size
                    largest_set = found_sets
                    break


        # Get Set of unique names
        comps = set()
        for lan_set in largest_set:
            comps.update(lan_set)

        # Convert to comma separted, sorted string
        names = list(comps)
        names.sort()
        passwd = ",".join(names)

        return passwd


    def decode_passwd(self):
        lan_sets = []
        for comp_name in self.__computers:
            lan_set = set()
            lan_set.add(comp_name)
            lan_sets.append(lan_set)
            for conn in self.__connections.values():
                if comp_name in conn:
                    lan_set.update(conn.nodes)

        # for comp_name in ("kh", "qp", "ub"):
        #     lan_set = set()
        #     lan_set.add(comp_name)
        #     lan_sets.append(lan_set)
        #     for conn in self.__connections.values():
        #         if comp_name in conn:
        #             lan_set.update(conn.nodes)

        # print(lan_sets)
        # print(len(lan_sets))

        # a = {'ta', 'ub', 'kh', 'qp', 'tc'}
        # b = {'qp', 'ub', 'wh', 'td', 'kh'}
        # c = {'qp', 'wq', 'ub', 'vc', 'kh'}

        # z = a & b & c
        # a = a.intersection(b)
        # a = a.intersection(c)
        # print(a)

        # lan_sets = [a,b,c]

        s1 = lan_sets.pop()
        for ls in lan_sets:
            s1 = s1.intersection(ls)

        print(s1)

        # s1 = lan_sets.pop()
        # ------ this -----
        # print(s1)
        # fish = s1.intersection(
        #     lan_sets[0], lan_sets[1], lan_sets[2], lan_sets[3],
        #     lan_sets[4], lan_sets[5], lan_sets[6], lan_sets[7],
        #     lan_sets[8], lan_sets[9], lan_sets[10], lan_sets[11],
        #     lan_sets[12], lan_sets[13], lan_sets[14]
        # )
        # print(fish)
        # -----------------

        # for idx in range(3):
        #     s1 = s1.intersection(lan_sets[idx])

        # for ls in lan_sets:
        #     s1.intersection_update(ls)
        # print(s1)
        # what = set()
        # what = what.intersection(lan_sets)
        # print(what)

        return "foo-bar"


    def analyze(self):
        count = 0

        # All combinations of 3 computers
        combos = itertools.combinations(self.__computers, 3)

        found_sets = []
        for conn_set in combos:
            # conn_set => ('yn', 'wq', 'de')

            # All combos of each of the 3 computers
            # conns => [('ka', 'co'), ('ka', 'cg'), ('co', 'cg')]
            # assert len(list(conn_set)) == 3
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

        for lan_set in found_sets:
            for comp_name in lan_set:
                if comp_name.startswith("t"):
                    count += 1
                    # Exit as soon as 1 is found, don't count any single set
                    # more than once
                    break

        return count
