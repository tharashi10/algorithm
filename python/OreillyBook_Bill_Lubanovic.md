# Oreilly Contents
- https://learning.oreilly.com/library/view/introducing-python-2nd/9781492051374/

|##|  Title                     |進捗  |
|--|----------------------------|-----|
|01| A taste of py              | OK  |
|02| Data Type, Values,Variables| OK  |
|03| Numbers                    | OK  |
|04| Choose with IF             | OK  |
|05| Text Strings               | OK  |
|06| Loop with while and For    | OK  |
|07| Tuple and List             | OK  |
|08| Dictionary and Set         | OK  |
|09| Functions                  | OK  |
|10| Objects and Classes        | OK  |
|11| Modules and Package        | OK  |
|12| Wrangle and Mangle data    | OK  |
|13| Calendar and Clocks        | OK  |
|14| File and Directory         | OK  |
|15| Data in Time: concurrency  | OK  |
|16| Data in a Box              | OK  |
|17| Data in Space              | OK  |
|18| The Web                    | OK  |
|19| Be a Pythonista            | OK  |
|20| Py Art                     | Opt |
|21| Py at Work                 | Opt |
|22| Py Sci                     | Opt |
                  

<br/><br/>

# 第1部/Pythonの基本
## 1章:概要
- Pythonは`1991年`に登場したため、C < Python < Java での順で若いそう
- Guido van Rossum が PythonのCreator（オランダ人）
- Pythonは `Dynamic Language`(also called Scripting Language)
  - そのため変数宣言をしなくてもOK
- Python が流行る理由は、Readableであることと同時に、Writableだから
- Familiar quote is that "fits you brain".
- Python の`terseness`(簡潔さ)も流行る理由の一つ
- Python2は、Python2.7まであり、これらは2020年の1月までのサポートになる
- Python3では、printがメソッドになって登場した
- プログラマーの心構えが `import this`　すると出てくる(Zen=[禅])

<br/>

## 2章:データ型
- Pythonのデータは `Object` である
- データ型に対して、内部的に異なるbitを使う
  - そのため、`int 7`は、`int`と`7`に包み込まれた箱のようなイメージになる
- Data型

