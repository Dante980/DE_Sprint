#include <iostream>
#include <string>
using namespace std;

int main() {
	float x = -4, y;
	while (x < 4.5){
		cout << "x = " << to_string(x) << " y = " << to_string(-2 * x * x - 5 * x - 8) << endl;
		x += 0.5;
	}
	return 0;
}
