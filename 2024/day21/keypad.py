class KeyPad:

    LAYOUT_NUMERIC = (
        ("7", "8", "9"),
        ("4", "5", "6"),
        ("1", "2", "3"),
        (" ", "0", "A")
    )

    LAYOUT_DIRECTIONAL = (
        (" ", "^", "A"),
        ("<", "v", ">")
    )

    def __init__(self, layout):
        self.__layout = layout
        self.__linked_pad = None


    def __str__(self) -> str:
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


    def link(self, keypad):
        self.__linked_pad = keypad


    def press(self, key):
        if self.__linked_pad:
            self.__linked_pad.press(key)
        else:
            print(f"-> {key}")







#
