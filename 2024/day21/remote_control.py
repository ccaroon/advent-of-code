from keybot import KeyBot
from keypad import KeyPad

class RemoteControl:
    def __init__(self, input_file:str):
        self.__input_file = input_file
        self.__codes = []

        self.__read_codes()

        self.__keybots = []
        self.__init_keybots()

        self.__keypad = None
        self.__init_user()


    def __read_codes(self):
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                self.__codes.append(line.strip())


    def __init_keybots(self):
        # C3-PO | MurderBot | R2-D2 | K-9
        arrow_bot1 = KeyBot(
            "Marvin",
            KeyPad(KeyPad.LAYOUT_DIRECTIONAL), start_key="A")
        # print(arrow_bot1)
        arrow_bot2 = KeyBot(
            "UnCharles",
            KeyPad(KeyPad.LAYOUT_DIRECTIONAL), start_key="A")
        # print(arrow_bot2)
        door_bot = KeyBot(
            "Kryten",
            KeyPad(KeyPad.LAYOUT_NUMERIC), start_key="A")
        # print(door_bot)

        arrow_bot1.link(arrow_bot2)
        arrow_bot2.link(door_bot)

        self.__keybots = (
            arrow_bot1,
            arrow_bot2,
            door_bot
        )


    def __init_user(self):
        # Directional KeyPad that user (ME) is controlling
        self.__keypad = KeyPad(KeyPad.LAYOUT_DIRECTIONAL)
        # Link user (MY) KeyPad to the first KeyBot
        self.__keypad.connect_to(self.__keybots[0])


    def __str__(self):
        return f"User[{self.__keypad}] -> {self.__keybots[0]} => {self.__codes}"


    @property
    def codes(self):
        return self.__codes


    def press(self, key:str):
        return self.__keypad.press(key)


    def systems_test(self):
        # Test Sequences
        test_seqs = {
            # "9": "v<<A>>^AAAvA^A",
            "029A": "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
            "980A": "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
            "179A": "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
            "456A": "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
            "379A": "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
        }

        # Enter Sequence
        for code, seq in test_seqs.items():
            key_presses = list(seq)
            result = ""
            for key in key_presses:
                what = self.press(key)
                if what is not None:
                    result += what

            assert result == code, f"Result [{result}] should match [{code}]"


    def enter_codes(self):
        sequences = []


        return sequences










#
