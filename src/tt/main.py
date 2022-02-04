import argparse
import os
import asyncio

ap = argparse.ArgumentParser(description="Run a tool directly to bypass PATH conflicts.")

ap.add_argument(
    "tool", type=str, help="the tool you want to call"
)
ap.add_argument("passthrough", nargs="*", help="the arguments to pass to the tool")

args = ap.parse_args()

async def get_PATH_tt():
    proc = await asyncio.create_subprocess_shell(
        "where tt", stderr=asyncio.subprocess.PIPE, stdout=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()
    if stderr:
        if stderr.startswith(b"INFO:"):
            print("Cannot use tt to bypass PATH conflict as TinyTools is not on the PATH.")
            exit(1)
        else:
            print("Unexpected output from where: "+op)
            exit(1)
    else:
        if os.path.isdir(os.path.dirname(stdout.decode().strip())):
            os.system(os.path.join(os.path.dirname(stdout.decode().strip()),args.tool)+" "+" ".join(args.passthrough))

asyncio.run(get_PATH_tt())