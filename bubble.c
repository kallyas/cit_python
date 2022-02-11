// bubble sort in c
#include <stdio.h>
#include <stdlib.h>


void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}


int main(){
    int n, i, j;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int a[n];
    printf("Enter the elements: ");
    for(i = 0; i < n; i++)
        scanf("%d", &a[i]);

    // bubble sort
    for(i = 0; i < n; i++)
        for(j = 0; j < n-i-1; j++)
            if(a[j] > a[j+1])
                swap(&a[j], &a[j+1]);
    
    // print sorted array
    for(i = 0; i < n; i++)
        printf("%d ", a[i]);

    return 0;

}




