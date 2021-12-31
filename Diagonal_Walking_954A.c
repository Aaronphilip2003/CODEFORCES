#include <bits/stdc++.h>
using namespace std;
 
int main (void)
{
 
    char str[101];
    int len,i,k;
 
    while (scanf ("%d %s",&len,str) != EOF)
    {
        k = 0;
 
        for (i=0; i<len; i++)
        {
            if ((str[i] == 'R' && str[i+1] == 'U') || (str[i] == 'U' && str[i+1] == 'R'))
                i+=1;
 
            ++k;
        }
 
        printf ("%d\n",k);
    }
 
    return 0;
}
