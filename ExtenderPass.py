import argparse
import hashlib
import random
import string
import sys

def pre_hash(input_str):
    """First deterministic hashing stage"""
    return hashlib.sha512(input_str.encode()).hexdigest()

def generate_fixed_length_hash(input_str, length, verbose=False, no_symbols=False, 
                             digits_only=False, letters_only=False):
    # Create unique identifier based on input parameters
    params_hash = hashlib.md5(f"{input_str}{length}{no_symbols}{digits_only}{letters_only}".encode()).hexdigest()
    
    # First hashing stage
    intermediate_hash = pre_hash(input_str + str(length) + params_hash)
    
    # Deterministic seed based on hash
    seed = int(hashlib.sha256(intermediate_hash.encode()).hexdigest(), 16) % (2**32)
    random_gen = random.Random(seed)
    
    # Define character set based on parameters
    if digits_only:
        chars = string.digits
    elif letters_only:
        chars = string.ascii_letters
    elif no_symbols:
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    
    # Generate and reverse the string
    result = ''.join(random_gen.choice(chars) for _ in range(length))[::-1]
    
    if verbose:
        print(f"Input: {input_str}")
        print(f"Length: {length}")
        print(f"Params: no_symbols={no_symbols}, digits_only={digits_only}, letters_only={letters_only}")
        print(f"Seed: {seed}")
        print(f"Result: {result}")
    
    return result

def main():
    parser = argparse.ArgumentParser(description="Deterministic string generator", add_help=False)
    
    parser.add_argument("-s", "--string", required=True, help="Input string")
    parser.add_argument("-l", "--length", type=int, required=True, help="Output length")
    parser.add_argument("-n", "--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("-d", "--digits-only", action="store_true", help="Digits only")
    parser.add_argument("-a", "--letters-only", action="store_true", help="Letters only")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose mode")
    parser.add_argument("-h", "--help", action="store_true", help="Show help")
    
    args = parser.parse_args()
    
    if args.help:
        parser.print_help()
        sys.exit(0)
    
    if args.length <= 0:
        print("Error: Length must be positive", file=sys.stderr)
        sys.exit(1)
    
    result = generate_fixed_length_hash(
        args.string,
        args.length,
        args.verbose,
        args.no_symbols,
        args.digits_only,
        args.letters_only
    )
    
    print(result)

if __name__ == "__main__":
    main()
