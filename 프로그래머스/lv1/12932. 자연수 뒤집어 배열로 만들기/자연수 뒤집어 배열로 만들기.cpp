#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    
    while(n > 0){
        answer.push_back(n%10);
        n=int(n/10);
    }
    
    return answer;
}