#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a1, a2, b1, b2;
    cin >> a1 >> a2;
    cin >> b1 >> b2;
    if(a1==b1&&a2>b2 || a1>b1){
        cout << 'A';
    }else if(a1==b1&&a2<b2 || b1>a1){
        cout << 'B';
    }
    return 0;
}