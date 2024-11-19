#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int a, b, sum = 0;
    cin >> a >> b;
    if(a > b ){
        for(int i = b; i <= a; i++ ){
            if(i%5 == 0) sum += i;
        }
    }else if( a < b){
        for(int i = a; i <= b; i++ ){
            if(i%5 == 0) sum += i;
        }
    }else{
        sum = a;
    }
    cout << sum;
    return 0;
}