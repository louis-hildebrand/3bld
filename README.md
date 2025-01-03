# 3bld

This is a collection of tools related to solving the Rubik's Cube blindfolded, especially using 3-style.

## Spreadsheet

These are useful functions for a 3-style algorithm spreadsheet.
They work in Google Sheets.

- [`invert_alg.txt`](./invert_alg.txt): Find the algorithm for the inverse case. For example, given a solution to AB, find one for BA.
- [`check_corner_commutator.txt`](./check_corner_commutator.txt): Check that the given algorithm correctly solves the given case.
- [`check_edge_commutator.txt`](./check_edge_commutator.txt): Check that the given algorithm correctly solves the given case.

In addition to the functions themselves, [`generate_lut.py`](./generate_lut.py) is used to generate a look-up table specifying how different moves affect the cube.

To update the spreadsheet, simply copy-paste the functions.
It doesn't hurt to remove unnecessary whitespace in the process.
That can be done with the following commands, assuming `xsel` is installed.

```sh
cat check_corner_commutator.txt | tr --delete '\n' | sed -E 's/\s+/ /g' | xsel --clipboard
```
