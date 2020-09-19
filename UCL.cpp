#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <algorithm>


std::map<std::string, int> goals;
std::map<std::string, int> points;

bool sortByVal(std::string& a, std::string& b)
{
    if (points[a] > points[b])
        return 1;
    if (points[b] > points[a])
        return 0;
    if (goals[a] > goals[b])
        return 1;
    return 0;

}


int main()
{   
    int T = 0;
    std::set<std::string> teams;
    std::cin >> T;
    while (T--) {
        goals.clear();
        points.clear();

        for (int i=0; i<12; i++) {
            std::string ht, at, _;
            int g1, g2;
            std::cin >> ht >> g1 >> _ >> g2 >> at;
            if (g1 > g2)
                points[ht] += 3;
            else if (g2 > g1)
                points[at] += 3;
            else
                points[ht] += 1, points[at] += 1;

            goals[ht] = g1 - g2;
            goals[at] = g2 - g1;

            teams.insert(ht), teams.insert(at);
        }
        std::vector<std::string>v(teams.begin(), teams.end());
        teams.clear();
        sort(v.begin(), v.end(), sortByVal);
        std::cout << v[0] << " " << v[1] << std::endl;
    }
    return 0;
}
