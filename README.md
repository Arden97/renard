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
### Installing
Run these commands in your terminal:
```
-> cd /home/user/bin
-> git clone https://github.com/Arden97/renard.git
-> cd renard
-> chmod +x renard.py renard_tools.py
```
Add this to your shell config file (.zshrc in my case):
```
export PATH=$PATH:/home/arden/bin/renard
```
Now run:
```
-> source ~/.zshrc
-> renard.py -h
```
Help message will show up. Here you can see detailed information about the flags and options of the tool.
