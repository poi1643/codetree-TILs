#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            if(i == 0 || i == n-1 || j < i|| j == n-1)  cout << "* ";
            else cout << "  ";
        }
        cout << '\n';
    }
    return 0;
}