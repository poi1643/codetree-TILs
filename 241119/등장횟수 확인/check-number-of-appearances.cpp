#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a,b,c,d,e;
    cin >> a >> b >> c >> d >> e;
    int cnt = 0;
    if(a%2 == 0) cnt++;
    if(b%2 == 0) cnt++;
    if(c%2 == 0) cnt++;
    if(d%2 == 0) cnt++;
    if(e%2 == 0) cnt++;
    cout << cnt;

    return 0;
}