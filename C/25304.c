#include <stdio.h>

int main(void){
    int x, n, a, b, result=0;
    scanf("%d", &x);
    scanf("%d", &n);
    for(int i=0; i<n; i++){
        scanf("%d %d", &a, &b);
        result += a*b;
    }
    printf(result==x? "Yes":"No");
    return 0;
}