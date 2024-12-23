class MonkeyMarket:
    def __init__(self, input_file:str):
        self.__input_file = input_file

        self.__secret_numbers = []
        self.__read_input_file()


    def __read_input_file(self):
        self.__secret_numbers = []
        with open(self.__input_file, "r") as fptr:
            while line := fptr.readline():
                self.__secret_numbers.append(int(line.strip()))


    @property
    def secret_number_count(self):
        return len(self.__secret_numbers)


    def __mix(self, value, secret_number):
        """
        To mix a value into the secret number, calculate the bitwise XOR of the
        given value and the secret number. Then, the secret number becomes the
        result of that operation. (If the secret number is 42 and you were to
        mix 15 into the secret number, the secret number would become 37.)
        """
        return value ^ secret_number


    def __prune(self, secret_number):
        """
        To prune the secret number, calculate the value of the secret number
        modulo 16777216. Then, the secret number becomes the result of that
        operation. (If the secret number is 100000000 and you were to prune the
        secret number, the secret number would become 16113920.)
        """
        return secret_number % 16777216


    def __compute_next(self, secret_number):
        """
        1) Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.

        2) Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.

        3) Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
        """
        # Step 1
        modifier = secret_number * 64
        next_number = self.__mix(modifier, secret_number)
        next_number = self.__prune(next_number)

        # Step 2
        modifier = next_number // 32
        next_number = self.__mix(modifier, next_number)
        next_number = self.__prune(next_number)

        # Step 3
        modifier = next_number * 2048
        next_number = self.__mix(modifier, next_number)
        next_number = self.__prune(next_number)

        return next_number


    def __compute_to(self, secret_number, count):
        """
        Given an initial `secret_number`, compute up-to the `count`th next
        number.
        """
        working_number = secret_number
        for _ in range(count):
            working_number = self.__compute_next(working_number)

        return working_number


    def hack(self):
        total = 0

        for initial_num in self.__secret_numbers:
            total += self.__compute_to(initial_num, 2000)

        return total
