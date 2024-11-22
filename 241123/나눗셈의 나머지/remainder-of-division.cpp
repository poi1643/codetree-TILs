#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, sum = 0, i, n[100] = {}, count[10] = {};
    cin >> a >> b;
    for(i = 0; a > 1; i++){
        n[i] = a%b;
        a = a/b;
    }
    for(int j = 0; j < i; j++){
        count[n[j]]++;
    }
    for(int j = 0; j < 10; j++){
        sum += count[j]*count[j];
    }
    cout << sum;

    return 0;
}