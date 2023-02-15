#include <iostream>
#include <cmath>


using namespace std;

// define global var
int age; 
float tall;
string name;
int myNumbers[5] = {10, 20, 30, 40, 50};

// useful string function 
string clipper(string str){
return str.substr(0,3); // other useful functions are 
}

bool looker(int* rr, unsigned int length){
bool ind =false;
for(int i=0;  i < length;i++){
    if (rr[i] > 50.0 )
    {
        ind=true;
    }
}
return ind;
}




// data type exercise for cpp iint float string etc 
int main() {
age = 55;
printf("what is your name \n");
cin >> name ;
cout<< age << "\n";
cout << clipper(name) << endl; 
unsigned int length =  sizeof(myNumbers) / sizeof(int);
bool bigger=looker(myNumbers,length);
cout << bigger << endl; 
return 0;
}