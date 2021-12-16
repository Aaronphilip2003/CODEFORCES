#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;
typedef long long ll;
int main() 
{
	ll n=0;
	ll k=0;
	cin>>n>>k;
	ll x=1;
	vector<ll> v1;
	for(ll i=k-1;i>0;i--)
	{
		if((n%i)==0)
		{
			cout<<((n/i)*k)+i<<endl;
			break;
		}
	}
} 