| Type | Mutable? | Example  |
| ---- | -------- | -------- |
| bool  |   no     | True/False |
| int   |   no     | 47         |
| float |   no     | 3.14  |
| complex  |   no     | True/False |
| str   |   no       | "hoge", ''' |
| list |   `yes`     | [1,2,3]  |
| tuple  |   no     | (1,2,3) |
| bytes  |   no     | b'ab\xff'         |
| bytearray |   `yes`     | bytearray(..)  |
| set   |   `yes`     | set([1,2,3]) |
| flozen set   |   no     | flozenset(['Hoge']) |
| dict  |   `yes`     | {'key':'value'}  |

<br/>

- variable names は、`case-sensitive`
- 予約語
```py
>>> help("keywords")

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not
``` 
- Pythonでは変数は、単なる参照(`reference`)に過ぎない
  - C/C++のように変数に型定義を書くのは、変数に型およびメモリの場所をバインドしているため
  - Pythonのダウンサイドは速度。これは上記の操作をComputerにお任せしているため。
- 表にあるように、Integerは`Immutable`、Listは`Mutable` (詳しくは8章)

<br/>

## 3章:数値型
- `/`は、浮動小数点を返却する
- `//`は、整数型を返却する
- base-18 arithmetic. (Cat)
- `int(10,2)`でバイナリに変換できる

<br/>

## 4章:If文
- Comment with `#`
- セイウチ演算子(`:=`)
  - if文で代入演算子として利用可能
  - 簡単に言うと代入を式に埋め込むことが可能
```py
if (length := len(s)) > 3:
  print(length)
else:
  print('too short')
```
<br />

## 5章:Text文字
- String = シーケンス
- String型は`'str'`, `"str"`のどちらで囲んでもOK
- 改行ありのString型は, `''' sentence '''` Triple Quotesにする
- 特殊文字のエスケープは`\'`あるいは`\"`
- Backslashのエスケープは2回打つ->`\\`
- Stringはイミュータブルなので、Indexで指定して置換できない(str.replace使う)
- formatは`f{}`の方式が推奨されている. `%d`などの方式は古い(python2.7まで)

<br/>


## 6章:Loop文
- itertools はショートカットを多く含んだ標準ライブラリ
- Iteratorについて、Pythonicな方法は以下
```python
for letter in word:
  print(letter)
```
<br/>


## 7章:TupleとList
- TupleはImmutable。ListはMutable。
- Tupleは末尾にコンマをつける
```py
word = ('Apple')   # String になる
word = ('Apple',)  # Tuple になる
```
- Immutableな様子
```py
values = ("Apple","Orange","Melon")
print(id(values))    ## 4394467712
values+= ("Lemon",)
print(id(values))    ## 4404376448
```
- LIFO
  - append()と`pop()` (デフォルトでpop(-1))
- FIFO
  - append()と`pop(0)`
- `sort()`と`sorted()`
```py
values = ['G','A','C']
values.sort()                  # List自身をソートする
values_sorted = sorted(values) # ソートして、Copyする
```
- Shallow Copy(`list.copy()`) と Deep Copy(`list.deepcopy()`)
```python
import copy
A = [a,b,c]
B = copy.deepcopy(A) # 2次元配列の場合でも、値の更新が可能
```
- `zip(A,B)`は内積をとるイメージ(Pairを作る)
- List ComplehensionはよりPythonicな手法かつ高速
```py
a_list = [number for number in range(6) if number%2==0]
a_list  ## [0, 2, 4]
```

- tupleは`append()`などのビルトイン関数がないのになぜ有用なのか
  - メモリスペースを節約できる
  - TupleをDictionary型Keyのように使える

<br/>

## 8章: Dict型とSet型
- コロンを使わない場合のDict型の書き方
```py
customer = dict(first="Wile", middle="E", last="Coyote")
```
- DictKeyは常にUniqueであることは要注意
- Dictの結合
```py
s_dict = {'a':"A", 'b':"B"}
t_dict = {'b':"B", 'c':"C"}
{**s_dict,**t_dict} ## {'a': 'A', 'b': 'B', 'c': 'C'}
```
- set型の作り方=`set()` (`{}`とした場合、空ならDict型と判断される)
```py
s = {1,2,3,4,5}
type(s)
```
- frozenSet()を使うとImmutableなSet()が作れる
```py
s = frozenset({1,2,3,4,5})
s ## frozenset({1, 2, 3, 4, 5})
```

<br/>

## 9章: Functions
- `None`と`False`を見分ける方法は`if val is None`を使うこと
- default Parameterは関数を定義した時に計算される
```python
def menu(wine, entree, dessert='pudding'):
  return {'wine':wine, 'entree':entree, 'dessert':dessert}
```
- よくPythonに関する面接で聞かれるものとして以下がある。
```py
def buggy(args,result=[]):
    result.append(args)
    return result
buggy('a') ## ['a']
buggy('b') ## ['a','b'] 2回目に呼ばれるときにListが初期化されていない

def works(args,result=None):
    result=[]
    result.append(args)
    return result
buggy('a') ## ['a']
buggy('b') ## ['a'] OK
```
- `def func(*args)`は`args`にtupleの複数値が格納される([One-Asterisk])
- `def func(**kwargs)`は`kwargs`にDict型のKeywordが格納される([Two-Asterisk])
- docstringは以下
```py
def func(some):
  'echo input argument'
  return some

>>help(func) ## helpでDocstringが見える
```
- `dunder`=`Duble Underscore`で、接頭辞が`__`のもの
- FunctionsはImmutableなオブジェクトである
- Lambdaは、無名関数であり、GUIのCallback関数として利用されることが多い
- GeneratorはIteratorの一種である
```py
def my_generator():
    yield 1
    yield 2
    yield 3
my_generator        ## <function __main__.my_generator()>
list(my_generator()) ## [1,2,3]
```
- generator はメモリに展開されず、使い切りのものになる
- generator　内包記は以下
```py
genobj = (pair for pair in zip(['1','2'],['a','b']))
list(genobj)
```
- Global変数にアクセスする方法は以下.
```py
animal = 'cat'
def print_global():
    global animal     ## 明示的に指定する
    animal = 'catcat'
    print(animal)
print_global()
```
- dunkerの名前空間は、`globals()`で見ることができる
<br/>
<br/>

## 10章: クラス
- Objectとは、「`Data`と`Code` を持つカスタムなデータ構造のこと」
- 例えば`int 7`は、アサインしたタイミングで既に加算や減算のメソッドを持つObjectと言える
  - これは、Pythonで暗黙的に整数Integerクラスがビルトインされているためである
- `def __init__(self)`はどのクラスも必ず持つべきというものではない
  - また正確には、Javaでいうところのコンストラクタではない
  - イニシャライザというべきものになる
- 親クラスのMethodを子クラスから呼びたいときは、`super()`を使う
  - `super()`には親クラスのクラス定義が格納される
  - privateなメンバ変数にしたい場合は、`self.__name = name`のようにUnderScoreを付与する
```py
class Person():
    def __init__(self,name):
        self.name = name

class EmailPerson(Person):
    def __init__(self,name,email):
        super().__init__(name)
        self.email = email

p = EmailPerson("Foo","sample@gmail.com")
p.name
```
- `mro`というクラスがデフォで備わっている。これによりクラス多重継承の場合にメソッドの解決順序がわかる
- ミックスイン(`mixin`)=クラス拡張で、単体では動作しさせないクラス(Logging)
- `@property`デコレータを付けることで`getter`を実装できる
  - `property`で定義した属性値は外側から更新できない(メリット)
- Methodの種類は3つある
  - インスタンスメソッド(selfを伴うもの)
  - クラスメソッド(clsを呼び出すもの。@classmethodデコレータ)
  - 静的メソッド(ただprintを呼ぶだけのようなもの。オブジェクト生成せずに呼び出せる)
- ポリモーフィズム(多態性):異なるクラス間の類似したメソッドの名前を統一する
- magic method は、`__eq__`や`__str__`のようなメソッド(`==`で比較できるようにする)
- `named tuple`は`tuple`のサブクラスである
  - 引数の`Member`はクラス名になる
  - dictのKeyのようにアクセス可能になる
  - Immutableのように扱える
```py
from collections import namedtuple
Member = namedtuple('Member',['id','name'])
```


<br/>
<br/>


# 第2部/実用向け
## 11章: Moduleとパッケージ
- moduleは同じ階層でのPythonファイルのこと
- Packageはサブディレクトリのこと
- PackageはサブディレクトリでネストされていてもModuleをimportの記述で読み込める
```py
from subdirectory import module
```
- Python3.3以下では、Packageには`__init__.py`（空のファイル）を置くべし
- Moduleは上から優先的に利用される
```py
import sys
sys.path
['/Users/tharashi/2022/JupyterHome',
 '/opt/homebrew/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python310.zip',
 '/opt/homebrew/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10',
 '/opt/homebrew/Cellar/python@3.10/3.10.8/Frameworks/Python.framework/Versions/3.10/lib/python3.10/lib-dynload',
 '',
 '/opt/homebrew/lib/python3.10/site-packages']
```
- setdefault()関数は以下
```py
di = {1:'a',2:'b'}
di.setdefault(1,'c') # Keyがある場合は置き換えない
di.setdefault(3,'c') # Keyがない場合は新規追加
di
```
- 標準ライブラリ(`Counter`)の使い方
```py
from collections import Counter
l = ["spam","spam","spam","goodie"]
counter = Counter(l)
counter.most_common()
```
- `stack + queue = deque (double-ended queue)`=両端キュー(先頭及び末尾から要素消せる)
- palindrome(回文)のサンプルで`deque`のお試し
```py
from collections import deque
def palindrome(word):
    queue = deque(word)
    while len(queue)>0:
        if queue.popleft()!=queue.pop():
            return False
        return True
palindrome("madam")
```
- **itertools `accumulate`は知っていたが、累積`積`も行けるのは知らなかった
```py
import itertools
def multiple(a,b):
  return a*b
ll = [1,2,3,4]
acc = itertools.accumulate(ll,multiple)
print(list(acc)) # [1,2,6,24]
```

<br/>

## 12章: Unicode
- 雑にいうと、データフォーマットは`text`か`binary`の2種類に分けられる
- ASCII = American Standard Code International Interchange
- ASCIIは、7bitsで128個の一意な値
- ただし、ASCIIはヨーロッパの言語に対応できない(ドイツ語など)
- そこでUnicodeが登場する(言語やPlatformに依存しない)
```py
import unicodedata
v = '\u2603'
name = unicodedata.name(v)
value = unicodedata.lookup(name)
print(v,name,value) ## ☃ SNOWMAN ☃
```
- `len()`メソッドはUnicode文字の長さを返す（Byteではない）
- UTF-8は、Unicodeをバイト列に変換する方式のひとつ
- encodeは以下。
```py
snowman = "\u2603"
e = snowman.encode('utf-8')
e    #b'\xe2\x98\x83'
```
- decodeは以下。
```py
place = "caf\u00e9"
place_bytes = place.encode('utf-8')
place_bytes.decode('utf-8') ## 'café'
```
- Unicodeを使うのがデファクト
- decimal(10進法) ex.233
- hex(16進法) ex.0xe9
- 正規表現の例は以下。
```py
import re
result = re.match('young','young boy') # matchは先頭から始まるものをマッチ
if result:
    print(result.group()) ## young

---
import re
result = re.search('ng','young boy')　# searchは、Anywhereマッチ
if result:
    print(result.group()) #ng

---
import re
result = re.findall('y','young boy') # findallは、複数マッチ
if result:
    print(result) ## 2

---
import re
result = re.sub('y','%','young boy') # subは、置換
if result:
    print(result)
```

- Bytesについて
  - `bytes`は、イミュータブル
  - `bytearray`は、ミュータブル(like a list)
```py
b_list = [1,2,3,4,5]
the_bytes = bytes(b_list)
the_bytearray = bytearray(b_list)
the_bytes, the_bytearray   
## (b'\x01\x02\x03\x04\x05', bytearray(b'\x01\x02\x03\x04\x05'))
```
- Bit演算子
```py
x = 5  #  0b101  101
y = 1  #    0b1  001

print(x & y) # 1   And     001
print(x | y) # 5   Or      101
print(x ^ y) # 4   排他Or   100
print(~x)    # -6  Flip    010
print(x<<1)  # 10  Left   1010
print(x>>1)  # 2   Right    10
```
<br/>

## 13章: カレンダー
- datetimeモジュールは、dateもtimeも含んでいる
- 扱えるObjectは以下の4つ
  - date (年・月・日)
  - time (時・分・秒)
  - datetime (dateとtime両方とも)
  - timedelta (date/timeのインターバル)

```py
from datetime import timedelta, date
one_day = timedelta(days=1)
date.today() + one_day


from datetime import datetime
dt = datetime(2023,1,1,13,24,0,0)
dt.isoformat()   ## '2023-01-01T13:24:00'
```
- ISO8601は、timezoneに対応している
- timeモジュールのtime()はEpoch時間を返却する(datetimeモジュールのtimeとは別物)
```py
import time
time.time() ## 1672893039.657204
```
- 時間の扱い方としては、UTCを用いるのはデファクト
- サーバについても同様で、基本的にはローカルタイムではなく、UTCを用いる
- `struct_time`はNamedTupleである
```py
import time
now = time.time()
time.localtime(now) # struct_time　オブジェクトを返す
# time.struct_time(
#  tm_year=2023, 
#  tm_mon=1, 
#  tm_mday=5,
#  tm_hour=14,
#  tm_min=54, 
#  tm_sec=9, 
#  tm_wday=3, 
#  tm_yday=5, 
#  tm_isdst=0
# )
```
- dateのフォーマットについて
```py
from datetime import date
d = date(2022,2,2)
fmt = "It's %A, %B %d, %Y, local time => %I:%M:%S:%p"
d.strftime(fmt)
```

<br/>

## 14章: ファイルとディレクトリ
- 構文:`fileobj = open(filename, mode)`
- modeはファイル操作のこと
  - firstletter
    - `r`=read
    - `w`=write
    - `x`=既存ファイルがない場合のみwrite(file守れる)
    - `a`=append
  - secondletter
    - `t`=text
    - `b`=binary
```py
fout = open('ops.txt','wt')
print('Hello',file=fout)
fout.close()
```
- readline()の基本は以下。
```py
fn = open('ops.txt','rt')
tx = ''
while True:
    line = fn.readline()
    if not line:
        break
    tx+=line
print(tx)
```
- Fileの自動クローズは、`with open('some.txt','wt') as alias:`
```py
with open('ops.txt','wt') as fout:
    fout.write("hello")
``` 
- ファイルオペレーションはosモジュールを使う
```py
import os
os.path.exists('ops.txt') # True
```
- File/Dir名のMatch
```py
import glob
glob.glob('*.ipynb')
```
- `BytesIO`/ `StringIO`は、ファイルライクなObjectとして使える
- Usecaseとしては、データフォーマット変換
```py
from io import BytesIO
from PIL import Image
def data_to_img(data):
    fp = BytesIO(data)
    return Image.open(fp)  # read from memory
```

<br/>

## 15章: プロセスと同期処理
- multiprocessingモジュールの利用例は以下。
- built-inで動かすとNG(multiprocessing自体が制限多いため)
```python
import os
import multiprocessing

def whoami(some):
    print('Process %s: %s' % (os.getpid(),some))

if __name__=="__main__":
    whoami("I am the main program")
    for n in range(4):
        proc = multiprocessing.Process(target=whoami,args=("I am the function : %s" %n,))
        proc.start()
# Process 67687: I am the main program
# Process 67689: I am the function : 0
# Process 67690: I am the function : 1
# Process 67691: I am the function : 2
# Process 67692: I am the function : 3
```
- PythonからBusy度合いを見ることも可能
```py
import psutil
psutil.cpu_percent(True) # 9.7
```
- `invoke`モジュールを使うと、コマンドラインにて自作関数を実行可能
- time_strの誤植発見
```py
'''
File名は tasks.py とする
'''
from invoke import task
@task
def mytime(ctx):
    import time
    now = time.time()
    time_str = time.asctime(time.localtime(now))
    print("Local Time is ", time_str) 

# $ invoke mytime
# Local Time is  Thu Jan  2 22:22:48 2023
```
- 何かを待たされている場合は、基本的には以下の二つが考えられる
  - I/Oバウンド: CPUはめちゃくちゃ高速。メモリの~100倍、Diskの~1000倍
  - CPUバウンド: CPU張り付き状態
- 並列処理(Concurrency)には以下の二つの用語がある
  - Synchronous : 親に続いて歩いていくガチョウ
  - Asynchronous: 池を別々に散らばって泳ぐガチョウ
- 例として、皿洗いのイメージ(洗う/乾かす/しまう)
- Synchronousは、One Worker, One thing at a timeの思想
- Drier + Washer + Put-it-awayer
- `threading`モジュールはmultiprocessingの従兄弟
```py
import threading
def do_this(what):
    whoami(what)

def whoami(some):
    print('Thread %s: %s' % (threading.current_thread(),some))

if __name__=="__main__":
    whoami("I am the main program")
    for n in range(4):
        p = threading.Thread(target=do_this,args=("I am the function : %s" %n,))
        p.start()

# Thread <_MainThread(MainThread, started 4369286528)>: I am the main program
# Thread <Thread(Thread-1 (do_this), started 6118322176)>: I am the function : 0
# Thread <Thread(Thread-2 (do_this), started 6118322176)>: I am the function : 1
# Thread <Thread(Thread-3 (do_this), started 6135148544)>: I am the function : 2
# Thread <Thread(Thread-4 (do_this), started 6151974912)>: I am the function : 3
```
- Global変数がなければThreadingは特に問題ないが、ある場合はスレッドセーフを意識する必要がある
- 基本的な考え方は以下
  - IOバウンズは、`threading`を使う
  - CPUバウンズは、`multiprocessing`を使う
- concurrentモジュールを使ってマルチスレッドを確認する
```py
from concurrent import futures
import math
import sys

def calc(val):
    result = math.sqrt(float(val))
    return val, result

def use_threads(num,values):
    with futures.ThreadPoolExecutor(num) as tex:
        tasks = [tex.submit(calc, value) for value in values]
        for f in futures.as_completed(tasks):
            yield f.result()

def use_processes(num,values):
    with futures.ProcessPoolExecutor(num) as pex:
        tasks = [pex.submit(calc, value) for value in values]
        for f in futures.as_completed(tasks):
            yield f.result()

def main(workers,values):
    print(f"Using {workers} workers for {len(values)} values")
    
    print("Using Threads:")
    for val, result in use_threads(workers,values):
        print(f"{val} {result:.4f}")
    
    print("Using Processes:")
    for val, result in use_processes(workers,values):
        print(f"{val} {result:.4f}")

if __name__=="__main__":
    workers = 3    # default
    if len(sys.argv) > 1:
        workers = int(sys.argv[1])
        values = list(range(1,6)) # 1...5
        main(workers, values)

# $ p cf.py 5
# Using 5 workers for 5 values
# Using Threads:
# 2 1.4142
# 1 1.0000
# 3 1.7321
# 4 2.0000
# 5 2.2361
# Using Processes:
# 1 1.0000
# 2 1.4142
# 3 1.7321
# 4 2.0000
# 5 2.2361
```
<br/>

## 16章: ストレージ
- トレードオフな関係にあるRAMとDiskのどちらにデータを保存すべきか
- Flatfile/Structured File/Databaseについて記述していく
- CSV Parse
```py
import csv
villans = []
with open('test.csv','rt') as fin:
    cin = csv.reader(fin)
    villans = [row for row in cin]

print(villans)
```
- JSONのモジュールは一個だけ。
- `dumps()`を使うとJSON StringにEncodeできる
- `loads()`を使うとPythonのデータ構造に戻せる
```py
import json
with open('test.json','rt') as fin: 
    test_json = json.load(fin)    # File読み込みの場合
print(test_json)

---
import json
test = {
    "Hoge":"hoge",
    "Foo":"foo",
    "Bar":"bar"
    }
test_json = json.dumps(test)     # json dataをOnthe Flyで読み込む場合
print(test_json)                 # <class 'str'>の型になる 

---
po = json.loads(test_json)       # JSON StrをPythonObjに変換できる
print(type(po))                  # <class 'dict'>
```
- datetimeの扱い
- JSONモジュールでは日付型を定義していないため、str 変換しないとErrorになる
```py
import json
import datetime

now = datetime.datetime.utcnow()
print(json.dumps(now,default=str))  # str()を適用している
# "2023-01-06 03:27:46.642119"
```
- `configparser`モジュール
```py
# settings.cfg
# [English]
# greeting=hello
# 
# [French]
# greeting=bonjour
import configparser
cfg = configparser.ConfigParser()
print(cfg['English'])
```
- ExcelなどのSpreadSheetはバイナリ形式である
- フルスキャンはDBの値をbrute-force(全探索)すると言う意味
- DB-API
  - `connect`
  - `cursor`
  - `execute`
  - `fetchall`
- sqlite3使ってみる
```py
import sqlite3     # これだけでsqliteが使えてしまう
dbname = 'main.db'
conn = sqlite3.connect(dbname)
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo
(critter varchar(20) primary key,
count int,
damages float)
''')

