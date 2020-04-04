#include <iostream>
#include <random>

using namespace std;

long bil = 1000000000;
int trials = 100;

int main(int arc, char *argv[])
{
    // Assume that there will be no bin with more than 10,000 balls
    int loads[25] = {0};
    int maxLoads[25] = {0};

    if (atoi(argv[1]) == 0)
    {
        cout << "TRADITIONAL EXPERIMENT: \n \n";

        for (int m = 0; m < trials; m++)
        {
            // cout << "new trial started \n";
            // Assume that the first toss lands in a previously empty bucket
            loads[1] = 1;
            int max = 1;
            bool trial = false;

            // 999,999,999 throws left
            for (int i = 0; i < bil - 1; i++)
            {
                int num = rand() % bil;
                int pos = 0;
                bool toss = false;

                // Ball lands in a non-empty bin
                for (int j = 1; j <= max; j++)
                {
                    if (num >= pos && num < pos + loads[j])
                    {
                        loads[j]--;
                        loads[j + 1]++;
                        if (j + 1 > max)
                        {
                            max = j + 1;
                        }
                        toss = true;
                        break;
                    }
                    pos += loads[j];
                }

                // Ball lands in a previously empty bin
                if (toss == false)
                {
                    loads[1]++;
                }
            }

            for (int k = 0; k < 25; k++)
            {
                cout << loads[k] << " ";
            }

            // Reset values for new trial
            for (int k = 0; k < 25; k++)
            {
                loads[k] = 0;
            }

            cout << "Max for trial #" << m + 1 << ": " << max << "\n";
            maxLoads[max]++;
        }
    }
    else if (atoi(argv[1]) == 1)
    {
        cout << "MODIFIED EXPERIMENT: \n \n";

        for (int m = 0; m < trials; m++)
        {
            // Assume that the first toss lands in a previously empty bucket
            loads[1] = 1;
            int max = 1;
            int maxpos = 1;

            // 999,999,999 throws left
            for (int i = 0; i < bil - 1; i++)
            {
                int num1 = rand() % bil;
                int num2 = rand() % bil;

                // One of the options is to throw into an empty bin
                if (num1 > maxpos || num2 > maxpos)
                {
                    loads[1]++;
                    maxpos++;
                }

                // Only option is to throw into a non-empty bin
                else
                {
                    // We go with the lower number, because lower numbers correspond with lower loads
                    int num = num1;
                    if (num2 < num1)
                    {
                        num = num2;
                    }

                    int pos = 0;
                    for (int j = 1; j <= max; j++)
                    {
                        if (num >= pos && num < pos + loads[j])
                        {
                            loads[j]--;
                            loads[j + 1]++;
                            if (j + 1 > max)
                            {
                                max = j + 1;
                            }
                            break;
                        }

                        pos += loads[j];
                    }
                }
            }

            // Reset values for new trial
            for (int k = 0; k < 25; k++)
            {
                loads[k] = 0;
            }

            cout << "Max for trial #" << m + 1 << ": " << max << "\n";
            maxLoads[max]++;
        }
        for (int k = 0; k < 25; k++)
        {
            cout << maxLoads[k] << " ";
        }
    }
}
