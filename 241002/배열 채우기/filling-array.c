#include <stdio.h>
int a;
int list[10];
int count = 0;
int main() {
    for(int i=0; i<10; i++){
        scanf("%d", &a);
        if (a == 0) break;
        else {
            list[count++] = a;

        }
    }
    for(int j=count-1; j>=0; j--){
        printf("% d", list[j]);
    }
    
    return 0;
}