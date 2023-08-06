# CSVと階層フォルダの相互変換

## このモジュールについて

このプロジェクトは、CSVファイルと階層フォルダを相互変換するpythonモジュール。具体的には、ルールに沿って作成されたディレクトリからcsvファイルへの書き起こし、そして、ある一定のルールベースに沿って作成されたcsvからディレクトリを作成する。

### csvからディレクトリへ変換

csvファイルから階層をパースして、ディレクトリとプロパティファイルを作成する
* csv
  
  ```csv
  index, no, pos, param1, param2, param3,
  1, 1.1, 1, p1_1, p1_2, p1_3
  2, 2.2, 2, p2_1, p2_2, p2_3
  ```

* csvをディレクトリに変換  

  ```
  .
  |-- 1
  |   |--1.1
  |       |-- attribute.json(機械学習用パラメータ)
  |-- 2
  |   |--2.1
  |       |-- attribute.json(機械学習用パラメータ)
  ```

  `attribute.json`の内容

  ```json
  {
    "index": "1",
    "no": "1.1",
    "pos": "1",
    "param1": "p1_1",
    "param2": "p1_2",
    "param3": "p1_3"
  }
  ````

* ディレクトリ階層をパースして、CSVファイルを作成  
  上記変換ステップの逆順で実行する

## 動作条件

* python >= 3.8

## インストール

※ 本パッケージは、仮想環境を作成して実行することを推奨します。

* PyPI

```bash
pip install convoc
```

* Gitlab Package Registory

```bash
pip install convoc --index-url https://__token__:<your_personal_token>@gitlab.com/api/v4/projects/37267127/packages/pypi/simple
```

GitLabは、プライベートリポジトリであるため、インストール時に、個人のアクセストークン(`your_personal_token`)を使用してインストールしてください。

## Usage

### CSVからディレクトリ階層へ

#### Format

```python
def csv2dir(csvfile: str, level: int, root_dir: str, *, isheader: bool = False, attribute_type: str = "json") -> List[Dict[str, str]]:
```

#### Input

* `csvfile (str)`: CSVファイル
* `level (int)`: 作成するディレクトリ階層の指定
* `root_dir (str)`: ディレクトリを作成する親ディレクトリ
* `isheader (bool, optional)`: CSVのヘッダー情報有無
* `attribute_type (str, optional)`: 属性ファイル(e.g. attribue.json)のファイルタイプ。json/toml/yaml/csv/textをサポート。

#### Output

* 読み込んだcsvファイルのコンテンツ

#### Exsample

```python
from convoc import csv2dir

# csv file to be read
read_filepath = 'csv/sample.csv'

# Convert directory from csv
csv_contents = csv2dir(csvfile=read_filepath, level=2, target_path="target", is_header=True)

# loaded csv file (type: list)
print(csv_contents)
```

### ディレクトリ階層からcsvへ

#### Format

```python
def dir2csv(root_dir: str, output: str, *, level: Optional[int] = None, attribute_type: str = "json") -> List[Any]:
```

#### Input

* `root_dir (str)`: 読み込み対象となるルートディレクトリ
* `output (str)`: 変換したcsvの格納先ディレクトリ
* `level (Optional[int], optional)`: csvに書き出す階層の指定
* `attribute_type (str, optional)`: 読み取り対象の属性ファイル

#### Output

* 変換後のディレクトリのリスト

#### Exsample

```python
# exsample.py
from convoc import dir2csv

# Convert directory structure to csv
result = dir2csv(root_dir='target', output='csv/recover.csv', level=2)

# Output list of converted directories
# At the same time, csv/recover.csv is generated.
print(result)
```

