#include <iostream>
using namespace std;

int main() {
	int a, b;
	cin >> a >> b;
	// ������ �����
	if (a > b){
		// ������ ����� ������ �������
		cout << a << " greater then " << b;
		return 0;
	}
	if (a < b){
		// ������ ����� ������ �������
		cout << b << " greater then " << a;
		return 0;
	}
	// ���� ������ ����� �������
	cout << "Digits are eaqual";
	return 0;
}
