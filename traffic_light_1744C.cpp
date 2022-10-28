#include <iostream>
#include <vector>
#include <string>
#include<algorithm> 
#include<limits.h>
using namespace std;

int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n;
        char ch;
        string s;
        cin >> n;
        cin >> ch;
        cin >> s;

        if (ch == 'g')
        {
            cout << "0" << endl;
            continue;
        }
        vector<int> idxG, idxCh;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == ch)
            {
                idxCh.push_back(i);
            }
            else if (s[i] == 'g')
            {
                idxG.push_back(i);
            }
        }

        int ans = INT_MIN;

        for (int i = 0; i < idxCh.size(); i++)
        {
            auto it = upper_bound(idxG.begin(), idxG.end(), idxCh[i]);
            if (it == idxG.end())
            {
                int dist = n - idxCh[i] + idxG[0];
                ans = max(ans, dist);
            }
            else
            {
                int dist = *it - idxCh[i];
                ans = max(ans, dist);
            }
        }

        cout << ans << endl;
    }

    return 0;
}
