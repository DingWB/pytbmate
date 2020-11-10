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
- (1). Download HM450 array manifest file and index it with tabix:
```
#Downloading HM450 manifest file from illumina website
wget ftp://webdata2:webdata2@ussd-ftp.illumina.com/downloads/ProductFiles/HumanMethylation450/HumanMethylation450_15017482_v1-2.csv

#Prepare tabix index file
sed '1,8d' HumanMethylation450_15017482_v1-2.csv |cut -f 1 -d ","|grep -E "^cg|^ch|^rs" | sort -k1V |awk 'BEGIN {OFS="\t";print "Chr","Start","End","Index"} {print $0,1,2,NR-1}' | bgzip > hm450_idx.bed.gz
zcat hm450_idx.bed.gz |head

Chr	Start	End	Index
cg00000029	1	2	0
cg00000108	1	2	1
cg00000109	1	2	2
cg00000165	1	2	3
cg00000236	1	2	4
cg00000289	1	2	5
cg00000292	1	2	6
cg00000321	1	2	7
cg00000363	1	2	8

tabix -s 1 -b 2 -e 3 -p bed hm450_idx.bed.gz 
#Simple query with tabix:
tabix hm450_idx.bed.gz cg18478105:1-2
```

- (2). EPIC and WGBS index files:
Similarly, a EPIC manifest file can be downloaded from http://webdata.illumina.com.s3-website-us-east-1.amazonaws.com/downloads/productfiles/methylationEPIC/infinium-methylationepic-v5-manifest-file-csv.zip. To save time, we provided the index file and tabix index for EPIC and WGBS in [test dataset](https://).

2. Packing data into .tbk files.
