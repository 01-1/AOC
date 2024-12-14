// {{{ <<-<<<<=< the optimal template >>=>>>>->>
#include <bits/stdc++.h>  // clang-format off

#include <queue>
#include <utility>
using namespace std;
#ifdef TAKOTIME
#include "z/d.cc"
#else
#define D(...)
#endif
#define int long long
#define P pair
#define v vector
#define p push
#define e emplace
#define pb push_back
#define eb emplace_back
#define f first
#define s second
#define sz(x) ((int)ssize(x))
#define ben(x) begin(x),end(x)
#define SQ(x) ((x)*(x))
#define frange(i, l, r, k) for(int(i)=(l);(i)<(r);(i)+=(k))
#define fo(i, l, r) frange(i, l, r, 1)
#define f0(i, r) fo(i, 0, r)
#define f1(i, r) fo(i, 1, r)
#define rangerev(i, r, l, k) for(int(i)=(r);(i)>(l);(i)-=(k))
#define ranger(i, r, l) rangerev(i, r, l, 1)
#define fro(i, l, r) ranger(i, (r)-1, (l)-1)
#define fr0(i, r) fro(i, 0, r)
#define TT int TN; cin >> TN; f0(TI, TN)
#define nl << '\n'
#define t template<class T>
#define u using
#define I int
u ll = int64_t; u ull = uint64_t;
u pi = P<I, I>; u vp = v<pi>;
u vi = v<I>;    u v2 = v<vi>;
u v8 = v<uint8_t>; u vl = v<ll>;   
t using uset = unordered_set<T>; template<class K,class U> u umap = unordered_map<K, U>;
u seti  = set<I>;  u mapi  = map<I, I>;
u useti = uset<I>; u umapi = umap<I, I>;
t istream &operator>>(istream &i, v<T> &a) { for (auto &x : a) i >> x; return i; };
t ostream &operator<<(ostream &o, v<T> &a) { for (auto &x : a) o << x << ' '; return o; };
t void Unique(T &a) { a.erase(unique(a.begin(), a.end()), a.end()); }
t bool ckx(T &x, T v) { return v > x && (x = v, 1); }
t bool ckn(T &x, T v) { return v < x && (x = v, 1); }
#define rep(i,a,b) fo(i,a,b)
#define all(x) ben(x)
#undef t
#undef u
#undef I
// clang-format on
// }}} 998244353 1000000007

const array<pi, 4> dir{{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}};

int run() {
  const int n = 141;
  v<string> g(n);
  cin >> g;
  // heat loss, position, consecutive blocks/direction (direction = %4, blocks = /4
  using pipi = pair<pi, pi>;
  priority_queue<pipi, vector<pipi>, greater<pipi>> pq;
  pq.e(make_pair(0, 0), make_pair(0, 0));

  v<char> dbij(n * n * 16);
  while (!pq.empty()) {
    auto &[hd, pos] = pq.top();
    auto [hl, db] = hd;
    auto [i, j] = pos;
    pq.pop();
    if (dbij[db * n * n + i * n + j]) {
      continue;
    }
    dbij[db * n * n + i * n + j] = 1;

    cout << hl << ' ' << db << ' ' << i << ' ' << j nl;
    if (i == n - 1 && j == n - 1) {
      cout << hl nl;
      return hl;
    }

    {
      auto [di, dj] = dir[(db % 4) ^ 1];
      di += i;
      dj += j;
      if (0 <= di && di < n && 0 <= dj && dj < n) {
        pq.e(make_pair(hl + g[di][dj] - '0', (db % 4) ^ 1), make_pair(di, dj));
      }
    }
    {
      auto [di, dj] = dir[(db % 4) ^ 3];
      di += i;
      dj += j;
      if (0 <= di && di < n && 0 <= dj && dj < n)
        pq.e(make_pair(hl + g[di][dj] - '0', (db % 4) ^ 3), make_pair(di, dj));
    }
    if (db / 4 < 2) {
      auto [di, dj] = dir[db % 4];
      di += i;
      dj += j;
      if (0 <= di && di < n && 0 <= dj && dj < n)
        pq.e(make_pair(hl + g[di][dj] - '0', db + 4), make_pair(di, dj));
    }
  }

  return 0;
}

signed main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);
  { printf("Case #%lld: %lld\n", 1LL, run()); }
}
