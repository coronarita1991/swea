#include <bits/stdc++.h>

using namespace std;

int main(int argc, char **argv)
{

    // 하나의 자연수 N의 자릿수 합
    string s;
    cin >> s;
    int sum = 0;

    for (int i = 0; i < s.size(); ++i)
    {
        sum += (s[i] - '0');
        // cout << s[i] << ' ';
    }
    cout << sum;
    return 0; // 정상종료시 반드시 0을 리턴해야합니다.
}