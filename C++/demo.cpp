#include<iostream>
using namespace std;

int main() {
    int a=5;
    int b=2;
    int  d=10;
    double  price=100.99;
    char grade = 'a';
    float PI = 3.14f;
    bool issafe= false;
    bool issnot= true;


    cout << issafe << endl;//false->0 & true->1
    cout << issnot << endl;//false->0 & true->1
    cout << a + d << endl;
    cout << price  << endl;// in int after decimal will not show but without round off the digit 
    cout << a/b    << endl;
    cout << a - b  << endl;
    cout << a%b    << endl;// that's use for checking remainder if yes then show 1 and if now remainder then it's shows 0 
    cout << a*b    << endl;
    //g++ demo.cpp -o demo && .\demo
    cout << a+ price << endl;
    cout << price + PI << endl;
    cout << a + b + d + price + PI << endl;
    cout << a + b + price / d  + PI << endl;
    
    return 0;
}


