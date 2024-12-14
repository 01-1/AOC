// {{{ <<-<<<<=< the optimal template >>=>>>>->>
#include <bits/stdc++.h>  // clang-format off

#include <climits>
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

// using vc = vector<bool>;

const size_t umx = (ll)UINT_MAX * 2;

signed main() {
  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);
  // vc<umx> bs;
  // vc bs(umx);
  bitset<umx> bs;
  int l;
  cin >> l;
  l /= 2;
  f0(i, l) {
    uint a, b;
    cin >> a >> b;
    fo(j, a, a + b) {
      bs[j] = 1;  // prob better way to do this // actually no im not gonna use bitsets
    }
  }
  while (1) {
    int l;
    cin >> l;
    if (l == 0)
      break;
    // vc nbs = bs;
    // bitset<umx> nbs = bs;
    v2 blah(l);
    f0(i, l) {
      int a, b, c;
      cin >> a >> b >> c;
      blah[i].pb(a);
      blah[i].pb(b);
      blah[i].pb(c);

      /*
      fo(j, b, b + c) {
        if (j > umx || a + j - b > umx) {
          cout << "BAD" << endl;
          return -1;
        }
        if (bs[j]) {
          if (nbs[j] == 0) {
            cout << "BAD" << endl;
            return -1;
          }
          nbs[j] = 0;
          nbs[a + j - b] = 1;
        }
      }*/
    }
    bitset<umx> nbs;

    f0(k, umx) {
      if (!bs[k])
        continue;
      for (vi &bla : blah) {
        int a = bla[0];
        int b = bla[1];
        int c = bla[2];
        if (b <= k && k < b + c) {
          nbs[a + k - b] = 1;
          goto END;
        }
      }
      nbs[k] = 1;
    END:
      (void)0;
    }
    bs = std::move(nbs);
  }
  cout << "oh no " << endl;
  f0(i, umx) {
    if (bs[i]) {
      cout << i << endl;
      return i;
    }
  }
}
