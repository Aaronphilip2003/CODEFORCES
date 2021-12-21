#include<iostream>
#include<set>
using namespace std;
int main(){
	int testcases;
	cin>>testcases;
	while(testcases!=0){
		int n;
		cin>>n;
        set<int> a;
	for(int i=1;i*i<=n;i++) 
    {
        a.insert(i*i);
    }
	for(int i=1;i*i*i<=n;i++) 
    {
        a.insert(i*i*i);
    }
    cout<<(int)a.size()<<endl;
    testcases--;
	}
	return 0;
}
