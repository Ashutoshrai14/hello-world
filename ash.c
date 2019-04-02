#include<stdio.h>
#include<conio.h>

void main()
{
char s[]="india";
int i,j;
clrscr();
for(i=0;s[i];i++)
{
for(j=0;j<=i;j++)
printf("%c",s[j]);
printf("\n");
}
getch();
}
