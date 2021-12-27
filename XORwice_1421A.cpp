#include<iostream>
#include<algorithm>
typedef long long ll;
using namespace std;
int main()
{
    ll testcases,a,b;
    cin>>testcases;
    
    while(testcases!=0)
    {
        cin>>a>>b;
        cout<<(a^b)<<endl;
        testcases--;
    }
    
    return 0;
}

// 800 rated program
