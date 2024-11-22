#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin >> n;
    char a = 'A'-1;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < i; j++) cout << "  ";
        for(int j = 0; j < n - i; j++){ 
            if(a == 'Z') a = 'A' - 1;
            a = a + 1;
            cout << a << ' ';
        }
        cout << '\n';
    }
    return 0;
}