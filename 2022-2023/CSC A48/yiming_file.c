#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#define PI 3.14159265

// int function1(int month, int year)
// {
//     int month_year = 0;     

//     month_year = month*year;
//     return month_year;
// }
// int main()
// {

// int month=10;
// int year=2001;
// int month_year=0;

// month_year = function1(10, 2001);
// printf("My birthday is on %d, %d\n", month, year);
// printf("month year multiplier is %d\n", month_year);

// return 0;
// }

// int main()
// {
//     float d = PI;
//     printf("%1.0f \n", d);
//     printf("%1.1f \n", d);
//     printf("%1.2f \n", d);
//     printf("%1.3f \n", d);
//     printf("%1.4f \n", d);
//     printf("%1.5f \n", d);

//     return 0;
// }

//     int i;
//     for (i=0; i<10; i=i+1)
//     {                           // - start of for loop
//         printf("%d\n",i);
//     }                           // - end of the for loop
// return 0;

// float angle;



// for (angle=0.0; angle<2.0*PI; angle=angle+0.01)
// {
//     printf("%f\n", sin(angle));
// }
// }

// int i,j;

// for (i=0; i<10; i=i+1)
// {
//         for (j=0; j<i; j=j+1)
//         {
//             printf("%d\n", j);
//         }
//     printf("\n");
// }
// }

int main()
{
int i,j;

for (i=0; i<=100; i=i+1)
{
    for (j=1; j<=10; j=j+1)
    {
        if (i==j*j)
        {
            printf("%d = %d*%d\n", i, j, j);
        }
        else
        {
            continue;
        }
    }
}
}