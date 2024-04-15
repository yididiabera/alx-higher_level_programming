
#!/usr/bin/python3
"""inheritance of MyInt from int"""


class MyInt(int):
    """change place int operators == and !=."""

    def __eq__(self, value):
        """write over == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """changes != operator with == behavior."""
        return self.real == value
