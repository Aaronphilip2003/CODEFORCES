#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int main() 
{
    int minimum=0;
    string a, b;
    cin >> a >> b;
    minimum=std::min(a.length(),b.length());
    for (int i = 0; i < minimum; i++) 
    {
        if (a[i] < 92)
        {
            a[i] += 32;
        }
        if (b[i] < 92)
        {
            b[i] += 32;
        }
    }
    if (a < b) 
    {
        cout << -1;
    } 
    else if (a > b)
    {
        cout << 1;
    } 
    else if (a == b)
    {
        cout << 0;
    }

    return 0;
}