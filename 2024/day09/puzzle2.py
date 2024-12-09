#!/usr/bin/env python
import sys

from disk_fragmenter import DiskFragmenter

def main(input_file:str) -> None:

    fsck = DiskFragmenter(input_file)
    # print(fsck)
    fsck.expand()
    # print(fsck)
    fsck.smart_enfrag()
    # print(fsck)

    print(f"""--- Day 09 // Puzzle 02 ---
-> Input File: {input_file}
-> File Count: {fsck.file_count}
-> Checksum: {fsck.checksum}
""")


if __name__ == "__main__":
    input_file = "./disk.map"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]

    main(input_file)
