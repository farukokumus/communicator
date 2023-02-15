# Task1 
This task includes UDP communication including CRC checksum for the message integrity.<br /> 
Sender is written in python, which sends 3x3 rotation matrix + CRC checksum. All elements of the matrix is double and checksum is unsigned integer (32 bit). <br /> 
Required libraries are zlib, and socket. 

## Python Side
To run the example, please type ```python ./udpSender.py```. 

## C++ Side
To build ```udpReceiver.cpp```, <br /> 
 please use ```g++ udpReceiver.cpp -o udpReceiver.exe -lz```, <br> then type 
```./udpReceiver.exe``` to run example