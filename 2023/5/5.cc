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

using vc = vector<char>;

// const int umx = 100;  //(ll)UINT_MAX * 2;
int umx = (ll)UINT_MAX * 2;

char ZERO = 0;
char ONE = 1;
// ZERO = '0';
// ONE = '1';

signed main() {
  // umx = 100;
  //

  cin.tie(0)->sync_with_stdio(0);
  cin.exceptions(cin.failbit);
  // vc<umx> bs;
  vc bs(umx);
  int le;
  cin >> le;
  le /= 2;

  f0(i, umx) {
    bs[i] = ZERO;
  }

  f0(i, le) {
    int a, b;
    cin >> a >> b;
    fo(j, a, a + b) {
      bs[j] = ONE;  // prob better way to do this // actually no im not gonna use bitsets
    }
  }
  // cout << bs nl;

  while (1) {
    int l;
    cin >> l;
    if (l == 0)
      break;
    vc nbs = bs;
    v2 blah(l);
    f0(i, l) {
      int a, b, c;
      cin >> a >> b >> c;
      blah[i].pb(a);
      blah[i].pb(b);
      blah[i].pb(c);

      // cout << a << ' ' << b << ' ' << c nl;
      /*
      fo(j, b, b + c) {
        if (j >= umx || a + j - b >= umx || a + j - b < 0) {
          cout << "BAD" << endl;
          return -1;
        }
        // if (bs[j] == ONE) {
        if (bs[j]) {
          nbs[j] = ZERO;
          // nbs[a + j - b] = ONE;
        }
      }
      fo(j, b, b + c) {
        /*if (j > umx || a + j - b > umx) {
          cout << "BAD" << endl;
          return -1;
        }*/
      // if (bs[j] == ONE) {
      /*
      if (bs[j]) {
        // nbs[j] = ZERO;
        nbs[a + j - b] = ONE;
      }
      */
    }
    f0(i, umx) {
      for (auto &x :)
    }
  }
  bs = std::move(nbs);
  /*f0(i, umx) {
    if (bs[i] == ONE) {
      cout << i << ' ';
    }
  }
  cout nl;
  */
  // cout << bs nl;
}
cout << "oh no " << endl;
f0(i, umx) {
  if (bs[i] == ONE) {
    cout << i << endl;
    return (signed)i;
  }
}
}
