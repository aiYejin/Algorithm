#include<string>
#include <iostream>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    int cnt = 0;
    for (char a:s){
        if (a=='('){
            cnt += 1;
        }
        else{
            cnt -= 1;
        }
        if (cnt < 0){
            answer = false;
            break;
        }
    }
    if (cnt != 0){
        answer = false;
    }
    return answer;
}