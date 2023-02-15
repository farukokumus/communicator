#include <iostream>
#include <cmath>
// pointers 

using namespace std;

class Human{
protected: // thanks to protected we can use these private variable in derived classes..
    string Name;
    int Age; 
    
 public:   
    Human(){
        Name= "Noname";
        Age = 0;
    }

    Human(string aname, int aage){
        Name= aname;
        Age = aage;
    }

    string getName(){
        return Name; 
    }
    void setName(string name){
        Name = name;
    }

};

class Student : public Human {

    float gpa; 
    string major; 

    public:
    Student(string aname, int aage,float agpa, string amajor){
        Name= aname;
        Age = aage;
        gpa = agpa; 
        major = amajor ;
    }
    string getName(){
        return "Student name is" + Name; 
    }

};




void printer(int* page){
    cout << "printer funtion" << endl;
    cout<< *page << endl;
}

int main() {

    Human human1;
    Human human2("Lale", 25);
    Student student1("Lale", 25, 3.5, "Business");
    cout << human1.getName() << endl;
    human1.setName("cimcime");
    cout << human1.getName() << endl;
    cout << human2.getName() << endl; 
    cout << student1.getName() << endl; 


    // in the pointers & is referencing and * is dereferencing 
    int age = 55; 
    printer(&age);
    cout << &age << "\n"; //dereferencing it is going to print the address

    int* page= & age; //create a pointer of age as page

    cout<< *page << "\n"; // this is the dereferencing print out the value stored in page

    return 0;
}