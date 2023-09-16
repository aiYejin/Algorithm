#include <iostream>

using namespace std;

int solution(int n) {
    int a = 0, b = 1, c;
    for (int i = 2; i <= n; i++) {
        c = (a + b) % 1234567;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n = 5; // 예시: n번째 피보나치 수
    int result = solution(n);
    cout << "F(" << n << ") mod 1234567 = " << result << endl;
    return 0;
}
