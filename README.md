# DSA-Sparse-Matrix

This project implements a memory-efficient sparse matrix data structure with support for addition, subtraction, and multiplication operations.

## Features

- Memory-efficient storage using dictionary-based sparse representation
- File I/O with format validation and error handling
- Interactive command-line interface
- Support for large matrices with minimal memory footprint
- Comprehensive error handling and input validation

## Project Structure

```
src/
├── main.py                 # Main entry point
├── components/
│   ├── SparseMatrix.py     # Core sparse matrix implementation
│   └── MatrixOperations.py # Operations and user interface
└── sample_inputs/
    ├── matrix1.txt         # Sample 3x3 matrix
    ├── matrix2.txt         # Sample 3x3 matrix
    ├── large_matrix1.txt   # Sample 1000x1000 matrix
    └── large_matrix2.txt   # Sample 1000x1000 matrix
```

## Usage

1. Navigate to the src directory:
   ```bash
   cd src
   ```

2. Run the program:
   ```bash
   python main.py
   ```

3. Follow the interactive prompts to:
   - Select an operation (Addition, Subtraction, or Multiplication)
   - Provide paths to two input matrix files
   - View the results saved to a results file

## Input File Format

Matrix files should follow this format:
```
rows=<number_of_rows>
cols=<number_of_columns>
(row, col, value)
(row, col, value)
...
```

Example:
```
rows=3
cols=3
(0, 0, 1)
(0, 1, 2)
(1, 0, 3)
(1, 1, 4)
(2, 2, 5)
```

