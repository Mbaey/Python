#include<cstdio>
#include<stdlib.h>
#include<iostream>
#include<assert.h>
#include<map>
using namespace std;

const int N=1<<20; //10 6
long long a[N]= {0}, n=0, cnt=0;
map<string , pair<double, int>> sch;
int main()
{
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    cin >> n;
    int score;
    string name;

    for(int i=0; i<n; i++){
        cin >> score >> name;
        if(sch.count(name)){
            sch[name].first += score;
            sch[name].second += 1;
        }else{
            sch[name].first = score;
            sch[name].second = 1;
        }
    }

    for (auto it=sch.begin() ; it != sch.end(); it++ )
        cout << (*it).first << " => " << ((*it).second.first)/ ((*it).second.second) << endl;

    return 0;
}
