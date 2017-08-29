#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

double fact(double n) {
    return (n == 0) ? 1 : n * fact(n-1);
}

template<typename T>
ostream& operator<<(ostream& str, vector<T> vec) {
    str << "[";
    for (auto const& i : vec)
        str << i << ", ";
    return str << "]";
}

template<typename keyT, typename valueT>
ostream& operator<<(ostream& str, map<keyT, valueT> vec) {
    str << "[";
    for (auto const& i : vec)
        str << "(" << i.first << "," << i.second << "), ";
    return str << "]";
}


double sumDigits(int n) {
    double sum(0);
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

double f(int n, vector<int> facts) {
    double sum(0);
    while (n > 0) {
        sum += facts.at(n % 10);
        n /= 10;
    }
    return sum;
}

double sf(int n, vector<int> facts) {
    return sumDigits(f(n, facts));
}

double sg(map<int, int> g) {
    int sum(0);
    for (auto i : g)
        sum += sumDigits(i.second);
    return sum;
}

int

int main() {
    vector<int> test(10);
    iota(test.begin(), test.end(), 0);
    cout << test << endl;
    int index(50);
    vector<int> facts;
    cout << facts.size() << endl;
    for (int i(0); i < 10 ; ++i)
        facts.push_back(fact(i));
    cout << facts << endl;
    map<int, int> g;
    int res;
    int counter(0);
    map<int, int>::iterator it;
    long i(0);
    int nDigits(2);
    while (counter <= index) {
        for (auto digit: {1,2,3,4,5,6,7,8,9}) {   
            cout << digit;
        }
        ++nDigits;
        counter = index + 1;
    }
    cout << g

    cout << g << endl;
    cout << sg(g) << endl;
    return 0;
}
