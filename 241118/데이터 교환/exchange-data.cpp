#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a = 5, b = 6, c = 7, temp ;
    temp = b;
    b = a;
    a = c;
    c = temp;
    cout << a <<'\n'<< b << '\n' << c;
    return 0;
}