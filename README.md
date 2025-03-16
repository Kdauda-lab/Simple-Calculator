# Simple Calculator

A simple Python program that performs basic arithmetic operations (addition, subtraction, multiplication, and division) based on user input.

## Features

- Accepts two numerical inputs from the user.
- Supports the following operations:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
- Handles division by zero with an appropriate error message.
- Validates input to ensure proper numerical values and valid operations are entered.

## Prerequisites

- Python 3.x

## Installation

No installation is necessary, just copy the code and run it on your local machine.

1. Clone or download the repository:
    ```
    git clone https://github.com/Kdauda-lab/simple-calculator.git
    ```

2. Navigate into the project directory:
    ```
    cd simple-calculator
    ```

3. Run the program:
    ```
    python calculator.py
    ```

## Usage

Upon running the script, the user will be prompted to:

1. Enter the first numerical value.
2. Enter the operation (choose from `+`, `-`, `*`, or `/`).
3. Enter the second numerical value.

### Example Input/Output:

```
Enter first value: 10
Enter operation (+, -, *, /): +
Enter second value: 5
```

```
Output: 15
```

If an invalid operation is entered:

```
Enter first value: 10
Enter operation (+, -, *, /): ^
Enter second value: 5
```

```
Output: Invalid operation. Please enter one of +, -, *, or /.
```

### Error Handling:

- Division by zero will display a user-friendly error message:
  ```
  Enter first value: 10
  Enter operation (+, -, *, /): /
  Enter second value: 0
  ```
  ```
  Output: Error: Cannot divide by zero
  ```

- Invalid numerical input will prompt the user to enter a valid number:
  ```
  Enter first value: abc
  ```

  ```
  Output: Invalid input. Please enter valid numbers.
