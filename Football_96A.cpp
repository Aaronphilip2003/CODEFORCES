#include<iostream>
#include<vector>
#include<string>
#include<string.h>
typedef long long ll;
using namespace std;
int main()
{
    string a;
    cin>>a;
    ll count=1;
    for(int i=1;i<=a.length();i++)
    {
        if (a[i]==a[i-1])
        {
            count++;
            if (count==7)
            {
                cout<<"YES"<<endl;
                return 0;
            }
        }
            else
            {
                count=1;
            }
        }
        cout<<"NO"<<endl;
        return 0;
    }
// 1000000001
