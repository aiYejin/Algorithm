#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    string answer = "";
    bool capital = true;
    for (char c:s){
        if (isspace(c)){
            capital = true;
            answer += c;
        }
        else if (capital){
            capital = false;
            if (isalpha(c)){
                answer += toupper(c);
            }
            else{
                answer += c;
            }
        }
        else{
            answer += tolower(c);
        }
    }
    return answer;
}