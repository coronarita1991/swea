#include <bits/stdc++.h>
using namespace std;

string isValidDate(string &date)
{
    // 길이/숫자는 8자리 숫자로 검증 불필요
    // 연도 검증 : substr(idx, sub_size)
    int year = stoi(date.substr(0, 4));
    int month = stoi(date.substr(4, 2));
    int day = stoi(date.substr(6, 2));

    // 연도 범위 확인
    if (year < 1)
        return "-1";
    // 월 확인
    if (month < 1 || month > 12)
        return "-1";
    // 월별 최대 일수
    int daysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    // 윤년 고려 x
    if (day < 1 || day > daysInMonth[month - 1])
        return "-1";

    return date.substr(0, 4) + '/' + date.substr(4, 2) + '/' + date.substr(6, 2);
}

int main(int argc, char **argv)
{
    int test_case;
    int T;

    // freopen("input.txt", "r", stdin);
    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case)
    {
        // 입력 받아서 날짜의 유효성 판단
        string s;
        cin >> s;

        string ans = isValidDate(s);

        cout << '#' << test_case << ' ' << ans << '\n';
    }
    return 0; // 정상종료시 반드시 0을 리턴해야합니다.
}