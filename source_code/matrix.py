import os
class SparseMatrix:
    def __init__(self, file_path=None, num_rows=0, num_cols=0):
        # initialize a sparse matrix
        self.rows = 0
        self.cols = 0
        self.data = {} #to store non zero elements
        if file_path is not None:
            self._load_from_file(file_path)
        else:
            self.rows = num_rows
            self.cols = num_cols

    def _load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = [line.strip() for line in f if line.strip()]
                if not lines[0].startswith('rows=') or not lines[1].startswith('cols='):
                    raise ValueError("Input file has wrong format")
                self.rows = int(lines[0][5:])
                self.cols = int(lines[1][5:])
                for line in lines[2:]:
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Input file has wrong format")
                    p = line[1:-1].split(',')
                    if len(p) != 3:
                        raise ValueError("Input file has wrong format")
                    try:
                        r = int(p[0].strip())
                        c = int(p[1].strip())
                        v = int(p[2].strip())
                    except ValueError:
                        raise ValueError("Input file has wrong format")
                    try:
                        self.set_element(r, c, v)
                    except IndexError:
                        continue
        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}")

    def get_element(self, r, c):
        if r >= self.rows or c >= self.cols or r < 0 or c < 0:
            raise IndexError("Index out of bounds")
        return self.data.get((r, c), 0)

    def set_element(self, r, c, v):
        if r >= self.rows or c >= self.cols or r < 0 or c < 0:
            raise IndexError("Index out of bounds")
        if v == 0:
            self.data.pop((r, c), None)
        else:
            self.data[(r, c)] = v

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for addition")
        res = SparseMatrix(num_rows=self.rows, num_cols=self.cols)
        for (r, c), v in self.data.items():
            res.set_element(r, c, v)
        for (r, c), v in other.data.items():
            cur = res.get_element(r, c)
            res.set_element(r, c, cur + v)
        return res

    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        res = SparseMatrix(num_rows=self.rows, num_cols=self.cols)
        for (r, c), v in self.data.items():
            res.set_element(r, c, v)
        for (r, c), v in other.data.items():
            cur = res.get_element(r, c)
            res.set_element(r, c, cur - v)
        return res

    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in first matrix must match number of rows in second matrix")
        res = SparseMatrix(num_rows=self.rows, num_cols=other.cols)
        other_map = {}
        for (r, c), v in other.data.items():
            if r not in other_map:
                other_map[r] = []
            other_map[r].append((c, v))
        for (i, k), a in self.data.items():
            if k in other_map:
                for (j, b) in other_map[k]:
                    cur = res.get_element(i, j)
                    res.set_element(i, j, cur + a * b)
        return res

    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.cols}\n")
            for (r, c), v in sorted(self.data.items()):
                f.write(f"({r}, {c}, {v})\n")

def main():
    # function to handle user input and perform operations
    os.makedirs("results", exist_ok=True) #creates results directory if it doen't exist
    print("Sparse Matrix Operations(add, subtract, multiply)")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    try:
        ch = int(input("Enter your choice (1-3): "))
        if ch not in [1, 2, 3]:
            raise ValueError("Invalid choice")
        f1 = input("Enter path to first matrix file: ")
        f2 = input("Enter path to second matrix file: ")
        m1 = SparseMatrix(f1)
        m2 = SparseMatrix(f2)
        if ch == 1:
            res = m1.add(m2)
            out_file = "results/addition_result.txt"
        elif ch == 2:
            res = m1.subtract(m2)
            out_file = "results/subtraction_result.txt"
        elif ch == 3:
            res = m1.multiply(m2)
            out_file = "results/multiplication_result.txt"
        res.save_to_file(out_file)
        print(f"Operation completed. Results saved to: {os.path.abspath(out_file)}")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()