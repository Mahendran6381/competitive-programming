#include <iostream>
using namespace std;
int main()
{
    int n, k, i, j, arr[1000];
    int ans = 0;
    cin >> n >> k;
    int a;
    for (i = 0; i < n; i++)
    {
        cin >> a;
        arr[i] = a;
    }
    for (i = 0; i < n; i++)
    {
        if (arr[i] >= arr[k] && arr[i] > 0)
        {
            ans = ans + 1;
        }
    }
    cout << ans;
}