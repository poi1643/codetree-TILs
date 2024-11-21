#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        for(int j = 1; j <= n; j++){
            if(i%2 == 0){
                cout << i*n+j << ' ';
            }
            else{
                cout << (i+1)*n-j+1 << ' ';
            }
        }
        cout << '\n';
    }
    return 0;
}