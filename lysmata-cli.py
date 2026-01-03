#!/usr/bin/env python3
"""
Lysmata CLI Entry Point

This script provides a command-line interface to the Lysmata fuzzer.
"""

if __name__ == "__main__":
    from lysmata.main import get_arguments, fuzz

    fuzzruns, seqlen, testfilename = get_arguments()
    fuzz(testfilename, fuzzruns, seqlen)
