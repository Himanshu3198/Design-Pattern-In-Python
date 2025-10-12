def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    col: Set[int] = set()
    row: Set[int] = set()

    for i in range(0, len(matrix)):

        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if i in row or j in col:
                matrix[i][j] = 0

def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        col: set[int] = set()
        row: set[int] = set()

        for i in range(0, len(matrix)):

            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if i in row or j in col:
                    matrix[i][j] = 0


