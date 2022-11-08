# 100問チャレンジ
### 作成日
- 2022-10-11
- ![SPM is supported](https://img.shields.io/badge/SPM-Supported-orange)
- ![reposize](https://img.shields.io/github/repo-size/tharashi10/terraform)

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
| 03 | 全探索：ビット全探索 | OK |
| 04 | 全探索：順列全探索 | OK |
| 05 | 二分探索 | OK |
| 06 | 深さ優先探索 | OK |
| 07 | 幅優先探索 | OK |
| 08 | 動的計画法：ナップザック DP | OK |
| 09 | 動的計画法：区間 DP | OK |
| 10 | 動的計画法：bit DP | OK |
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
| 07 | Archaeological Sites | https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_c | Listのフィルタ(値の削除)、ベクトルの演算(Zipを使う)<br>と思ったが、in List使った時点で、TLEになる。<br>setに置換して頑張るしかない模様。なんとかAC.. <br>.pyの場合、 Codeは最小限にかかないとACにならない |
| 08 | AtCoder Market | https://atcoder.jp/contests/s8pc-6/tasks/s8pc_6_b | 計算量が$N^3$なので全探索有効<br>ステップ系での`abs()`の使い方|
| 09 | Constellation | https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_d | ある点に着目して考え得る平行移動ベクトルを全探索する<br> 座標を返すLambda式<br> set(tuple)での計算(座標)|
| 10 | Exhaustive Search | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_A | Bit探索の基本<br>シフト演算のユースケースを理解<br> `(x>>n)&1`(xは10進数. 2進数で表した際にn桁目の数が1となる場合True|
| 11 | Switch | https://atcoder.jp/contests/abc128/tasks/abc128_c | 全探索bit<br>全探索bit分かっててもSwitchと電球で頭が混乱する→5日後再度解く(2022-10-21) |
| 12 | Faction | https://atcoder.jp/contests/abc002/tasks/abc002_4 | 全探索bit<br> 2重ループを一気に抜け出す方法(flag利用)<br> nC2をfor..forで記述|
| 13 | Osenbei | https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e | [TODO] |
| 14 | BuildingsColorful | https://atcoder.jp/contests/s8pc-4/tasks/s8pc_4_b| Bit全探索<br>初期値を10**18にすべし |
| 15 | Average Length | https://atcoder.jp/contests/abc145/tasks/abc145_c | 順列全探索<br>問題はEasy |
| 16 |  Count Order |https://atcoder.jp/contests/abc150/tasks/abc150_c | 順列全探索<br>問題はTooEasy<br>エラーハンドリングはしなくてOK|
| 17 | 8 Queens | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_13_A&lang=ja | 順列全探索<br>斜め判定を一時関数的に考える<br>出力でJoin|
| 18 | Binary Search | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja| 二分探索<br>Midで絞り込む|
| 19 | Pizza | https://atcoder.jp/contests/joi2009ho/tasks/joi2009ho_b | 二分探索は`bisect`を使うべし(Listに昇順でAppend可能)<br>円環なので番兵使う(ラストに原点追加)|
| 20 | Snuke Festival | https://atcoder.jp/contests/abc077/tasks/arc084_a | 固定する段が大事<br> 3組を考える場合は真ん中をFix(定石)|
| 21 | 射撃王 | https://atcoder.jp/contests/abc023/tasks/abc023_d| 二分探索<br>最小問題→判定問題と読み解く<br> 探索は両サイドから解を絞ってく|
| 22 | ムーアの法則 |https://atcoder.jp/contests/arc054/tasks/arc054_b | 二分法(二分探索と同じ考え方)<br>2回微分と`f'(x)`の単調性利用|
| 23 | ダーツ | https://atcoder.jp/contests/joi2008ho/tasks/joi2008ho_c | Diffして二分探索<br> |
| 24 | 深さ優先探索 | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B | DFS問題(再帰で)<br>行きがけと帰りがけを利用 |
| 25 | How Many Islands? | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp | 再帰の上限数を引き上げるべし<br> Listの作成時Immutableになることに留意 |
| 26 | Ki | https://atcoder.jp/contests/abc138/tasks/abc138_d | 累積和で計算するべし<br>隣接リストAを双方向で保存する |
| 27 | 薄氷 | https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_d | 異なるパス毎に計算していく<br>引数に位置だけでなく、スコアも入れる |
| 28 | AOJ-BFS | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja | 既に訪問済みリストを作る<br>浅い段階でメモした深さが最短を表す |
| 29 | 迷路BFS | https://atcoder.jp/contests/abc007/tasks/abc007_3 | 自力でいける |
| 30 | Cheese | https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_e | 自力でいける |
| 31 | イルミネーション |https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_e | 6方向をきちんと書く<br>周りを0埋めする<br>同じ処理を書かないこと |
| 32 | Amazing Mazes | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1166&lang=jp | 縦壁と横壁を作る<br>標準入力は癖あり |
| 33 | Grid Repainting  | https://atcoder.jp/contests/abc088/tasks/abc088_d | 自力で行けた|
| 34 | フィボナッチ数列| https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_A&lang=ja | 自力で行けた |
| 35 | Knapsack Problem |https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=ja | DP表を書けるかが全て<br>DPは全部で3種類ある<br>1.ナップザックDP<br>2.区間DP<br>3.bit DP|
| 36 | Knapsack Problem v2| https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_C&lang=ja| 一般ナップザックは同一行を参照する |
| 37 | 最小コインの枚数 | https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=ja |`最小個数部分和問題`というそう<br>自力できた |
| 38 | 最長共通部分列　| https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_10_C&lang=ja| 1次元配列のdpを作ればTLE回避できる |
| 39 | 1年生 | https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_d |DP表かけるか |
| 40 | パスタ |https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d<br>https://atcoder.jp/contests/dp/tasks/dp_c (こちらの問題にすり替え) |オリジナルは重い<br>別の類題でAC済み |
| 41 |暑い日々 | https://atcoder.jp/contests/joi2013yo/tasks/joi2013yo_d| 初期条件の設定を誤らないこと<br>同じ服が続いてもOK |
| 42 | シルクロード| https://atcoder.jp/contests/joi2015yo/tasks/joi2015yo_d| |
| 43 | | | |
| 44 | | | |
| 45 | | | |
| 46 | | | |
| 47 | | | |
| 48 | | | |
| 49 | | | |
| 50 | | | |

### 週ごと

| Week |     Duration    |    Title    | 進捗 |
|------|-----------------|-------------|-----|
| 01   | 2022-10-10(月)~ | 全探索       |  OK |
| 02   | 2022-10-17(月)~ | 全探索       |  OK |
| 03   | 2022-10-24(月)~ | 二分探索・DFS |  OK |
| 04   | 2022-10-31(月)~ | BFS | OK |
| 05   | 2022-11-07(月)~ | 動的計画法 |  |
| 06   | 2022-11-14(月)~ | 動的計画法 |  |
| 07   | 2022-11-21(月)~ | ダイクストラ・ワーシャルフロイド・最小全域木問題 |  |
| 08   | 2022-11-28(月)~ | 逆元を使う問題・累積和 |  |
| 09   | 2022-12-05(月)~ | Union-Find問題 |  |
| 10   | 2022-12-12(月)~ | 実装問題・数学的な問題 |  |


### アルゴリズム基本
#### ナップザックDP
- 製品数×最大容量値 のDP表を書く
- 式
$$
dp_{(i+1),(j)} =  
\left\{
    \begin{array}{ll}
    dp_{(i-1),(j-w)}+value_{(i)} & 容量j-w>=0 \\
    dp_{(i-1),(j)} & Others
    \end{array}
\right.
$$

