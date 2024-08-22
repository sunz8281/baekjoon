#include <stdio.h>

int memo0[41] = {1};
int memo1[41] = {0, 1};

void f(int n){
    if(memo0[n]||memo1[n]) return; //메모 n번째에 값이 있으면 리턴

    if(memo0[n-1]==0&&memo1[n-1]==0) f(n-1); //메모 n-1에 값이 없다면 f(n-1)
    if(memo0[n-2]==0&&memo1[n-2]==0) f(n-2); //메모 n-2에 값이 없다면 f(n-2)
        

    memo0[n] = memo0[n-1]+memo0[n-2]; //메모0 n번째 값 = n-1번째 + n-2번째
    memo1[n] = memo1[n-1]+memo1[n-2]; //메모1 n번째 값 = n-1번째 + n-2번째
    return;
}

int main(void){
    int t, n;
    scanf("%d", &t);
    for(int i=0; i<t; i++){
        scanf("%d", &n);
        f(n);
        printf("%d %d\n", memo0[n], memo1[n]);
    }
    return 0;
}