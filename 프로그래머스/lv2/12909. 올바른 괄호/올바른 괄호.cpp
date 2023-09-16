#include<string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    bool answer = true;
    vector<char> v;
    for(char c:s){
        if (c=='('){
            v.push_back('(');
        }
        else if(v.empty()){
            answer=false;
            break;
        }
        else{
            v.pop_back();
        }
    }
    if(!v.empty()){
        answer=false;
    }

    return answer;
}