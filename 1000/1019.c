#include <stdio.h>
int main(void){
    int y, m, d;
    scanf("%d.%d.%d", &y, &m, &d);
    printf("%d.%02d.%02d", y, m, d);
    return 0;
}