curs.execute('insert into zoo values ("duck",5, 0.0)')

# Place Holder使う方が良い
ins = 'insert into zoo(critter,count,damages) values (?,?,?)' 
curs.execute(ins,("wisel",2,3.0))

curs.execute('select * from zoo')
result = curs.fetchall()
result

curs.close()
conn.close()
```
- SqlAlchemyのORM:https://docs.sqlalchemy.org/en/14/orm/tutorial.html
- SqlAlchemyは以下の3つのレベルで使い分けることができる
  - The lowest level=DB connection pooling, execute sql...
  - The next level=Python-likeなSQL表現
  - The highest level=ORM(SQL Expression Language and bind applications
- NOSQLの最もシンプルな例は、Key-Valueストア
- `dbm`フォーマットがNoSQLとして使える
```py
import dbm
db = dbm.open('definition','c')
db['mustard']='yellow'
db['apple']='red'

print(db.keys)  ## [b'apple', b'mustard'] 
``` 
- Document Database = 項目が変わりうるNoSQLデータベース
- ODM(Object Document Mapper)
  - Mongo-> PythonAPI=`tools`
- TimeSeriesDatabase 
  - InfluxDB-> PythonAPI=`influx-client`
- GraphDB
  - Neo4J-> PythonAPI=`py2neo`
- Full-Text DB
  - Solr-> Python API=`SolPython`

<br/>

## 17章: ネットワーク
- TCP/IP
  - Session/Presentation/Application Layer
  - Transport Layer(UDP/TCP)★
  - Network Layer 
  - Data Link Layer
  - Physical Layer
- UDP=User Datagram Protocol(tiny massages)
- TCP=Transmission Connection Protocol(long-lived connections)
- Socketは、最も最下層のレイヤーで使用される
- UDPは、ライトなメッセージを送る用であり、順序は気にしない
- UDPは、Packet自体がロストしてもOK
- TCPは、Stringメッセージではなく、Byteストリームを送信する
- Networkingパターン
  - request-replyパターン
    - 最も一般的なもの
    - REQ-REPと言う
    - 同期なMessageのやりとりになる
  - pushパターン 
    - LBが前段にあるバックエンドのweb serverがこれ(Activeなサーバが受け止める)
  - pub-subパターン
    - subscriberはtopic(興味のあるもの)を定義して、pubはtopicに該当するものだけ送る
- ZeroMQは、Socket関連のライブラリ
- 多数のREQ/REPを扱う場合は、Brokerとして、DEALER/ROUTERを使う
- Publish-Subscribeパターンは、以下のイメージ
  - ラジオ放送で放映しているようなもの。聞き手は不特定多数のため意識しない
```py
import redis
import random

