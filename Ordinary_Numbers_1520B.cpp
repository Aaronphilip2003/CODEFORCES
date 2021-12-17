#include<bits/stdc++.h>
#include<iostream>
#include<vector>
#include<algorithm>
#define ll long long
#define pb push_back
using namespace std;
int main()
{
    int t;
    ll n;
    cin>>t;
    while(t--){
        cin>>n;
        ll a = 0,ans = 0;
        vector<ll>v;
        for(int i = 1; i <= 9; i++) {
            a = i;
            while(a < 2e9) {
                v.pb(a);
                a = 10 * a + i;
            }
        }
        sort(v.begin(),v.end());
        for(int i=0; i<v.size(); i++){
            if(v[i] <= n){
                ans++;
            }
        }
        cout<<ans<<endl;
    }

    return 0;
}
