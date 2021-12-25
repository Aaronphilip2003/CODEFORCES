#include<iostream>
using namespace std;

int main()
{
    int n,k,i,j;
    cin>>n>>k;
    char number[1000000];
    cin>>number;
    if(k==0)
    {
        cout<<number;
        return 0;
    }
    if(n==1 && k>=1)
    {
        cout<<"0";
        return 0;
    }
    if(number[0]!='1')
    {
        j=1;
        number[0]='1';
    }
    else
        j=0;
    for(i=1; i<n && j<k; i++)
    {
        if(number[i]=='0')
            continue;
        else
        {
            number[i]='0';
            j++;
        }
    }
    cout<<number<<endl;
    return 0;
}
