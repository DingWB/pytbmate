# pytbmate
Pytbmate is a Python API for [TabixMate](https://github.com/zhou-lab/tbmate): nimble storage of multifarious genomic data: https://github.com/zhou-lab/tbmate

## Dependencies:
- [tabix](http://www.htslib.org/doc/tabix.html)
- [tbmate](https://github.com/zhou-lab/tbmate)
- [pytabix](https://github.com/slowkow/pytabix)

## Installation
1. **Install tabix**:

If you have already installed HTSlib, then tabix should be already installed in your system.</br>
To test whether tabix is installed in your computer:
```
tabix --version
```
If not, you can download and install it in http://www.htslib.org/doc/tabix.html.</br>
OR
```
wget https://github.com/samtools/htslib/releases/download/1.11/htslib-1.11.tar.bz2
tar jxvf htslib-1.11.tar.bz2
cd htslib-1.11
./configure --prefix=/usr/local/htslib
make
make install
```
The executable programs will be installed to a bin subdirectory under your specified prefix, so you may wish to add this directory to your $PATH:
```
export PATH=/usr/local/htslib/bin:$PATH
```
You can chech whether tabix is successfully installed by running:
```
tabix -h
```

2. **Install tbmate**:
```
wget -O tbmate "https://github.com/zhou-lab/tbmate/releases/download/1.6.20200915/tbmate_linux_amd64"

# or mac
wget -O tbmate "https://github.com/zhou-lab/tbmate/releases/download/1.6.20200915/tbmate_darwin_amd64"

chmod a+x tbmate
# Moving tbmate to /usr/bin
mv tbmate /usr/bin
```

3. **Install pytabix**:
You can install pytabix before installing pytbmate, or pytabix will be install automatically when pytbmate is installed.
```
pip install pytabix
```

4. Install pytbmate:
```
pip install git+https://github.com/DingWB/pytbmate
```
OR
```
git clone https://github.com/DingWB/pytbmate
cd pytbmate
python setup.py install
```

## Usage
1. Building tabix index.
