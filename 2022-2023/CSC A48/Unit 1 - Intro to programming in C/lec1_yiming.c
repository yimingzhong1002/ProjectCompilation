/*
* This is our very first program in C
*
* Written by ALL OF US (c)
*/

/*
*
*
*
*
*   As many comments as I like
* 
*
*/

// This is a single line comment

#include<stdio.h>       //Standard Input/Output
#include<stdlib.h>      //Standard Library
#include<math.h>        //Always include a math header when defining symbols like PI

#define PI 3.1415926535     //define symbol always above int main()

double function1(double a, double b, char c)
{
    // this function multiplies a and b, and then
    // prints a,b,a*b,c
    // return a*b

    double d=0;      // defaulted as 0.0

    printf("%f, %f, %f, %c\n", a, b, a*b, c);

    d=a*b;
    return d;
}

// now function1 is built, later it would be called on to execute outcomes

int main()
{
    // function header, tells me what this does: always the first step
    // general idea of functionality
    // inputs
    // what it returns (if any)
    // maybe anything interesting I should pay attention to

// need to declare all variables I want to use
// WHY?

int a=0, b=0;       // should always assign meaningfull variable name
int c=5;
double d=2;
char f='p';

d=PI*2.0;       // compiler will see d=3.1415926535*2.0
printf("2 times pi = %f\n", d);

// Call function1() and print out what it returns:
d=function1(7,2.1,'3');
printf("The function returned %f\n",d);

if (fabs(d-14.7) < .00000000001) printf("We solved it!\n");
else printf("No... :(\n");

return 0;
// const float pi=3.1415926535; could do this as const float or define PI header above int main()
}