#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    double g[8], n;
    cout << fixed;
    cout.precision(1);
    for(int i = 0; i < 8; i++){
        cin >> g[i];
        n += g[i];
    }
    cout << n/8;
    return 0;
}