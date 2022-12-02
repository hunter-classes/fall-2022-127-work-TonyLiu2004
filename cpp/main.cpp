#include <iostream>

/*
 functions included: 
  - addInt -> add 2 integers and return sum
  - returnLarger -> input 2 integers and returns larger integer
  - sum1ToNum -> Returns sum from 1 to inputted integer
*/
using namespace std;

int addInt(int x, int y); // declares functions so the function script can be below main()
int returnLarger(int x, int y);
int sum1ToNum(int x);

int main() {
    cout << "Hello World!\n";
    cout << "Add 10 and 20: " << addInt(10,20) << endl;
    cout << "Largest between 10 and 20: " << returnLarger(10,20) << endl;
    cout << "Sum from 1 to 20: " << sum1ToNum(20) << endl;
    return 0;
}

int addInt(int x, int y){
    return x + y;   
}

int returnLarger(int x, int y){
    if (x > y){
        return x;
    }else{
        return y;
    }
}

int sum1ToNum(int x){
    int sum = 0;
    for(int i = 1; i <= x; i++){
        sum += i;
    }
    return sum;
}