#include <iostream>
using namespace std;
int main()
{
    int n, m, i, j, k, ans = 0;
    cin >> n;
    int arr[n];
    int **arr = new int *[n];
    for (i = 0; i < n; i++)
    {
        cin >> m;
        arr[i] = new int *[m];
        for (j = 0; j < m; j++)
        {
            cin >> k;
            arr[i][j] = k;
        }
    }
    cout << arr[0];
}