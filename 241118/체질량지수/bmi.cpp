#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int h, w;
    double b;
    cin >> h >> w;
    cout.precision(0);
    b = (10000*w)/(h*h);
    cout << fixed << b;
    if( b >= 25 )
        cout << "\nObesity";
    return 0;
}