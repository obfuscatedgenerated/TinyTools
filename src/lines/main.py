import argparse

ap = argparse.ArgumentParser(description="Get the line count of a file.")

ap.add_argument("file", type=argparse.FileType("r", encoding="UTF-8"), help="path to the file")

args = ap.parse_args()

print(len(args.file.readlines()))

args.file.close()
