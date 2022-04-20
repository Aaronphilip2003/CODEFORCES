#include<iostream>
#include<vector>
#include<algorithm>
typedef long long ll;
using namespace std;
int main()
{
    ll testcases=0;
    cin>>testcases;
    while (testcases!=0)
    {
        vector<ll>num(3);
        for(auto &it: num) cin>>it; // way to input a vector
        sort(num.begin(),num.end());
        if(num[1]!=num[2])
        {
            cout<<"NO"<<endl;
        }
        else
        {
            cout<<"YES"<<endl;
            cout<<num[0]<<" "<<num[0]<<" "<<num[2]<<endl;
        }
        testcases--;
    }
    return 0;
}
