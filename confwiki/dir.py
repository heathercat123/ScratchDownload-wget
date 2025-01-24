import os

# Based on dir.py from local ScratchDownload
# Before running:
#- Delete ./WikkaWiki/.git
#- Delete ./WikkaWiki/.htaccess
#- Create a file called ./WikkaWiki/wikka.config.php

def writeFolder(path, isDownloads):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            writeFolder(full_path, isDownloads)
        else:
            if isDownloads:
                f.write('https://downloads.scratch.mit.edu' + full_path[11:].replace('\\', '/') + '\n')
            else:
                f.write('https://download.scratch.mit.edu/conference/wiki' + full_path[11:].replace('\\', '/') + '\n')

f = open("wget.txt", "w")
f.write('# Usage: wget --no-check-certificate -i wget.txt -x\n')
f.write('# Then, put its contents into the local ScratchDownloads and run its dir.py\n\n')
writeFolder('./WikkaWiki', False)
f.close()