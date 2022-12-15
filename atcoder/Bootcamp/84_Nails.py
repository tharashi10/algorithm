"""
三角形の累積和
Imos法
解説読んだけど、圧倒的に謎い
+1/-1をどの頂点にしていて、なんでそこなのかが大変謎い
https://www.ioi-jp.org/joi/2011/2012-ho-prob_and_sol/2012-ho-t4-review.pdf
5 2
2 2 1
2 1 3
--
12
"""


"""
/*
	Problem: Nails (2012-ho-t4)
	Solution by: Kazuhiro Hosaka
*/

#include <cstdio>

using namespace std;

#define MAXN 5020

int N, M;
int is[MAXN][MAXN];

int main() {
	int i;
	int a, b, x;
	
	scanf("%d %d", &N, &M);
	for (i = 0; i < M; ++i) {
		scanf("%d %d %d", &a, &b, &x);
		++is[a][b];
		--is[a][b + 1];
		--is[a + x + 1][b];
		++is[a + x + 1][b + x + 2];
		++is[a + x + 2][b + 1];
		--is[a + x + 2][b + x + 2];
	}
	for (a = 1; a <= N + 10; ++a) for (b = 1; b <= a + 5; ++b) {
		is[a][b] += is[a - 1][b - 1];
	}
	for (a = 1; a <= N + 10; ++a) for (b = 1; b <= a + 5; ++b) {
		is[a][b] += is[a - 1][b];
	}
	for (a = 1; a <= N + 10; ++a) for (b = 1; b <= a + 5; ++b) {
		is[a][b] += is[a][b - 1];
	}
	int ans = 0;
	for (a = 1; a <= N; ++a) for (b = 1; b <= a; ++b) {
		if (is[a][b]) {
			++ans;
		}
	}
	printf("%d\n", ans);
	
	return 0;
}

"""