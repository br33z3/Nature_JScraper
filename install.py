import os

os.system("apt-get update && apt-get install golang -y")
os.system("python3 LinkFinder/setup.py install")
os.system("pip3 install -r jsbeautifier")
os.system("pip3 install pyfiglet argparse html==1.7")
os.system("rm -rf build/ README.md dist/ LinkFinder.egg-info/")
os.system("mv LinkFinder/linkfinder.py LinkFinder/template.html .")
os.system("rm -rf LinkFinder")
os.system("go install -v github.com/003random/getJS@latest")
os.system("cp /root/go/bin/getJS /bin/getJS")
os.system("go install -v github.com/tomnomnom/waybackurls@latest")
os.system("cp /root/go/bin/waybackurls /usr/bin/waybackurls")
os.system("pip3 install timeout_decorator")
os.system("go install -v github.com/jaeles-project/gospider@latest")
os.system("cp /root/go/bin/gospider /bin/gospider")
