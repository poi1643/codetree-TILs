#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    bool nnn = true;
    for(int i = 2; i < n; i++){
        if(n%i == 0) nnn = false;
    }
    if(nnn) cout << 'P';
    else cout << 'C';
    return 0;
}