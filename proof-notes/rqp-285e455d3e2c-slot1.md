# Repository note: unitconv

`unitconv` is a tiny, dependency-free unit converter CLI. It targets Python 3.11+ and uses only the standard library.

## Usage

```bash
python -m unitconv 100 c f      # 212.0
python -m unitconv 5 km mi      # 3.1069
```

## Supported units

- Temperature: `c`, `f`
- Length: `km`, `mi`, `m`, `ft`

## Layout

- `unitconv/convert.py`: conversion logic
- `unitconv/__main__.py`: CLI entry point
- `unitconv/tests/`: unit tests

## Tests

```bash
python -m unittest discover -s unitconv/tests -v
```

Requester-Marker: rqp-owner-285e455d3e2c
