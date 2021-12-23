#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int n=0;
    cin>>n;
    char s[10000];
    cin>>s;
    int counts=0;
    int countf=0;
    
    for(int i=0;i<strlen(s)-1;i++)
    {
        if (s[i]=='S' && s[i+1]=='F')
        {
            counts++;
        }
        else if(s[i]=='F' && s[i+1]=='S')
        {
            countf++;
        }
    }

    if(counts>countf)
    {
        cout<<"YES"<<endl;
    }
    else if(countf>counts)
    {
        cout<<"NO"<<endl;
    }
    else
    {
        cout<<"NO"<<endl;
    }


    return 0;
}

// s--->f good ---> seattle
