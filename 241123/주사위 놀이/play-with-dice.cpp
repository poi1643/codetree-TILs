#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int arr[10];
    int count[7] = {};
    for(int i = 0; i < 10; i++){
        cin >> arr[i];
        count[arr[i]]++;
    }

    for(int k = 1; k <= 6; k++){
        cout << k << " - " << count[k] << '\n';
    }
    return 0;
}