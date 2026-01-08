import argparse

parser = argparse.ArgumentParser(description="A simple calculator that divides two numbers.")

parser.add_argument("val1")
parser.add_argument("val2")

args = parser.parse_args()
    
# result = (float(args.val1) / float(args.val2))
    