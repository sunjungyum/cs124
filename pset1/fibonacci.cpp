#include <iostream>
#include <chrono>
#include <iomanip>

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

// void multiply(int[] base)
// {
//    int multiplier[2][2] = {{0, 1}, {1, 1}};

//    for (int j = 0; j < 2; j++)
//    {
//       for (int k = 0; k < 2; k++)
//       {
//          base for (int l = 0; l < 2; l++)
//          {
//             base[j][k] += temp[j][l] * base[l][k];
//          }
//       }
//    }
// }

// int matrixFib(int n)
// {
//    int base[2][2] = {{0, 1}, {1, 1}};
//    int first[2][1] = {{0}, {1}};

//    for (int i = 0; i < n; i++)
//    {
//       multiply(base);
//    }

//    return 0;
// }

int main()
{
   cout << setw(3) << "n" << setw(13) << "Recursive" << setw(20) << "Recurs. Time (ns)" << setw(13) << "Iterative" << setw(20) << "Iter. Time (ns)" << setw(10) << "Matrix" << setw(20) << "Matr. Time (ns)" << endl
        << endl;
   for (int i = 1; i <= 10; i++)
   {
      int num = 5 * i;
      auto start = chrono::high_resolution_clock::now();
      int recurs = recursiveFib(num) % 65536;
      auto end = chrono::high_resolution_clock::now();
      auto duration1 = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();

      start = chrono::high_resolution_clock::now();
      int iter = iterativeFib(num) % 65536;
      end = chrono::high_resolution_clock::now();
      auto duration2 = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();

      cout << setw(3) << num << setw(13) << recurs << setw(20) << duration1 << setw(13) << iter << setw(20) << duration2 << setw(10) << "hi" << setw(20) << "0" << endl;
      // start = chrono::high_resolution_clock::now();
      // cout << "Matrix result: " << (iterativeFib(num) % 65536) << "\n";
      // end = chrono::high_resolution_clock::now();
      // duration = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start).count();
      // std::cout << "The iterative method executed in " << duration << " nanoseconds. \n";
   }
}
