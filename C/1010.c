#include <stdio.h>

int memo[31][31];

int f(int n, int m){
    if(n==1) return m;
    if(n==m) return 1;
    if(memo[n][m]) return memo[n][m];
    return memo[n][m] = f(n-1, m-1) + f(n, m-1);
}

int main(void){
    int t, n, m;
    scanf("%d", &t);
    for(int i=0; i<t; i++){
        scanf("%d %d", &n, &m);
        printf("%d\n", f(n, m));
    }
    return 0;
}