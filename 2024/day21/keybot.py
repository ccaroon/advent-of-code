class KeyBot:

    ACTIVATE_KEY = "A"

    DIRECTION = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }

    def __init__(self, uid, keypad, **kwargs):
        self.__uid = uid
        self.__keypad = keypad

        start_key = kwargs.get("start_key", self.ACTIVATE_KEY)
        self.__arm_positon = self.__keypad.position(start_key)

        self.__linked_bot = None


    @property
    def uid(self):
        return self.__uid


    @property
    def keypad(self):
        return self.__keypad


    def __str__(self):
        key = self.__keypad.key(self.__arm_positon)
        output = f"{self.uid}->[{self.__keypad}]: {self.__arm_positon} <{key}>"
        return output


    def show_links(self) -> str:
        output = ""
        if self.__linked_bot:
            output = "-> " + str(self.__linked_bot)

        key = self.__keypad.key(self.__arm_positon)
        output = f"{self.uid}[{self.__keypad}]<{key}> {output}"

        return output


    def link(self, other_bot):
        """
        Link this Keybot's key presses to another Keybot
        """
        self.__linked_bot = other_bot
        self.__keypad.connect_to(other_bot)


    def input(self, key:str):
        result = None
        if key == self.ACTIVATE_KEY:
            result = self.activate()
        else:
            self.move(key)

        return result


    def move(self, arrow):
        direction = self.DIRECTION.get(arrow)

        new_pos = (
            self.__arm_positon[0] + direction[0],
            self.__arm_positon[1] + direction[1]
        )

        # old_key = self.__keypad.key(self.__arm_positon)
        # new_key = self.__keypad.key(new_pos)

        # print(f"{self.uid} move from {self.__arm_positon}<{old_key}> to {new_pos}<{new_key}>")

        self.__arm_positon = new_pos

        if not self.__keypad.key(self.__arm_positon):
            raise RuntimeError(f"Panic! Don't Panic! Wait! Panic!? GOTO 1? Core Dump//Meltdown.%$#$^?...--(Return, Return, Return) Dive! Dive! Dive! GO-SUB...Error____0xDEADBEEF!")


    def activate(self):
        """ Press the Key under the Bot's Arm Position """
        key = self.__keypad.key(self.__arm_positon)
        # print(f"{self.uid} -> {key}")
        return self.__keypad.press(key)




#
