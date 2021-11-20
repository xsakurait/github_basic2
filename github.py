#エンジニアの必須スキル
# 前のバージョンに戻すことで、エラーが起きても安心
# 思わぬ上書きを防止できる
# OSSに参加できる

from typing import Mapping


ワークツリー→ステージ→リポジトリ
git init ローカルリポジトリ作る
git add ステージング(ワークツリーからステージに挙げる）したいファイル
git commit -m(message) ""（変更を（りもーおリポジトリではない）リポジトリに挙げる

git add は土のファイル上げた以下の指定するため必要
git remote add origin url リモートリポジトリ作成、これによりoriginでurlにアクセスできて楽になる
git push github上にコードを上げる
~変更内容確認～
git status 土のファイルを変更したか
git diff リポジトリとワークツリー（パソコンのカレントディレクトリのこと）の差分をチェック（ローカルリポジトリからプルしてきたときに使）
git diff --staged　ローカルリポジトリとステージの差分を見る
git log ローカルリポジトリのコミットされた履歴（変更履歴）確認
q出戻れる
git restore ファイル名　ワークツリーの変更を取り消す（つまりローカルリポジトリに戻す）
git restore 　-staged ファイル名 ステージの変更をワークツリーに戻す

ブランチ
git branch ブランチ名　ブランチ作成
git branch (リモートブランチも確認 git branch -a)ブランチ一覧表示
git switch 切り替えたいブランチ名
git switch -c ブランチ名　ブランチ新規作成してそのブランチに切り替える
git merge 取り込みたいコミットをさすブランチ名　それぞれのブランチがさす変更点（コミット）を取り込む（マージ） 
リモートのブランチを取り込みたいとき　git merge origin/main originをmainに取り込む

コンフリクト　mainブランチでfileAの２行目、aブランチでfileAの２行目
変更したときmergeするとどちらを優先して変更を確定すればいいかわからないのでパソコンエラー

解消方法
fileAの内容
>>>main>>>
<p>a</p>
>>>a>>>
<p>b</p>
----
-や>>>を消してfileAを変更する

# プルリクエスト　commitした変更をgithub上のリモートリポジトリにおｋだったら反映してくださいというお願い
git pull origin main ワークツリーとローカルリポジトリ二もリモートリポジトリの最新情報を反映(git pullでもか)
git fetch　origin ローカルリポジトリだけに反映

pull=fetch+merge
mainブランチにいるときは最新情報にしたいのでpull
ブランチ複数ある時は、fetch+merge

プルリクエスト
mainを最新に更新　ブランチ作成　ファイル修正してコミット
プッシュ　github上でプルリクエスト　コードレビュー　マージ
git remote add origin url 
git pull origin main 
git branch feature
git add .
git commit -m "1commit"
git push origin main
pullrequestタグ押してbase main compare feature(変更したほう)でプル陸作成
コードレビューは右上の緑のボタンのところオスとできる。チームでやらないとできない
下のmergeの緑ボタン押すとできる

