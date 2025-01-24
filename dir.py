import os

def writeFolder(path, isDownloads):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            writeFolder(full_path, isDownloads)
        else:
            if isDownloads:
                f.write('https://downloads.scratch.mit.edu' + full_path[11:].replace('\\', '/') + '\n')
            else:
                f.write('https://download.scratch.mit.edu' + full_path[10:].replace('\\', '/') + '\n')

f = open("wget.txt", "w")
f.write('# Usage: wget --no-check-certificate -i wget.txt -x\n')
f.write('# Takes about half an hour to download everything on HDD and a Linksys USB wireless adapter\n')
f.write('# May be faster on SSD with a better wireless card\n\n')
writeFolder('./download', False)
writeFolder('./downloads', True)
f.close()