# parviflora is a binary exchange format

[Permuatio](https://codeberg.org/Patpine/Permutatio) uses a binary format called parviflora.
This is a python implementation of said format.

## Usage

The module exports main 2 methods `write_msg` and `read_msg`, as well as their safe (non-exception throwing) counterparts `safe_write_msg` and `safe_read_msg`.

Documentation:

### `write_msg`

Takes 2 argumentss

- `file`: a BufferedWriter that can have binary values write to
- `obj`: one of the types that parviflora can represent, that will be writen

### `safe_write_msg`

Takes 2 argument:

- `filename`: a filename that the file should be written to, should there not be issues with writing the value
- `obj`: as in above

It also returns 1 value: Either `None` or `str` which is an error string

### `read_msg`

Takes 1 argument:

- `file`: a BufferedReader that can have binary values read from

It also returns 1 value: an object that has been read from the file.

### `safe_read_msg`

Takes 1 argument:

- `filename`: a filename that the file should be read from

It also returns 1 value: an object that has been read from the file or an error.

## Example

```python
import binformat

safe_write_msg("hexxy", {
    1: b"Hello world",
    2: [1, 2, 3]
})

with open("hexxy", "rb") as f:
    print(read_msg(f))
    # { 1: b"Hello world", 2: [1, 2, 3] }
```

## Testing

Run `tests.py`
