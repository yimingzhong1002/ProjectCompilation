// // Jan26th arrays and strings
// // arrays: fixed size, fixed data type, indexes used access data
// // array entries: each one in a separate box, boxes have to be contiguous

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    // create an array of size 100
    // fill this array with the fibonacci numbers (the first 100)
    // print backwards
    double array[152];
    double sum=0;
    array[0]=0;
    array[1]=1;
    for (int i=0; i<=149; i++)
    {
        array[i+2]=array[i+1]+array[i];
        if (fmod(array[i],2.0)!=0)
        {
            sum=sum+array[i];
        }
    }
    printf("The sum of all ODD Fibonacci numbers are %f\n", sum);

    
    // for (int i=149; i>=0; i--)
    // {
    //     printf("The  %d-th Fibonacci number is %f\n", i, array[i]);
    // }
    
    // return 0;
    // compute the sum of all ODD Fibonacci numbers, and print it :)
    // for (int i=1; i<=149; i=i+2)
    // {
    //     sum=sum+array[i];
    // }
    // printf("The sum of all ODD Fibonacci numbers are %f\n", sum);
    return 0;
}


#include<stdio.h>
#include<stdlib.h>

#define STR_LEN 1024        // compiler remembers STR_LEN is 1024

int main()
{
    char stringy[STR_LEN]="Hi there \n Starbucks is not good! \n Said Sean! \n Ok?";

    for (int i=0; i<STR_LEN; i++)
    {
        if (stringy[i]=='\0') break;
        if (stringy[i]==' ') printf("%c", '\n');
        else printf("%c", stringy[i]);
    }
    printf("%s\n", stringy);
    // take the string above, and print out word by word, each word in separate lines!
}