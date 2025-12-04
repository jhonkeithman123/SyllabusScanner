import argparse
from app import process_file

def parse_args():
    ap = argparse.ArgumentParser(description="SyllabusScanner CLI")
    ap.add_argument("input", help="Path to input PDF or DOCX")
    return ap.parse_args()

def main():
    args = parse_args()
    print(process_file(args.input))

if __name__ == "__main__":
    main()