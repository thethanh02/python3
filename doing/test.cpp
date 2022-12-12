#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    int k;
    cin >> s >> k;
    stack<char> st;
    for (char i : s) {
        while (!st.empty() && k > 0 && i > st.top()) {
            st.pop();
            k--;
        }
        st.push(i);
    }
    while (k--) st.pop();
    vector<char> res;
    while (!st.empty()) {
        res.push_back(st.top()); 
        st.pop();
    }
    for (int i = res.size() - 1; i >= 0; i--)
        cout << res[i];
}