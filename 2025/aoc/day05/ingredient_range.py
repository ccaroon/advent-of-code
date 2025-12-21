class IngredientRange:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    def __len__(self):
        return (self.end - self.start) + 1

    def __str__(self):
        return f"IngredientRange({self.start}-{self.end})"

    def __repr__(self):
        return f"IngredientRange({self.start}-{self.end})"

    def compare(self, other):
        """
        Compare two Ingredient Ranges: Compare `self` to `other`

        Returns:
            -1   - if overlap on left / low end
            1    - if overlap on right / high end
            0    - if overlap in middle / included in other range
            None - if NO overlap
        """
        result = None

        # left
        if self.start < other.start and other.start <= self.end <= other.end:
            result = -1

        # right
        if other.start <= self.start <= other.end and self.end > other.end:
            result = 1

        # middle
        if (other.start <= self.start <= other.end) and (other.start <= self.end <= other.end):
            result = 0

        return result

    def is_fresh(self, iid):
        """
        Is `iid` in this indredient range with start and end being inclusive

        Args:
            iid (int): Ingredient ID
        """
        is_fresh = False
        if iid >= self.start and iid <= self.end:
            is_fresh = True

        return is_fresh

    def unique_iids(self, other):
        """Count the number of unique indredient ids betwee two ranges"""
        count = 0

        if self.compare(other) is None and other.compare(self) is None:
            # print("No Overlap")
            count = len(self) + len(other)
        elif self.compare(other) == 0:
            # print("self contained in other")
            count = len(other)
        elif other.compare(self) == 0:
            # print("other contained in self")
            count = len(self)
        elif self.compare(other) == -1 or self.compare(other) == 1:
            # print("some overlap")
            rng1 = None
            if self.start < other.start:
                rng1 = IngredientRange(self.start, other.start - 1)
            else:
                rng1 = IngredientRange(other.start, self.start - 1)

            rng2 = None
            if self.end < other.end:
                rng2 = IngredientRange(self.end + 1, other.end)
            else:
                rng2 = IngredientRange(other.end + 1, self.end)

            # print(rng1, rng2)

            count = len(rng1) + len(rng2)

        return count

    def overlap_count(self, other):
        overlap_count = 0

        if self.start >= other.start and self.start <= other.end:
            overlap_count += (other.end - self.start) + 1
            # self._debug(f"{irng} overlaps {other_rng} @ start[{self.start}]: {overlap_count}")
        elif self.end >= other.start and self.end <= other.end:
            # self._debug(f"{irng} overlaps {other_rng} @ end[{self.end}]: {overlap_count}")
            overlap_count += (self.end - other.start) + 1

        return overlap_count

    #
