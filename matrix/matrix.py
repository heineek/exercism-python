class Matrix(object):
    def __init__(self, data):
        self.rows = data.split('\n')
        for pos, row in enumerate(self.rows):
            self.rows[pos] = row.split()
            for i, num in enumerate(self.rows[pos]):
                self.rows[pos][i] = int(num)

        self.columns = []
        for j in range(len(self.rows[0])):
            column = []
            for i in range(len(self.rows)):
                column.append(self.rows[i][j])
            self.columns.append(column)