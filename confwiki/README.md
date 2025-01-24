# Confwiki
Python script to turn a WikkaWiki install into a wget input file which downloads from the [Scratch Conference 2008 Wiki](https://download.scratch.mit.edu/conference/wiki/index.php).

## Usage
#### This guide was never tested as this python script wasn't meant to be public
1. Clone WikkaWiki:
```
git clone https://github.com/bakoontz/WikkaWiki
cd WikkaWiki
```
2. Switch to 1.1.6.5:
```
git checkout 1.1.6.5
```
3. Delete `.git` and `.htaccess` and create a file called `wikka.config.php`:

On Windows:
```
rd /s /q .git
del .htaccess
echo "" > wikka.config.php
```
On *nix:
```
rm -r .git
rm .htaccess
touch wikka.config.php
```
4. Run it:
```
py dir.py
```
5. wget it:
```
wget --no-check-certificate -i wget.txt -x
```
6. Copy `/download.scratch.mit.edu/conference/wiki` into `/conference` from ScratchDownload
7. Run ScratchDownload's dir.py