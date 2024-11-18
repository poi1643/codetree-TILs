#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b;
    cin >> a >> b;
    cout.precision(2);
    cout << fixed << (double)(a+b)/(a-b);
    return 0;
}