conn = redis.Redis()
cats = ['siamese', 'persian', 'maine coon', 'norwegian forest']
hats = ['stovepipe', 'bowler', 'tam-o-shanter', 'fedora']
for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print('Publish: %s wears a %s' % (cat, hat))
    conn.publish(cat, hat)

import redis
conn = redis.Redis()

topics = ['maine coon', 'persian']
sub = conn.pubsub()
sub.subscribe(topics)
for msg in sub.listen():
    if msg['type'] == 'message':
        cat = msg['channel']
        hat = msg['data']
        print('Subscribe: %s wears a %s' % (cat, hat))
```
- APIs一覧
  - https://developer.nytimes.com/
  - https://python-twitter.readthedocs.io/
  - https://developers.facebook.com/tools
  - http://www.wunderground.com/weather/api
  - http://developer.marvel.com/
- Serialization/Marshalling = メモリ上のデータとBytesシーケンス間の変換のこと
- Sportifyは、Hadoop Streamingを利用している
  - https://github.com/spotify/luigi
-  Sparkは、Hadoopよりも数100倍速い
<br/>

## 18章: Web
- HTTPの重要な特徴は`stateless`であること
- Curlは最もポピュラーなClient Web-Brower（telnetより使いやすい）
- HTTPS Status Code
  - `1xx`=info
  - `2xx`=success
  - `3xx`=redirection
  - `4xx`=client error
  - `5xx`=server error
- `urllib.request`は標準モジュールであるのに対して、`requests`はThird-Party Tool
- `requests`の方を使うのを推奨
- Web Server
```bash
python -m http.server
```
- WSGI= Web Server Gateway Interface(Wizgyと読む説)
  - ASGI=Asynchronous
  - Apache=PythonCodeをApache Processの中で実行可能
  - CentOSでyumで入れたけど Invalid command 'WSGIScriptAlias'に遭遇
  - おそらくApache2で試さないとNGな感じ
```py
# home.wsgi
import bottle
app = bottle.default_app()
@bottle.route
def home():
    return "apache and wsgi, sitting in a tree"

