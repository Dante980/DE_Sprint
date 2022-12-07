#include <iostream>
using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	// вводим числа
	if (a > b){
		// первое число больше второго
		cout << a << " greater then " << b;
		return 0;
	}
	if (a < b){
		// второе число больше первого
		cout << b << " greater then " << a;
		return 0;
	}
	// если первое равно второму
	cout << "Digits are eaqual";
	return 0;
}
