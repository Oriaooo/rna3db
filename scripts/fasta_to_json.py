from rna3db.utils import write_json
from rna3db.parser import parse_fasta
from pathlib import Path

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Converts a FASTA to an RNA3DB-style JSON."
    )
    parser.add_argument("input_path", type=Path)
    parser.add_argument("output_path", type=Path)
    args = parser.parse_args()

    descriptions, sequences = parse_fasta(args.input_path)
    data = {k: {"sequence": v} for (k, v) in zip(descriptions, sequences)}
    write_json(data, args.output_path)
