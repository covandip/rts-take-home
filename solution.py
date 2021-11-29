class Solution:
    def aboveBelow(self, numbers: list, comparator: int) -> dict:
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
        # validate arguments
        if not isinstance(rotationString, str):
            raise Exception('rotationString must be a string.')
        if not isinstance(n, int) or n < 0:
            raise Exception('n must be a positive integer')
        stringLength = len(rotationString)
        # if the rotation amount is larger than the length of the string
        # reduce to n mod length to keep the indices in bounds
        if n > stringLength:
            n = n % stringLength
        return rotationString[-n:] + rotationString[:(stringLength - n)]

