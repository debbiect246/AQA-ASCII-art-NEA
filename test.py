class RunLengthEncoder:

    """
    class containing 3 methods that can be used to return a run-length
    encoded string.
    """

    def encode_a(self, text):

        """
        Returns a run-length encoded string from an input string.
        Note: This function will not return the character count in the return
        string if only a single instance of the character is found.

        Args:
            text (str): A string to encode

        Returns:
            str: A run length encoded string

        Example:
            input: "aaabbcdddd"
            returns: "3a2bc4d"
        """

        count = 1
        previous = ""
        mapping = list()

        for character in text:
            if character != previous:
                if previous:
                    mapping.append((previous, count))
                count = 1
                previous = character
            else:
                count += 1
        else:
            mapping.append((character, count))

        result = ""

        for character, count in mapping:
            if count == 1:
                result += character
            else:
                result += str(count)
                result += character

        return result

    def encode_b(self, text):

        """
        Returns a run-length encoded string from an input string.

        Args:
            text (str): A string to encode

        Returns:
            str: A run length encoded string

        Example:
            input: "aaabbcdddd"
            returns: "3a2b1c4d"
        """

        count = 1
        previous = ""
        mapping = list()

        for character in text:
            if character != previous:
                if previous:
                    mapping.append((previous, count))
                count = 1
                previous = character
            else:
                count += 1
        else:
            mapping.append((character, count))

        result = ""

        for character, count in mapping:
            result += str(count)
            result += character

        return result

    def encode_c(self, text):

        """
        Returns a run-length encoded string from an input string.
        This method uses a list comprehension to build the return
        string.

        Args:
            text (str): A string to encode

        Returns:
            str: A run length encoded string

        Example:
            input: "aaabbcdddd"
            returns: "3a2b1c4d"
        """

        count = 1
        previous = ""
        mapping = list()

        for character in text:
            if character != previous:
                if previous:
                    mapping.append((previous, count))
                count = 1
                previous = character
            else:
                count += 1
        else:
            mapping.append((character, count))

        result = "".join(f"{str(count)}{character}" for character, count in mapping)

        return result
