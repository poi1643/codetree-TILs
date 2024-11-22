#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    cin.tie(0), cout.tie(0), ios::sync_with_stdio(0);
    int n, cnt = 0;
    cin >> n;
    for(int i = 1; i <= n; i++){
        for(int j = 1; j <= n; j++){
            if(i%2 != 0) cnt = cnt + 1 ;  
            else cnt = cnt + 2;
            cout << cnt << ' ';
        }
        cout << '\n';
    }
    return 0;
}