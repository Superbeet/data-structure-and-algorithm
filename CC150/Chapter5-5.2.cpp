#include <iostream> 
#include <string>
using namespace std; 

string printBinary1(double num){

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

string printBinary2(double num){

	if(num<0 or num>1)
		return "ERROR";

	string binary = ".";
	double frac = 0.5;

	while(num>0){

		if (binary.length() >= 32){
			return "ERROR";
		}

		if(num>1){
			binary = binary + "1";
			num = num - frac;
		} else {
			binary = binary + "0";
		}

		frac = frac/2;
		
	}
	return binary;
}

int main(){
	double x = 0.101;
	string y = printBinary1(x);
	cout << "Binary:" << y << endl;

	return 0;
}