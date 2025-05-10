# ExtenderPass - Deterministic Password Extender

## Overview

ExtenderPass is a Python tool that transforms simple passwords into fixed-length complex strings in a deterministic way. Ideal for creating extended and more secure versions of your passwords while maintaining reproducibility.

## Key Features

- Deterministic conversion (same input → same output)
- Generates strings of any desired length
- Full control over output characters:
  - All ASCII characters (default)
  - Letters and numbers only
  - Digits only
  - Letters only
- Verbose mode for debugging
- Fast processing based on cryptographic hash functions

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kuznetsov0x/ExtenderPass.git
cd ExtenderPass
```

2. Or simply download the `extenderpass.py` file

## Usage

### Basic Usage
```bash
python extenderpass.py -s "your_password" -l 32
```

### Available Options

| Option          | Description                                      | Example                     |
|----------------|-----------------------------------------------|-----------------------------|
| `-s`, `--string` | Input password (required)                    | `-s "mypassword123"`        |
| `-l`, `--length` | Output length (≥1)                           | `-l 50`                     |
| `-n`, `--no-symbols` | Exclude symbols (!@#, etc.)               | `-n`                        |
| `-d`, `--digits-only` | Generate digits only (0-9)               | `-d`                        |
| `-a`, `--letters-only` | Generate letters only (A-Z,a-z)         | `-a`                        |
| `-v`, `--verbose` | Show processing details                  | `-v`                        |
| `-h`, `--help`    | Display help                             | `-h`                        |

### Practical Examples

1. **Standard complex password (with symbols)**:
   ```bash
   python extenderpass.py -s "simplePass" -l 40
   ```

2. **Long password without symbols**:
   ```bash
   python extenderpass.py -s "base123" -l 64 -n
   ```

3. **16-digit numeric PIN**:
   ```bash
   python extenderpass.py -s "secret" -l 16 -d
   ```

4. **24-character alphabetical token**:
   ```bash
   python extenderpass.py -s "master-key" -l 24 -a -v
   ```

## Typical Use Cases

- Create extended versions of short passwords
- Generate consistent tokens for development
- Produce complex numeric PINs
- Create reproducible temporary passwords
- Increase password complexity before storage
