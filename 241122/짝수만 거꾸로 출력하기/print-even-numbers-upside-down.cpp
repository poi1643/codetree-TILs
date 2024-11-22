#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n,m[100];
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> m[i];
    }
    for(int j = 0; j < n; j++){
        if(m[n-j-1]%2 == 0) cout << m[n-j-1] << ' ';
    }
    return 0;
}