#include<iostream>
#include<vector>
#include<algorithm>
typedef long long ll;
using namespace std;
int main()
{
    ll testcases;
    cin>>testcases;
    while(testcases!=0)
    {
        ll l,r;
        cin>>l>>r;
        cout<<l<<" "<<2*l<<endl;
        testcases--;
    }
    return 0;
}
