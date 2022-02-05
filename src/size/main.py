import argparse
import math

ap = argparse.ArgumentParser(description="Get the line count of a file.")

ap.add_argument("file", type=argparse.FileType("r"), help="path to the file")
ap.add_argument(
    "--units",
    "-u",
    choices=[
        "bits",
        "bytes",
        "kilobits",
        "kilobytes",
        "megabits",
        "megabytes",
        "gigabits",
        "gigabytes",
        "terabits",
        "terabytes",
    ],
    default="bytes",
    help="units of the file size",
)
ap.add_argument(
    "--suffix",
    "-s",
    action="store_true",
    help="print the file size with the unit suffix",
)

args = ap.parse_args()

args.file.seek(0, 2)

bc = args.file.tell()

divisors = {
    "bits": 0.125,
    "bytes": 1,
    "kilobits": 125,
    "kilobytes": 1000,
    "megabits": 125000,
    "megabytes": 1000000,
    "gigabits": 125000000,
    "gigabytes": 1000000000,
    "terabits": 125000000000,
    "terabytes": 1000000000000,
}

suffixes = {
    "bits": "b",
    "bytes": "B",
    "kilobits": "Kb",
    "kilobytes": "KB",
    "megabits": "Mb",
    "megabytes": "MB",
    "gigabits": "Gb",
    "gigabytes": "GB",
    "terabits": "Tb",
    "terabytes": "TB",
}

dv = bc / divisors[args.units]

if math.floor(dv) == dv:
    dv = int(dv)

if args.suffix:
    print(str(dv) + suffixes[args.units])
else:
    print(dv)

args.file.close()
