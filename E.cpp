#include <functional>
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <sstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstdio>
#include <bitset>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

int a[5555];
vector <int> ones;
int num, n, m, k;
int dp[2][31][10000];
int par[31][10000];
map <int, int> pos;
vector <int> del, ans;


int main(){
    //    dp[i][k][x] = dp[i - 1][k][x] | dp[i - 1][k - 1][x / a[i]]
    cin >> n >> m >> k;
    for(int i = 1; i <= n; ++i){
        cin >> a[i];
        if(a[i] == 1) ones.push_back(i);
    }
    if(m == 0){
        int p = -1;
        for(int i = 1; i <= n; ++i){
            if(a[i] == 0){
                p = i;
                break;
            }
        }
        int cnt = 1;
        cout << p << " ";
        for(int i = 1; i <= n && cnt != k; ++i){
            if(i == p) continue;
            cout << i << " ";
            cnt++;
        }
        return 0;
    }
    for(int i = 1; i * 1ll * i <= m; ++i){
        if(m % i == 0){
            del.push_back(i);
            if(i * 1ll * i != m) del.push_back(m / i);
        }
    }
    for(int i = 0; i < del.size(); ++i){
        pos[del[i]] = i;
    }
    for(int i = 1; i <= n; ++i){
        dp[0][0][0] = 1;
        if(a[i] == 1 || a[i] == 0){
            continue;
        }
        for(int j = 0; j < del.size(); ++j){
            if(del[j] % a[i] == 0){
                int prev = pos[del[j] / a[i]];
                for(int cnt = 1; cnt <= 30; ++cnt){
                    dp[1][cnt][j] = dp[0][cnt - 1][prev] | dp[0][cnt][j];
                    if(dp[0][cnt - 1][prev]){
                        par[cnt][j] = i;
                    }
                }
            }else{
                for(int cnt = 0; cnt <= 30; ++cnt){
                    dp[1][cnt][j] = dp[0][cnt][j];
                }
            }
        }
        for(int j = 0; j < (int)del.size(); ++j){
            for(int cnt = 0; cnt <= 30; ++cnt){
                dp[0][cnt][j] = dp[1][cnt][j];
                dp[1][cnt][j] = 0;
            }
        }
    }
//    cout << dp[0][1][pos[m]] << endl;
    for(int cnt = 0; cnt <= 30; ++cnt){
        if(dp[0][cnt][pos[m]] && cnt <= k && cnt + (int)ones.size() >= k){
            for(int cur = cnt, x = m; x != 1; cur--){
                int p = par[cur][pos[x]];
                ans.push_back(p);
                x /= a[p];
            }
            for(int i = 0; i < ones.size() && ans.size() != k; ++i){
                ans.push_back(ones[i]);
            }
            for(int i = 0; i < (int)ans.size(); ++i){
                cout << ans[i] << " ";
                if(ans[i] == 0) assert(0);
            }
            cout << endl;
            return 0;
        }
    }
}
