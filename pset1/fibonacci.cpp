#include <iostream>
#include <chrono>
#include <iomanip>

using namespace std;

int recursiveFib(int n)
{
   if (n <= 1)
      return n;
   else
      return (recursiveFib(n - 1) + recursiveFib(n - 2)) % 65536;
}

int iterativeFib(int n)
{
   int *arr = (int *)malloc((n + 1) * sizeof(int));
   arr[0] = 0;
   arr[1] = 1;

   for (int i = 2; i <= n; i++)
   {
      arr[i] = (arr[i - 1] + arr[i - 2]) % 65536;
   }

   int ans = arr[n];
   free(arr);

   return ans;
}

int *multiply(int base[4], int multiplier[4])
{
   int *product;
   product[0] = ((base[0] * multiplier[0]) + (base[1] * multiplier[2])) % 65536;
   product[1] = ((base[0] * multiplier[1]) + (base[1] * multiplier[3])) % 65536;
   product[2] = ((base[2] * multiplier[0]) + (base[3] * multiplier[2])) % 65536;
   product[3] = ((base[2] * multiplier[1]) + (base[3] * multiplier[3])) % 65536;
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
   int answer = result[1];
   return answer;
}

int main()
{
   int num = 100000;
   auto start = chrono::high_resolution_clock::now();
   cout << "F(" << num << ") = " << matrixFib(num) << "\n";
   auto end = chrono::high_resolution_clock::now();
   while (std::chrono::duration_cast<std::chrono::microseconds>(end - start).count() < 10000000)
   {
      num += 10000;
      start = chrono::high_resolution_clock::now();
      cout << "F(" << num << ") = " << matrixFib(num) << "\n";
      end = chrono::high_resolution_clock::now();
      cout << "Time: " << std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();
   }

   // cout << setw(3) << "n" << setw(13) << "Recursive" << setw(20) << "Recurs. Time (ms)" << setw(13) << "Iterative" << setw(20) << "Iter. Time (ms)" << setw(13) << "Matrix" << setw(20) << "Matr. Time (ms)" << endl
   //      << endl;
   // for (int i = 1; i <= 10; i++)
   // {
   //    int num = 5 * i;
   //    auto start = chrono::high_resolution_clock::now();
   //    int recurs = recursiveFib(num);
   //    auto end = chrono::high_resolution_clock::now();
   //    auto duration1 = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();

   //    start = chrono::high_resolution_clock::now();
   //    int iter = iterativeFib(num);
   //    end = chrono::high_resolution_clock::now();
   //    auto duration2 = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();

   //    start = chrono::high_resolution_clock::now();
   //    int matrix = matrixFib(num);
   //    end = chrono::high_resolution_clock::now();
   //    auto duration3 = std::chrono::duration_cast<std::chrono::microseconds>(end - start).count();

   //    cout << setw(3) << num << setw(13) << recurs << setw(20) << duration1 << setw(13) << iter << setw(20) << duration2 << setw(13) << matrix << setw(20) << duration3 << endl;
   // }
}
