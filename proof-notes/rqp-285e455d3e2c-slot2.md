# Repository note: unitconv

`unitconv` is a tiny, dependency-free unit converter CLI written for Python 3.11+ using only the standard library.

## Usage

```bash
python -m unitconv 100 c f      # 212.0
python -m unitconv 5 km mi      # 3.1069
```

## Supported units

- Temperature: `c`, `f`
- Length: `km`, `mi`, `m`, `ft`

Unit names are case-insensitive. Temperature and length units cannot be mixed in one conversion.

## Layout

- `unitconv/convert.py`: the conversion table and the `convert` function the CLI calls.
- `unitconv/__main__.py`: the command-line entry point.
- `unitconv/tests/`: the unit tests.

## Tests

```bash
python -m unittest discover -s unitconv/tests -v
```

Requester-Marker: rqp-second-285e455d3e2c
