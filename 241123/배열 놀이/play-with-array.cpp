#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n, q , nn[100] ={}, qn;
    cin >> n >> q;
    for(int i = 1; i <= n; i++){
        cin >> nn[i];
    }
    for(int i = 0; i < q; i++){
        int x,y;
        cin >> qn;
        cin >> x;
        if(qn == 1){
            cout << nn[x] << '\n';
        }else if(qn == 2){
            int c = 0;
            for(int j = 1; j <= n; j++){
                if(nn[j] == x){
                    c = j;
                    break;
                } 
            }
            cout << c << '\n';
        }else{
            cin >> y;
            for(int j = x; j <= y; j++) cout << nn[j] << ' ';
            cout << '\n';
        }
    }
    return 0;
}