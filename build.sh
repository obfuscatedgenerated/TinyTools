PYTHONHASHSEED=1
export PYTHONHASHSEED
SOURCE_DATE_EPOCH=$(git log -1 --pretty=%ct)
export SOURCE_DATE_EPOCH
# create one-file build as myscript
pyinstaller ./spec/tt.spec
pyinstaller ./spec/chars.spec
pyinstaller ./spec/lines.spec
pyinstaller ./spec/size.spec
pyinstaller ./spec/image2ascii.spec
# let Python be unpredictable again
unset PYTHONHASHSEED
unset SOURCE_DATE_EPOCH