import os


os.system("git clone https://github.com/br33z3/Nature_JScraper/tree/main/LinkFinder")
os.system("cp LinkFinder/README.md .")
os.system("python3 LinkFinder/setup.py install")
os.system("pip3 install -r  LinkFinder/requirements.txt")
os.system("pip3 install pyfiglet argparse html==1.7")
os.system("rm -rf build/ README.md dist/ LinkFinder.egg-info/")
os.system("mv LinkFinder/linkfinder.py LinkFinder/template.html .")
os.system("rm -rf LinkFinder")
os.system("go get github.com/003random/getJS")
os.system("cp /root/go/bin/getJS /bin/getJS")
os.system("go install -v github.com/tomnomnom/waybackurls@latest")
os.system("cp /root/go/bin/waybackurls /usr/bin/waybackurls")
os.system("pip3 install timeout_decorator")
