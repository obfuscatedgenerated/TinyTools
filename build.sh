pyinstaller --onefile ./src/tt/main.py --specpath ./spec/ --name=tt
pyinstaller --onefile ./src/chars/main.py --specpath ./spec/ --name=chars
pyinstaller --onefile ./src/lines/main.py --specpath ./spec/ --name=lines
pyinstaller --onefile ./src/size/main.py --specpath ./spec/ --name=size
pyinstaller --onefile ./src/image2ascii/main.py --specpath ./spec/ --name=image2ascii