// Today we're learning about loops

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main()
{
    int counter;
    char c='A';
    int fake_char=0;
    // int temp=0;

    // for (counter=0; counter<10; counter=counter+1)
    // {
    //     printf("The counter is %d\n", counter);
    // }
    // initialization, condition to stop, increment

    // What kinds of variable data types can we use for counters?

    // C is freedom?

    // CHars are just numbers in [0, 255]
    // for (c='A'; c<'Z'; c=c+1)       // I expect the entire ASCII table to come out, if c<256
    // {
    //     printf("The char I got is %c\n",c);
    // }

    // for (c=0; c<256; c=c+1)       // I expect the entire ASCII table to come out, if c<256
    // {
    //     printf("The char I got is %d\n in decimal, and the corresponding character is %c\n",c, c);
    // }

    // for (fake_char=0; fake_char<256; fake_char=fake_char+1)       // I expect the entire ASCII table to come out, if c<256
    // {
    //     printf("The char I got is %d\n in decimal, and the corresponding character is %c\n",fake_char, fake_char);
    // }
    // for (short unsigned int test_int=1; test_int<8000000000; test_int++)
    // {
    //     if (test_int==0) break;
    //     temp=test_int;
    // }
    // printf("The largest number I could count to was %ud\n", temp);

    // Exercise:
    // Write a for loop that guesses (or estimates) the square root of 2 :)
    // You can't use math library
    double temp;
    for (double guess=1.0; guess<1.5; guess=guess+.00000001)
    {
        temp=guess*guess;
        if (fabs(temp-2.0)<.00000001) break;    // .001 works
        
    }
    printf("The current guess=%f, product is %f\n",guess,temp);
}