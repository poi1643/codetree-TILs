#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, cnt = 0, m[100],d[100];
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> m[i];
    }
    for(int i = 0; i < n; i++){
        if(m[i]%2 == 0){
            d[cnt++] = m[i];
            cout << d[cnt-1] << ' ';
        }
    }

    return 0;
}