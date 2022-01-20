#include <iostream>
#include <vector>
using namespace std;
int diversity(vector<int>v)
{
    int count{1};
    sort(v.begin(),v.end());
    for(int i = 1; i < v.size(); i++)
    {
        if(v[i] == v[i-1])
            v[i] = -v[i];
    }
    sort(v.begin(),v.end());
    for(int i = 1; i < v.size(); i++)
    {
        if(v[i] != v[i-1])
            count++;
    }
    return count;
}
int main()
{
    int test_cases, n, x;
    cin>>test_cases;
    while(test_cases--)
    {
        vector<int>v;
        cin>>n;
        while(n--)
        {
            cin>>x;
            v.push_back(abs(x));
            
        }
        cout<<diversity(v)<<'\n';
    }
}
