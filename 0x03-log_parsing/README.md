# Log Parsing

This directory contains a script that reads log entries from standard input, computes metrics, and prints statistics.

## Files

- `0-stats.py`: The main script that parses logs and prints statistics.
- `0-generator.py`: A script that generates random log entries for testing.

## Usage

To run the log parsing script, use the following command:

```bash
./0-generator.py | ./0-stats.py
```

This will generate random log entries and pass them to the `0-stats.py` script, which will compute and print the statistics. 