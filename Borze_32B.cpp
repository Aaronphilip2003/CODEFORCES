#include <iostream>
#include<string>
using namespace std;
 
int main() {
 string s,ans;
 cin>>s;
int len=s.length();
for(int i=0;i<len;i++)
 
{
	if(s[i]=='.'){
		ans+='0';
	}
	if(s[i]=='-'&&s[i+1]=='.'){
		ans+='1';
		++i;
		
	}
	if(s[i]=='-'&&s[i+1]=='-'){
		ans+='2';
		++i;
	}
	
} 
 cout<<ans;
 
 
 
 	return 0;
}
