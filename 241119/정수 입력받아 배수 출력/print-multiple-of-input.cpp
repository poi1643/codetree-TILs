#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    for(int k, i = n; k<5; i++ ){
        if(i%n == 0 ){
            cout << i << ' ';
            k++;
        }
    }
    return 0;
}