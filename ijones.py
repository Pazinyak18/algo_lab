from collections import defaultdict


class IJones:
    def __init__(self, corridor, columns, rows):
        self.corridor = list(corridor)
        self.columns = columns
        self.rows = rows
        self.slabs = [[1] for i in range(self.rows)]
        self.memoized_path = defaultdict(int)

    def algo(self):
        for row in range(self.rows):
            self.memoized_path[self.corridor[row][0]] += 1

        for column in range(1, self.columns):
            ways = {}

            for row in range(self.rows):
                name_plate = self.corridor[row][column]

                if name_plate is not self.corridor[row][column - 1]:
                    cur_way = self.slabs[row][column - 1] + self.memoized_path[name_plate]
                else:
                    cur_way = self.memoized_path[name_plate]

                self.slabs[row].append(cur_way)
                ways[name_plate] = cur_way + ways.get(name_plate, 0)

            if not column >= self.columns:
                for letter in ways:
                    self.memoized_path[letter] += ways[letter]

        if len(self.slabs) > 1:
            return self.slabs[0][-1] + self.slabs[-1][-1]
        else:
            return self.slabs[0][-1]


if __name__ == '__main__':
    arr = [['a', 'a', 'a', ],
           ['c', 'a', 'b', ],
           ['d', 'e', 'f', ]]

    alg = IJones(arr, 3, 3)  # column rows

    print(alg.algo())
