# 100問チャレンジ
### 作成日
- 2022-10-11

### 目的
- AtCoderで自信持ってC/D問題を解けるようにする

### 内容
- Aizu Online Judgeとやや重複があるが、復習にもなるので以下を進めていく
- [Qiita中級から](https://qiita.com/e869120/items/eb50fdaece12be418faa#2-3-%E5%88%86%E9%87%8E%E5%88%A5%E5%88%9D%E4%B8%AD%E7%B4%9A%E8%80%85%E3%81%8C%E8%A7%A3%E3%81%8F%E3%81%B9%E3%81%8D%E9%81%8E%E5%8E%BB%E5%95%8F%E7%B2%BE%E9%81%B8-100-%E5%95%8F)
- 主なコンテンツは以下

| ## | Title | 進捗 |
|----|-------|--|
| 01 | 全探索：全列挙 | OK |
| 02 | 全探索：工夫して通り数を減らす全列挙 |OK|
| 03 | 全探索：ビット全探索 ||
| 04 | 全探索：順列全探索 ||
| 05 | 二分探索 ||
| 06 | 深さ優先探索 ||
| 07 | 幅優先探索 ||
| 08 | 動的計画法：ナップザック DP ||
| 09 | 動的計画法：区間 DP ||
| 10 | 動的計画法：bit DP ||
| 11 | 動的計画法：その他 ||
| 12 | 最短経路問題：ダイクストラ法 ||
| 13 | 最短経路問題：ワーシャルフロイド法 ||
| 14 | 最小全域木問題 ||
| 15 | 高速な素数判定法 ||
| 16 | 高速なべき乗計算 ||
| 17 | 逆元を使う問題 ||
| 18 | 累積和 ||
| 19 | 累積和: いもす法 ||
| 20 | Union-Find ||
| 21 | その他のテクニック ||
| 22 | 実装問題 ||
| 23 | 数学的な問題 ||


### 実際の解くべき問題Set

| ## | Title | URL | Knowledge |
|----|-------|-------|--|
| 01 | 組み合わせ(基本)| https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_7_B&lang=ja | 全探索, Listのfiter |
| 02 |  約数8個だけの整数 | https://atcoder.jp/contests/abc106/tasks/abc106_b | 約数の全探索 |
| 03 | ACGT 文字列 | https://atcoder.jp/contests/abc122/tasks/abc122_b | 連続値のカウント |
| 04 | Karaoke | https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_c | ひたすらFor文(組み合わせ時のfor文のIndex)。<br>これが解ければ全探索に慣れたと思って良いです。とQiitaに書かれおり、特に何もみずに解けたのでこれからは全探索慣れたと言う。 |
| 05 | Half and Half | https://atcoder.jp/contests/abc095/tasks/arc096_a | よく出てきそうな場合分け問題 |
| 06 | **Lucky PIN** | https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_d | 全探索で逆算で考える.<br>`str.zfill()`の使い方<br>find(str)の使い方;Trueならindexを返す.<br>find(str,num)の使い方:第二引数で開始点を指定<br> |
| 07 | 幅優先探索 | | |
| 08 | 動的計画法：ナップザック DP | | |
| 09 | 動的計画法：区間 DP | | |
| 10 | 動的計画法：bit DP | | |
| 11 | 動的計画法：その他 | | |
| 12 | 最短経路問題：ダイクストラ法 | | |
| 13 | 最短経路問題：ワーシャルフロイド法 | | |
| 14 | 最小全域木問題 | | |
| 15 | 高速な素数判定法 | | |
| 16 | 高速なべき乗計算 | | |
| 17 | 逆元を使う問題 | | |
| 18 | 累積和 | | |
| 19 | 累積和: いもす法 | | |
| 20 | Union-Find | | |
| 21 | その他のテクニック | | |
| 22 | 実装問題 | | |
| 23 | 数学的な問題 | | |

---
### Competition
- ABC270
- ABC271