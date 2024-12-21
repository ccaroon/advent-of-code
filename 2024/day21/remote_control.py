from keybot import KeyBot
from keypad import KeyPad

class RemoteControl:
    def __init__(self, input_file:str):
        self.__input_file = input_file
        self.__codes = []

        self.__read_codes()

        self.__keybots = []
        self.__init_keybots()


    def __read_codes(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                self.__codes.append(line.strip())


    def __init_keybots(self):
        # C3-PO | MurderBot | R2-D2 | K-9
        arrow_bot1 = KeyBot(
            "Marvin",
            KeyPad(KeyPad.LAYOUT_DIRECTIONAL), start_key="A")
        arrow_bot2 = KeyBot(
            "UnCharles",
            KeyPad(KeyPad.LAYOUT_DIRECTIONAL), start_key="A")
        door_bot = KeyBot(
            "Kryten",
            KeyPad(KeyPad.LAYOUT_NUMERIC), start_key="A")

        arrow_bot1.link(arrow_bot2)
        arrow_bot2.link(door_bot)

        self.__keybots = (
            arrow_bot1,
            arrow_bot2,
            door_bot
        )


    def __str__(self):
        return f"{self.__codes}"


    @property
    def codes(self):
        return self.__codes


    def enter_codes(self):
        sequences = []
        # Directional Pad that I'M controlling
        arrow_pad = KeyPad(KeyPad.LAYOUT_DIRECTIONAL)
        # Link MY pad to the first KeyBot
        arrow_pad.link(self.__keybots[0])

        print(self.__keybots[0])


        return sequences