# /etc/httpd/conf/httpd.conf:
# <VirtualHost *:80>
#     DocumentRoot /var/www
# 
#     WSGIScriptAlias / /var/www/test/home.wsgi
# 
#     <Directory /var/www/test>
#     Order allow,deny
#     Allow from all
#     </Directory>
# </VirtualHost>
```
- `bottle`はWebFrameworkの一つ
```py
from bottle import route, run

@route('/')
def home():
  return "It isn't fancy, but it's my home page"
  # return static_file('index.html','.')

run(host='localhost', port=9999)
```
- `Flask`は、bottleよりも幅広く使うことができる
- 筆者もflaskは最も好きなPython WebFrameだと書いてある
- Flaskとbottleの差異としては、`jinja2`(templete system)が含まれているかどうか
- 
```py
from flask import Flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s" % thing
    # return render_template('flask2.html', thing=thing) # jinja2使う場合

app.run(port=9999, debug=True)

# clientサイド
curl -v localhost:9999
curl -v localhost:9999/echo/hi
```
- `Django`も人気のあるWeb Frameworkである
- Djangoは以下の特徴がある
  - ORM Codeが使える(CRUD操作)
  - 自動のAdminPageが含まれている
- `import antigravity` = Webbrowserの標準ライブラリ
- `scrapy`は`BeautifulSoup`のようなモジュールではなく、Frameworkである
```py
def get_links(url):
    import requests
    from bs4 import BeautifulSoup as soup
    result = requests.get(url)
    page = result.text
    doc = soup(page)
    links = [element.get('href') for element in doc.find_all('a')]
    return links

