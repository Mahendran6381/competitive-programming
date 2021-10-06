#include <iostream>
#include <vector>
#include <bits/stdc++.h>
int indexof(int K, vector<int> v)
{
    auto it = find(v.begin(), v.end(), K);

    // If element was found
    if (it != v.end())
    {

        // calculating the index
        // of K
        int index = it - v.begin();
        return index + 1;
    }
    else
    {
        // If the element is not
        // present in the vector
        return -1;
    }
}

int main()
{
    vector<int> arr;
    vector<int> ans;
    int n, k, c;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> k;
        arr.push_back(k);
    }
    for (int j = 1; j < n + 1; j++)
    {
        c = indexof(j, arr);
        ans.push_back(c);
    }
    for (std::vector<char>::const_iterator i = ans.begin(); i != ans.end(); ++i)
    {
        std::cout << *i << ' ';
    }
}