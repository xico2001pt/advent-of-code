class Matrix:
    def __init__(self, data):
        """
        Initializes a Matrix object.

        :param data: A 2D list representing the matrix elements.
        """
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same number of columns.")
        self.data = data

    def num_rows(self):
        """
        Returns the number of rows in the matrix.

        :return: Integer representing the number of rows.
        """
        return len(self.data)

    def num_columns(self):
        """
        Returns the number of columns in the matrix.

        :return: Integer representing the number of columns.
        """
        return len(self.data[0]) if self.data else 0

    def get_element(self, row, col):
        """
        Retrieves the element at the specified row and column.

        :param row: Row index (0-based).
        :param col: Column index (0-based).
        :return: The element at the given position.
        :raises IndexError: If the row or column index is out of bounds.
        """
        if row < 0 or row >= self.num_rows():
            raise IndexError("Row index out of bounds.")
        if col < 0 or col >= self.num_columns():
            raise IndexError("Column index out of bounds.")
        return self.data[row][col]

    def __repr__(self):
        """
        Returns a string representation of the matrix for debugging purposes.

        :return: String representation of the matrix.
        """
        return "\n".join([" ".join(map(str, row)) for row in self.data])
