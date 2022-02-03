import argparse

ap = argparse.ArgumentParser(description="Get the character count of a file.")

ap.add_argument(
    "file", type=argparse.FileType("r", encoding="UTF-8"), help="path to the file"
)
ap.add_argument(
    "--keep-newlines",
    "-k",
    action="store_true",
    help="count newlines as characters",
)

args = ap.parse_args()

if args.keep_newlines:
    print(len(args.file.read()))
else:
    print(len(args.file.read().replace("\n", "")))

args.file.close()
