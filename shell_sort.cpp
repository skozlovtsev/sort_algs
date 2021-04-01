#include <iostream>
#include <array>
#include <ctime>
#define N 300

using namespace std;

int* shell_sort(int* arr, int size) {
	int step;
	step = size / 2;
	while (step > 0) {
		for (int i = 0; i < size; i += step)
			for (int j = i + step; j < size; j += step) {
				if (arr[i] > arr[j]) {
					int sw = arr[i];
					arr[i] = arr[j];
					arr[j] = sw;
				};
			};
		step = step / 2;
	};
	return arr;
};


int main(){
	int list[10] = { 4, 2, 9, 6, 7, 1, 5, 3, 8, 0 };
	int l_list[N];
	srand(time(nullptr));
	for (int i = 0; i < N; i++) {
		l_list[i] = rand() % 600;
	};
	int *sorted_list = shell_sort(l_list, N);
	for (int i = 0; i < N; i++) {
		cout << l_list[i] << " ";
	};
	cout << endl;
	for (int i = 0; i < N; i++) {
		cout << sorted_list[i] << " ";
	};
	return 0;
}
