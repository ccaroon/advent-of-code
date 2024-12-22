class KeyPad:

    LAYOUT_NUMERIC = (
        ("7", "8", "9"),
        ("4", "5", "6"),
        ("1", "2", "3"),
        ("",  "0", "A")
    )

    LAYOUT_DIRECTIONAL = (
        ("",  "^", "A"),
        ("<", "v", ">")
    )


    def __init__(self, layout):
        self.__layout = layout
        self.__receiver = None


    def __str__(self):
        output = ""
        if self.__layout == self.LAYOUT_DIRECTIONAL:
            output = "D-PAD"
        elif self.__layout == self.LAYOUT_NUMERIC:
            output = "N-PAD"
        else:
            output = "Un-Known"

        return output


    def visual_layout(self) -> str:
        output = "+---+---+---+\n"
        for row in self.__layout:
            for col in row:
                output += f"| {col} "

            output += "|\n"
            output += "+---+---+---+\n"

        return output


    def position(self, key:str):
        """
        Get the position (r,c) of the given `key`
        """
        pos = None
        for ridx, row in enumerate(self.__layout):
            if key in row:
                cidx = row.index(key)
                pos = (ridx, cidx)
                break

        return pos


    def key(self, pos):
        """
        Get the key at the given postion(r,c)
        """
        return self.__layout[pos[0]][pos[1]]


    def connect_to(self, other):
        self.__receiver = other


    def press(self, key:str):
        result = key
        if self.__receiver:
            # print(f"Sending '{key}' to {self.__receiver}...")
            result = self.__receiver.input(key)
        # else:
        #     result = key
        #     print(f"'{key}'")

        return result




#
