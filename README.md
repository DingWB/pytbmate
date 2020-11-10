# pytbmate
Pytbmate is a Python API for [TabixMate](https://github.com/zhou-lab/tbmate): nimble storage of multifarious genomic data: https://github.com/zhou-lab/tbmate

## Dependencies:
- [tabix](http://www.htslib.org/doc/tabix.html)
- [tbmate](https://github.com/zhou-lab/tbmate)
- [pytabix](https://github.com/slowkow/pytabix)

## **Installation**
1. **Install tabix**:

You can download and install tabix in http://www.htslib.org/doc/tabix.html. Or:
```
wget https://github.com/samtools/htslib/releases/download/1.11/htslib-1.11.tar.bz2
tar jxvf htslib-1.11.tar.bz2
cd htslib-1.11
./configure --prefix=/usr/local/htslib
make
make install

#Adding to your $PATH
export PATH=/usr/local/htslib/bin:$PATH
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

3. **Install pytbmate**:
```
pip install pytabix
pip install git+https://github.com/DingWB/pytbmate
```
OR
```
git clone https://github.com/DingWB/pytbmate
cd pytbmate
python setup.py install
```

## **Usage**
1. Building tabix index.
- (1). Downloading EPIC manifest file and building tabix index:
```
#Download manifest file of EPIC from https://support.illumina.com
wget http://webdata.illumina.com.s3-website-us-east-1.amazonaws.com/downloads/productfiles/methylationEPIC/infinium-methylationepic-v5-manifest-file-csv.zip
unzip infinium-methylationepic-v-1-0-b5-manifest-file-csv.zip
#Prepare tabix index file
sed '1,8d' infinium-methylationepic-v-1-0-b5-manifest-file.csv |cut -f 1 -d ","|sort -k1V |awk 'BEGIN {OFS="\t";print "Chr","Start","End","Index"} {print $0,1,2,NR-1}' | bgzip > epic_idx.gz
zcat epic_idx.gz |head
```
```
Chr	Start	End	Index
10609447	1	2	0
10627500	1	2	1
10676356	1	2	2
10714330	1	2	3
10731326	1	2	4
10732387	1	2	5
10740401	1	2	6
10744385	1	2	7
10760363	1	2	8
```
```
tabix -s 1 -b 2 -e 3 epic_idx.gz
#Simple query with tabix:
tabix epic_idx.gz cg18478105:1-2
```
