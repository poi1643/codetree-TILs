#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, cnt = 0;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < i; j++) cout << "  ";
        for(int j = 0; j < n-i; j++) {
            if(cnt == 9) cnt = 0;
            cnt++;
            cout << cnt << ' ';
        }
        cout << '\n';
    }
    return 0;
}