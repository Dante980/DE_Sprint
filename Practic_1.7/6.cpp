#include <iostream>
using namespace std;

int main() {
	int a = 0, max_ = 0;
	/*while (cin >> a){
		if (a > max_){
			max = a
		}
	}*/
	// цикл с пост условием - мой любимый. ” теб€ цикл провер€ет условие после первой итерации. ¬ данном случае не оптимален дл€ данной задачи, так что грустно.
	do{
		if (a > max_){
			max_ = a;
		}
	} while (cin >> a);
	cout << max_;
	cout << " - is max";
	return 0;
}
