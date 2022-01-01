#include<iostream>
#include<algorithm>
using namespace std;
 
int main()
{
    int t;
    cin>>t;
    while(t!=0)
    {
        int a,b,n,count=0;
        cin>>a>>b>>n;
        while(a<=n)
        {
            if(a>b)
            {
                swap(a,b);
            }
            a=a+b;
            count++;
        }
        cout <<count<< endl;
        t-=1;
    }
}
