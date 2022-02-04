import argparse
import os

ap = argparse.ArgumentParser(description="Run a tool directly to bypass PATH conflicts.")

ap.add_argument(
    "tool", type=str, help="the tool you want to call"
)
ap.add_argument("passthrough",nargs="+", help="the arguments to pass to the tool")

args = ap.parse_args()

os.system(" ".join([args.tool] + args.passthrough))