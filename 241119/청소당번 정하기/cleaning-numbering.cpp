#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, cnt1 = 0,cnt2 = 0,cnt3 = 0;
    cin >> n;

    for(int i = 0; i < n ; i++){
        if((i+1)%12 == 0 && i != 0){
            cnt3++;
        }else if((i+1)%3 == 0 && i != 0){
            cnt2++;
        }else if((i+1)%2 == 0 && i != 0){
            cnt1++;
        }
    }
    cout << cnt1 << ' ' << cnt2 << ' ' << cnt3;
    return 0;
}