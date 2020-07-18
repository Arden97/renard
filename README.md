# renard
Small file renaming tool written in python. With it, you can rename several files and subdirectories according to certain name convention.
### Example
```
-> ls
dASDSArrr.docx   sadsadasdsadas.txt  sfddsafdsafsadfdasf
fasdfasfadsfasf  sdfasdfsdfasfsd
-> renard.py test
-> ls
test1.docx  test2  test3.txt  test4  test5
```
### Prerequisites
For the script to work correctly, you will need a Click package. The easiest way to install it is:
```
pip install click
```

### Installing
Run these commands in your terminal:
```
-> cd /home/user/bin
-> git clone https://github.com/Arden97/renard.git
-> cd renard
-> pip install --user .
```

### Run
```
-> renard.py --help
```
Help message will show up. Here you can see detailed information about the options of the tool.
