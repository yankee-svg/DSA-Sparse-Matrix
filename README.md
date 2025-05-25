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
├── src/
│   ├── components/
│   │   └── __pycache__/           # Python bytecode cache
│   ├─
│   ├── results/
│   │   └── addition_result.txt    # Output from matrix operations
│   └── sparse_matrix.py           # python script
├── sample_inputs/
│   
│   ├── easy_sample_01_2.txt       # test file
│   └── easy_sample_01_3.txt       # test file 
```

## Usage

1. Navigate to the src directory:
   ```bash
   cd src/components
   ```

2. Run the program:
   ```bash
   python sparse_matrix.py
   ```

3. Follow the interactive prompts to:
   - Select an operation (Addition, Subtraction, or Multiplication)
   - Provide paths to two input matrix files
   - View the results saved to a results file

## Input File Format from the txt

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

