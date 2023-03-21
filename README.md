# AES-tool  
### AES encryption and decryption tool for files
### key size (64,48,32) hexadecimal characters
### mode ECP



## how to use :
```java
python3 aes.py
usage: aes.py [-h] [-e] [-d] [-o] [-k]

AES tool using 128,192,256 key ECB mode

options:
  -h, --help       show this help message and exit
  -e , --encrypt   path to the file you want to encrypt
  -d , --decrypt   path to the file you want to decrypt
  -o , --output    path to where you want the output to be
  -k , --key       key 64,48,32 hexadecimal characters
```

## encryption : 
```bash
python3 aes.py -e test.jpg -o test2.jpg -k be6c0c9857d8a7a0afe468fe46a2141a6c8d13e2592dadad4200e2913c357587
```
## output :
```
time to finish :  2.635785112
```
![3](https://user-images.githubusercontent.com/57776872/226442857-7b4f0d61-29ef-4fb1-b069-3cc9aa17948d.png)


## decryption : 
```bash
python3 aes.py -d test2.jpg -o test3.jpg -k be6c0c9857d8a7a0afe468fe46a2141a6c8d13e2592dadad4200e2913c357587
```

## output:
```
time to finish :  2.559194137
```
![5](https://user-images.githubusercontent.com/57776872/226442959-821867c1-9945-4be1-97da-cb64474fbd50.png)
