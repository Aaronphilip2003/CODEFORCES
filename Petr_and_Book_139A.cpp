#include<iostream>
#include<vector>
using namespace std;
typedef long long ll;
int main()
{
    ll n=0;
    vector<ll> pagesperday(7);
    cin>>n;
    ll finalans=0;
    for(auto &it: pagesperday) cin>>it;

    ll i=0;
    ll k=pagesperday[0];

    while(k<n)
    {
        i++;
        i=i%7;
        k+=pagesperday[i];
    }
    cout<<i+1<<endl;


    return 0;
}
