#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 1; j < n - i; j++ ) cout << ' ';
        for(int k = 0; k < i*2+1; k++) cout << '*';
        cout << '\n';
    }
    for(int i = 1; i < n; i++){
        for(int j = 0; j < i; j++) cout << ' ';
        for(int k = 0; k < (n-i)*2-1; k++) cout << '*';
        cout << '\n';
    }
    return 0;
}