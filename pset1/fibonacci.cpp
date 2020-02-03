#include <iostream>
#include <chrono>

using namespace std;

int recursiveFib(int n)
{
   if (n <= 1)
      return n;
   else
      return recursiveFib(n - 1) + recursiveFib(n - 2);
}

int iterativeFib(int n)
{
   int arr[n + 1];
   arr[0] = 0;
   arr[1] = 1;

   for (int i = 2; i <= n; i++)
   {
      arr[i] = arr[i - 1] + arr[i - 2];
   }

   return arr[n];
}

// void multiply(int n)
// {
//    int temp[2][2] = {{0, 1}, {1, 1}};
//    int result[2][2];
//    for (int j = 0; j < 2; j++)
//    {
//       for (int k = 0; k < 2; k++)
//       {
//          for (int l = 0; l < 2; l++)
//          {
//             result[j][k] += temp[j][l] * base[l][k];
//          }
//       }
//    }
// }

int matrixFib(int n)
{
   int base[2][2] = {{0, 1}, {1, 1}};
   int first[2][1] = {{0}, {1}};

   // multiply(n);

   return 0;
}

int main()
{
   int num;
   cout << "Enter a number: ";
   cin >> num;
   auto start = chrono::high_resolution_clock::now();
   cout << "Recursive result: " << (recursiveFib(num) % 65536) << "\n";
   auto end = chrono::high_resolution_clock::now();
   auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
   std::cout << "The recursive method executed in " << duration << " nanoseconds. \n";

   start = chrono::high_resolution_clock::now();
   cout << "Iterative result: " << (iterativeFib(num) % 65536) << "\n";
   end = chrono::high_resolution_clock::now();
   duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
   std::cout << "The iterative method executed in " << duration << " nanoseconds. \n";

   // cout << "Iterative result: " << (iterativeFib(num) % 65536);
   // cout << "Matrix result: " << (matrixFib(num) & 65536);
}
