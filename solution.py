class Solution:

    def aboveBelow(self, numbers: list, comparator: int) -> dict:
        """
        This function will take a list of ints and a int to compare them to and return
        a dict with the number of ints above and below as values to the keys "above" and
        "below".
        :param numbers: A list of integers
        :param comparator: An integer to compare the list values
        :return: A dict with the keys "above" and "below" that map to the number of ints
                 that are above and below the comparator int
        """
        # validate arguments
        if not (isinstance(numbers, list) and all(isinstance(x, int) for x in numbers)):
            raise Exception('numbers must be a list of ints')
        if not isinstance(comparator, int):
            raise Exception('comparator must be an int')
        # count items above and below and return dict
        below = sum(1 for x in numbers if x < comparator)
        above = sum(1 for x in numbers if x > comparator)
        return {'below': below, 'above': above}

    def stringRotation(self, rotationString: str, n: int) -> str:
        """
        This function will rotate a string to the right and place the overflow in the front.
        :param rotationString: A string to be rotated.
        :param n: A positive integer amount of space to rotate the string by
        :return: Rotated string
        """
        # validate arguments
        if not isinstance(rotationString, str):
            raise Exception('rotationString must be a string.')
        if not isinstance(n, int) or n < 1:
            raise Exception('n must be a positive integer')
        stringLength = len(rotationString)
        # if the rotation amount is larger than the length of the string
        # reduce to n mod length to keep the indices in bounds
        if n > stringLength:
            n = n % stringLength
        return rotationString[-n:] + rotationString[:(stringLength - n)]
