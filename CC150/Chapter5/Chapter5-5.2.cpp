#include <iostream>
#include <string>
using namespace std; 

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
string printBinary(double num){

	if(num<0 or num>1)
		return "ERROR";

	string binary = ".";

	while(num>0){

		if (binary.length() >= 32){
			return "ERROR";
		}

		num = num*2;

		if(num>1){
			binary = binary + "1";
			num = num - 1;
		} else {
			binary = binary + "0";
		}
	}
	return binary;
}

int main(int argc, char** argv) {
	double x = 0.101;
	string y = printBinary(x);
	cout << "Binary:" << y << endl;
	
	return 0;
}
