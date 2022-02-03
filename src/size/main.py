import argparse

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

if args.units == "bits":  # this sucks, i'll change it later
    if args.suffix:
        print(str(bc * 8) + "b")
    else:
        print(bc * 8)
elif args.units == "bytes":
    if args.suffix:
        print(str(bc) + "B")
    else:
        print(bc)
elif args.units == "kilobits":
    if args.suffix:
        print(str(bc / 125) + "kb")
    else:
        print(bc / 125)
elif args.units == "kilobytes":
    if args.suffix:
        print(str(bc / 1000) + "KB")
    else:
        print(bc / 1000)
elif args.units == "megabits":
    if args.suffix:
        print(str(bc / 125000) + "mb")
    else:
        print(bc / 125000)
elif args.units == "megabytes":
    if args.suffix:
        print(str(bc / 1000000) + "MB")
    else:
        print(bc / 1000000)
elif args.units == "gigabits":
    if args.suffix:
        print(str(bc / 125000000) + "gb")
    else:
        print(bc / 125000000)
elif args.units == "gigabytes":
    if args.suffix:
        print(str(bc / 1000000000) + "GB")
    else:
        print(bc / 1000000000)
elif args.units == "terabits":
    if args.suffix:
        print(str(bc / 125000000000) + "tb")
    else:
        print(bc / 125000000000)
elif args.units == "terabytes":
    if args.suffix:
        print(str(bc / 1000000000000) + "TB")
    else:
        print(bc / 1000000000000)

args.file.close()
