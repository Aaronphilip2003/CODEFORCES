#include<iostream>
#include<algorithm>
#include<vector>
#include<string.h>
typedef long long ll;
using namespace std;
int main()
{
    ll testcases=0;
    cin>>testcases; 
    while(testcases!=0)
    {
        ll n=0;
        cin>>n;
        if (n==1)
        {
            cout<<1<<endl;
        }
        else if(n==2)
        cout<<2<<" "<<3<<endl;
        else
        {
            for(int i=2;i<=n+1;i++)
            {
                cout<<i<<" ";
            }
        }
        testcases--;
    }
    return 0;
}
