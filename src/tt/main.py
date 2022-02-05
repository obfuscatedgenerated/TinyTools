import argparse
import os
import sys
import glob
import asyncio
from colorama import init, Fore, Style
init()

ap = argparse.ArgumentParser(description="Manage TinyTools and run a tool directly to bypass PATH conflicts.")

ap.add_argument(
    "action", type=str, help="the action you want to call (list, run)"
)
ap.add_argument("arguments", nargs="*", help="the arguments to pass to the action/tool")

preproc = sys.argv[1:]

if (len(preproc) < 1):
    preproc.insert(0, "--help")

if not (preproc[0] == "--help" or preproc[0] == "-h"):
    preproc.insert(0,"--")

args = ap.parse_args(preproc)

async def get_PATH_tt():
    proc = None
    if (os.platform == "win32"):
        proc = await asyncio.create_subprocess_shell(
            "where tt", stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE
        )
    else:
        proc = await asyncio.create_subprocess_shell(
            "which tt", stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE
        )

    stdout, stderr = await proc.communicate()
    if stderr:
        if stderr.startswith(b"INFO:"):
            print("Cannot use tt as TinyTools is not on the PATH.")
            sys.exit(1)
        else:
            print("Unexpected output from where: "+op)
            sys.exit(1)
    else:
        if os.path.isdir(os.path.dirname(stdout.decode().strip())):
            return os.path.dirname(stdout.decode().strip())

if (args.action == "list"):
    for file in glob.glob(os.path.join(asyncio.run(get_PATH_tt())+"/*.exe")):
        print(os.path.basename(file).replace(".exe",""))
elif (args.action == "run"):
    tool = args.arguments[0]
    toolargs = args.arguments[1:]
    toolpath = asyncio.run(get_PATH_tt())
    for file in glob.glob(os.path.join(toolpath)+"/*.exe"):
        if tool == os.path.basename(file).replace(".exe",""):
            os.system(os.path.join(toolpath,file)+" "+" ".join(toolargs))
            sys.exit(0)
    print("Tool not found.")
else:
    print(Fore.YELLOW+"Deprecation Warning: v1 syntax is being phased out! Use tt run {tool} instead of tt {tool}")
    print(Style.RESET_ALL)
    os.system(os.path.join(asyncio.run(get_PATH_tt()),args.action)+" "+" ".join(args.arguments))