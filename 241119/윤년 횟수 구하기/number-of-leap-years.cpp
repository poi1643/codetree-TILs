#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, cnt=0;
    cin >> n;
    for(int i = 1; i < n; i++){
        if(i>100 && i%100 == 0 && i%400 != 0){}
        else if(i%4 == 0){
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}