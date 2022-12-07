#include <iostream>
using namespace std;
// ������ ��� ����� ��� ������
struct student{
	string LastName;
	string Initials;
	int GroupNumber;
	int Yspevaemost[6];
};


student Array_[3];
// ������ ��� ������ ��� ����������
void boubble_sort(int n){
	// ����������� ����������: ����� ������� �������� ���������� �� ���, ����� ������ �� �����������
	for(int i = 1; i < n; ++i){
		for(int r = 0; r < n-i; r++)
		{
			if(Array_[r].Yspevaemost[0] > Array_[r+1].Yspevaemost[0])
			{
				student temp = Array_[r];
				Array_[r] = Array_[r+1];
				Array_[r+1] = temp;
			}
		}
	}
}

student enter_student(int i){
	// ������ ������ �������� � ������
	int a;
	student single_student;
	cout << "Enter lastname of " << i << "-st student: ";
	cin >> single_student.LastName;
	cout << "Enter initials of " << i << "-st student: ";
	cin >> single_student.Initials;
	cout << "Enter Group Number of " << i << "-st student: ";
	cin >> single_student.GroupNumber;
	int temp;
	for (int j = 1; j < 6; j++){
		cout << "Enter count of " << j << ": ";
		cin >> a;
		single_student.Yspevaemost[j] = a;
		// � ������� ������� ������� �������� ��� ������� ����
		single_student.Yspevaemost[0] += a * j;
		temp += a;
	}
	single_student.Yspevaemost[0] /= temp;
	return single_student;
}
void cout_students(int jj){
	// ������� ���������
	for (int i = 0; i < jj; i++){
		if (Array_[i].Yspevaemost[1] == 0 && Array_[i].Yspevaemost[2] == 0 && Array_[i].Yspevaemost[3] == 0){
			// ������� ����������� ������ ���� � �������� ����� ������ ������ 4 ��� 5
			cout << Array_[i].LastName << " ";
			cout << Array_[i].Initials << " ";
			cout << Array_[i].GroupNumber << " ";
			for (int j = 1; j < 6; j++){
				cout << Array_[i].Yspevaemost[j] << " ";
			}
			cout << endl;
		}
	}
}


int main(){
	for (int i = 0; i < 3; i++){
		Array_[i] = enter_student(i);
	}
	cout << "_---------------_" << endl;
	boubble_sort(3);
	cout_students(3);
	return 0;
}
