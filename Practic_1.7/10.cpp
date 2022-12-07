#include <iostream>
#include <string.h>
using namespace std;
// наш новый тип данных
struct train{
	string ResultPoint;
	int TrainNumber;
	int TimeToStart;
};

train Array_[3];
// объ€вим массив как глобальный
void boubble_sort(int n){
	// ѕузырькова€ сортировка
	for(int i = 1; i < n; ++i){
		for(int r = 0; r < n-i; r++)
		{
			if(Array_[r].TrainNumber < Array_[r+1].TrainNumber)
			{
				train temp = Array_[r];
				Array_[r] = Array_[r+1];
				Array_[r+1] = temp;
			}
		}
	}
}

void boubble_sort_by_point(int n){
	// ѕузырькова€ сортировка дл€ пункта назначени€
	for(int i = 1; i < n; ++i){
		for(int r = 0; r < n-i; r++)
		{
			int jjjj = 0;
			if (Array_[r].ResultPoint == Array_[r+1].ResultPoint){
				// провер€ем равны ли пункты назначени€
				if (Array_[r].TimeToStart > Array_[r+1].TimeToStart){
					train temp = Array_[r];
					Array_[r] = Array_[r+1];
					Array_[r+1] = temp;
				}
			} else while (true){
				// »наче посимвольно провер€ем, где номер символа больше. «десь будет вылетать, к примеру в таком случае: Zdar  Zdarova
				char tt = Array_[r].ResultPoint[jjjj], hh = Array_[r + 1].ResultPoint[jjjj];
				if (tt < hh)  {
					train temp = Array_[r];
					Array_[r] = Array_[r+1];
					Array_[r+1] = temp;
					break;
				} else if (tt != hh){
					break;
				}
				jjjj += 1;
			}
		}
	}
}

/*
void cout_all_trains(int jj){
	for (int i = 0; i < jj; i++){
		cout << Array_[i].ResultPoint << " ";
		cout << Array_[i].TrainNumber << " ";
		cout << Array_[i].TimeToStart << " ";
		cout << endl;
	}
}
*/


train enter_train(int i){
	// ввод нашего одного поезда  
	int a;
	train single_train;
	cout << "Enter result point of " << i << "-st train: ";
	cin >> single_train.ResultPoint;
	cout << "Enter the number of " << i << "-st train: ";
	cin >> single_train.TrainNumber;
	cout << "Enter when the " << i << "-st train is leaving: ";
	string twari;
	cin >> twari;
	if (twari.length() > 5){
		cout << "Haha, try again, small digit :)))))))" << endl;
		single_train = enter_train(i);
	} else{
		single_train.TimeToStart = ((int)twari[0] - 48) * 600 + ((int)twari[1] - 48) * 60 + ((int)twari[3] - 48) * 10 + ((int)twari[4] - 48);
		cout <<  ((int)twari[0] - 48) * 600 + ((int)twari[1] - 48) * 60 + ((int)twari[3] - 48) * 10 + ((int)twari[4] - 48) << endl;
	}
	
	return single_train;
}

void cout_train_by_number(int jj, int number){
	bool founded = 1;
	for (int i = 0; i < jj; i++){
		if (Array_[i].TrainNumber == number){
			cout << Array_[i].ResultPoint << " ";
			cout << Array_[i].TrainNumber << " ";
			cout << Array_[i].TimeToStart / 60 << ":" << Array_[i].TimeToStart % 60;
			cout << endl;
			founded = 0;
			break;
		}
	}
	if (founded){
		cout << "There is no train with number like this. Try again! So, your number is: ";
		cin >> number;
		cout << endl;
		cout_train_by_number(jj, number);
	}
}

int main(){
	for (int i = 0; i < 3; i++){
		Array_[i] = enter_train(i);
	}
	cout << "_---------------_" << endl;
	boubble_sort_by_point(3);
	
	int number;
	cout << "Enter the number of train which you want to see: ";
	cin >> number;
	cout << endl;
	cout_train_by_number(3, number);
	return 0;
}
