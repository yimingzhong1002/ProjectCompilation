// // memory model today, Jan 23rd
#include<stdio.h>
#include<stdlib.h>
// #define ARRAY_ELEMENTS 3

// double divide_2(int a, int b)
// {
//     // return the result of a/b
//     double result;

//     result=(double)a/(double)b;         // when using miced data types (numeric), always tell the compiler what you want!
// // explicit type casting
//     return result;
// }

// int main()
// {
//     char c='A';
//     int x;
//     float floaty[ARRAY_ELEMENTS];
//     int y;
//     double r;
//     char d='Z';         // reserved boxes number is 5 variables + number of array elements + returned int


//     // x=7;
//     // y=3;

//     // r=divide_2(x,y);
//     // printf("The result is %f\n", r);

//     // arrays in C :)
//     // single data type, 
//     // type name [#elements];

//     for(int i=0; i<7; i++)
//     {
//         x=i;
//         y=i*i;
//         floaty[i]=y*1.4142;
        
//     }

//     for(int i=0; i<7; i++)
//     {
//         printf("The number at index %d is %f\n",i,floaty[i]);
        
//     }
// }



int main()
{
    int array[10];
    int i=1;
    for (i=1; i<11; i++)
    {
        printf("array[%d]=%d*pi\n", i-1, i);
    }
    return 0;
}
