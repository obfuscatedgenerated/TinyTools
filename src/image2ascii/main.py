import argparse
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser(description="Display an image as grayscale ASCII art.")

ap.add_argument(
    "file", type=argparse.FileType("rb"), help="path to the file"
)
ap.add_argument(
    "--scale", "-s", type=float, help="the scale of the image", default=1.0
)

args = ap.parse_args()

img = Image.open(args.file).convert("L")

ia = np.array(img)

w,h = ia.shape

if args.scale != 1.0:
    w = int(w*args.scale)
    h = int(h*args.scale)
    ia = np.array(img.resize((w,h)))

output = []

asc_scalar = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

for i in range(0,w):
    row = []
    for j in range(0,h):
        row.append(asc_scalar[int((np.average(ia[i][j])*(len(asc_scalar)-1))/255)])
    output.append("".join(row))

print("\n".join(output))
