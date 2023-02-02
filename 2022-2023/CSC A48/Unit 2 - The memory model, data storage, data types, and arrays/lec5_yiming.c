#include<stdio.h>

// void square(int *p)
// {
//     int x;
//     x=*p;           // 2. set x equals to the value which p points to, which is the value of my_int, 7
//     x=x*x;          // 3. the new x=x*x, which is 49
//     *p=x;           // 4. set the value which p points to as x, updated the new value of my_int as 49
// }
// int main()
// {
//     int my_int;
//     my_int=7;
//     square(&my_int);        // 1. in the square function, we call on the address of my_int, which sets p=&my_int
//     printf("The final value for my_int is: %d\n", my_int);
// }

#define STR_LEN 1024

void concatenate(char str1[STR_LEN], char str2[STR_LEN], char result[2*STR_LEN])
{
    // this function concatenates str1 and str2
    // C does no tcoopy, only get the boxes of str1 and str2
    // This function gets str1 @ 1234, str2 @ 4567

    // put the two strings into result, and return result
    int i=0;
    int j=0;

    while (str1[i]!='\0')
    {
        result[i]=str1[i];
        i++;
    }
    while (str2[j]!='\0')
    {
        result[i+j]=str2[j];
        j++;
    }
    // i did not add a delimiter to result!
    result[i+j]='\0';
    
    return;
}
int main()
{
    int array[5];
    char str1[STR_LEN]="Good ";         // If this is at #1234
    char str2[STR_LEN]="Morning!\n";   // thi si at #4567
    char res[STR_LEN*2]="";
    int a,b;

    printf("I know strings! %s\n", str1);

    concatenate(str1, str2, res);
    printf("The concatenated string is %s\n", concatenate(str1, str2, res));

    return 0;
}