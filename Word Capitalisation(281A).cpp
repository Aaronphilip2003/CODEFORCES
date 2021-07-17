#include<iostream>
using namespace std;

int main()
{
    int buffer;
    string name;
    string s2;
    cin>>name;
    int length;
    length=name.size();
    char ch1=name.at(0);
    ch1=toupper(ch1);
    for(int i=1;i<length;i++)
    {
        s2=s2+name[i];
    }
    cout<<(ch1+s2)<<endl;



    cin>>buffer;
    return 0;
}