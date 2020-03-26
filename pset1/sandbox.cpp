#include <iostream>
#include <chrono>
#include <iomanip>
#include <math.h>

using namespace std;

int *multiply(int base[4], int multiplier[4])
{
   int *product;
   product = new int[4];

   product[0] = (base[0] * multiplier[0]) + (base[1] * multiplier[2]);
   product[1] = (base[0] * multiplier[1]) + (base[1] * multiplier[3]);
   product[2] = (base[2] * multiplier[0]) + (base[3] * multiplier[2]);
   product[3] = (base[2] * multiplier[1]) + (base[3] * multiplier[3]);
   return product;
}

int *exponent(int base[], int n)
{
   if (n == 1)
   {
      return base;
   }

   int *next;
   next = exponent(base, n / 2);

   if (n % 2 == 1)
   {
      return multiply(multiply(next, next), base);
   }
   else
   {
      return multiply(next, next);
   }
}

int matrixFib(int n)
{
   int base[4] = {0, 1, 1, 1};
   int *result;
   result = exponent(base, n);

   cout << result[0] << " " << result[1] << " " << result[2] << " " << result[3];
   return 0;
}

int main()
{
   matrixFib(5);
   // cout << "Matrix result: " << (matrixFib(3) % 65536) << "\n";
}
