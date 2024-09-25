//알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 
//주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main(void)
{
    char c;
    scanf("%c", &c);
    printf("%d", c);
    
    return 0;
}