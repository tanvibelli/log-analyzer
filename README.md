# Log Analyzer

A small Python tool that reads a login log, counts failed logins for each IP address, and flags IPs with more than 5 failures as possibly brute-force attacks.

## How to run

python3 analyzer.py

## How to run the tests

pip3 install pytest
pytest

## How it works

1. Reads sample.log one line at a time
2. Splits each line into date, time, status, IP, and username
3. Counts the FAILED lines per IP in a dictionary
4. Prints a warning for any IP over the threshold


## Ideas for next steps

- Handle blank or badly formatted lines without crashing
- Let the user pick the file and threshold from the command line
