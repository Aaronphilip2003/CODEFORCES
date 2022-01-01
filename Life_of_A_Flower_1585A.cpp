#include<iostream>
#define fl(i,n) for(int i=0;i<n;i++)
using namespace std;
typedef long long ll;
void solution()
{
    ll n;
    cin>>n;
    ll ans=1;
    ll arr[n];
    fl(i,n)cin>>arr[i];
    if(arr[0]==1)ans++;
    for(int i=1;i<n;i++)
    {
        if(arr[i]==0)
        {
            if(arr[i]==arr[i-1])
            {
                cout<<"-1\n";
                return;
            }
        }
        else
        {
            if(arr[i]==arr[i-1])
            ans+=5;
            else ans++;
        }
    }
    cout<<ans<<"\n";
}
int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        solution();
    }
    return 0;
}