if __name__ == '__main__':
    import sys
    for url in sys.argv[1:]:
        print('Links in', url)
        for num, link in enumerate(get_links(url), start=1):
            print(num, link)
        print()


$ python links1.py http://boingboing.net
Links in http://boingboing.net
/home/opc/links1.py:6: GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 6 of the file /home/opc/links1.py. To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.

  doc = soup(page)
1 https://boingboing.net
2 https://boingboing.net/search
3 https://store.boingboing.net
4 https://boingboing.net/search
5 https://store.boingboing.net
6 https://boingboing.net/blog
7 https://bbs.boingboing.net
8 https://bbs.boingboing.net/faq
9 https://store.boingboing.net
10 https://bit.ly/boingboingdealssupport
11 https://boingboing.net/signup
12 https://boingboing.net/about
13 https://boingboing.net/contact
14 https://ads.boingboing.net
```

- Let’s Watch a Movie アプリ
```py
"""Find a video at the Internet Archive
2 by a partial title match and display it."""
```
<br/>



## 19章: パイソニスタになるために
- 参照すべきもの
  - PyPI(https://pypi.org/project/pinax-cms/)
  - GitHub(https://github.com/trending?l=python)
  - Recipe(bit.ly/popular-recipes)
- 複数のPython Packageをインストールする場合は、`requirements.txt`を利用するべし
- Jupyter は、IPythonの進化形である
- JupyterLabは、Jupyterの進化形である
- PEP8に従うと、定数は大文字かつアンダースコアで表現する
  - `F_BOIL_TEMP` = 212.0
- CodeChecker = `pylint`, `pyflakes`,`flake8`
- Unittest
```py
def just_do_it(text):
    return text.capitalize()

