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


    def __compute_price(self, secret_number):
        s1 = secret_number - (secret_number // 10)
        s2 = secret_number - s1
        price = secret_number - s2 * 10

        return price


    def __track_prices(self, secret_number, count):
        """
        Given an initial `secret_number`, compute the price and price changes
        up-to the `count`TH number.
        """
        market_prices = []
        prev_price = self.__compute_price(secret_number)
        market_prices.append((prev_price, None))
        working_number = secret_number
        for _ in range(count):
            working_number = self.__compute_next(working_number)

            # Track Price
            price = self.__compute_price(working_number)
            market_prices.append((price, price - prev_price))
            prev_price = price

        return market_prices


    def __analyze_prices(self, price_changes):
        best_price = 0
        best_index = 0
        for idx, info in enumerate(price_changes):
            # Don't care unless we have at least 4 changes
            if idx >= 4:
                price = info[0]
                if price > best_price:
                    best_price = price
                    best_index = idx

        seq = []
        for i in range(3, -1, -1):
            info = price_changes[best_index-i]
            seq.append(info[1])

        return seq


    def __compute_to(self, secret_number, count):
        """
        Given an initial `secret_number`, compute up-to the `count`TH next
        number.
        """
        working_number = secret_number
        for _ in range(count):
            working_number = self.__compute_next(working_number)

        return working_number


    def hack(self, **kwargs):
        total = 0
        mode = kwargs.get("mode", "sn2000_sum")

        if mode == "sn2000_sum":
            for initial_num in self.__secret_numbers:
                total += self.__compute_to(initial_num, 2000)
        elif mode == "buy_bananas":
            all_market_changes = []
            for initial_num in self.__secret_numbers:
                market_changes = self.__track_prices(initial_num, 10)
                all_market_changes.append(market_changes)

                best_seq = self.__analyze_prices(market_changes)
                print(market_changes, best_seq)

            # TODO: what if multiple seq at same price point?
            # find all best price seq
            # count how may times each appears in all other number's changes
            # one with the most is the winner?

        return total





#
