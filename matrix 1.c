#include <stdio.h>
int main()
{
    int a[3],b[3],i,j,r[3][3];
    printf("Enter 1st metrix elemnts:");
    for(i=0; i<3; i++)
    {
        for(j=0; j<3; j++)
        {
            scanf("%d\t", &a[i][j]);
        }
    }
    
    printf("Enter 2st metrix elemnts:");
    for(i=0; i<3; i++)
    {
        for(j=0; j<3; j++)
        {
            scanf("%d\t", &b[i][j]);
        }
    }
    for(i=0; i<3; i++)
    {
        for(j=0; j<3; j++)
        {
            r[3][3]=a[3][3]+b[3][3];
        }
    }
    for(i=0; i<3; i++)
    {
        for(j=0; j<3; j++)
        {
            printf("%d\t", r[3][3]);
        }
    }
    return 0;




}