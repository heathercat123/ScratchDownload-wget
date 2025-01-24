# [ScratchDownload-wget](https://github.com/heathercat123/ScratchDownload-wget/blob/master/wget.txt)
Wget input file to download almost everything from Scratch's download servers ([download.scratch.mit.edu](https://download.scratch.mit.edu/) and downloads.scratch.mit.edu](https://downloads.scratch.mit.edu/)).

Also includes a Python script to generate it, useful for contributing to this repository.

## Wget usage
```
wget --no-check-certificate -i wget.txt -x
```
On Windows, you can also use `get.bat`.

## Python script usage
1. Get ScratchDownload
An [outdated version](https://github.com/heathercat123/ScratchDownload/) is available on github. To get a more recent version, use wget then rename `download.scratch.mit.edu` to `download` and `downloads.scratch.mit.edu` to `downloads`.
2. Run dir.py
```
py dir.py
```
This python script generates `wget.txt` based on the `download` and `downloads` folder.