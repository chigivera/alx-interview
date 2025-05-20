# UTF-8 Validation

This directory contains a script that validates UTF-8 encoding in a dataset.

## Files

- `0-validate_utf8.py`: The main script that validates UTF-8 encoding.
- `0-main.py`: A test file that demonstrates the usage of the validation function.

## Usage

To run the validation script, use the following command:

```bash
./0-main.py
```

This will test the UTF-8 validation function with different datasets.

## UTF-8 Encoding Rules

- A character in UTF-8 can be 1 to 4 bytes long
- Single byte characters start with 0
- Multi-byte characters start with 1s followed by a 0
- Continuation bytes start with 10
- The data is represented by a list of integers
- Only the 8 least significant bits of each integer are considered 