import unittest
import cap

class TestCap(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'duck'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'Duck')

    def test_multiple_words(self):
        text = 'a veritable flock of ducks'
        result = cap.just_do_it(text)
        self.assertEqual(result, 'A Veritable Flock Of Ducks')


if __name__ == '__main__':
    unittest.main()
```

- Debugは、`print`使うか、`@dump`使うか、`dpb(python debugger)`を使う
- PseudoCode = like explanation
  - `python -m db code1.py city.csv`
  - `b`でbreakpointとなる
- import logging
  - debug()
  - info()
  - warn()
  - error()
  - critical()
- logレベルは`basicConfig()`で変えることができる
- デフォルトはwarning
```py
import logging
fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt, filename='sample.log')
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")
```
- fmt:asctime=[ISO 8601 string]
- 時間の計測は、`time`モジュールを使うか、`timeit`モジュール(引数にCodeを埋め込める)を使うか、
- あるいは`snooze()`メソッドを使うか、`TimeContextManager`クラスを使う
- データ構造とアルゴリズムについて  
  - list.append()よりもlist comprehensionの方が高速
  - PyPyは新しいインタプリタで、CPython(Cythonとは別物)よりも高速
  - Numbaは、`@jit`デコレータで使用可能になる。数値計算処理で有用
  - https://github.com/madscheme/introducing-python
- Book
  - Effective Python
  - Fluent Python
- Things to DO
  - Pythonists don't have homework today.
  - この後の3章は、`芸術`/`ビジネス`/`サイエンス`


<br/>

## 20章: 芸術
- Optional

## 以上