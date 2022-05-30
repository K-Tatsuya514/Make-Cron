import spacy

nlp = spacy.load('ja_ginza')

# 文境界解析
print('【文境界解析】')
doc = nlp('銀座でランチをご一緒しましょう。今度の日曜日はどうですか。')
for sent in doc.sents:
    print(sent)



# 形態素分割
import ginza
print('\r\n【形態素分割】')
ginza.set_split_mode(nlp, "B")
# ・A：選挙 / 管理 / 委員 / 会
# ・B：選挙 / 管理 / 委員会
# ・C：選挙管理委員会 (デフォルト)
doc = nlp('私は選挙管理委員会です')
for sent in doc.sents:
    for token in sent:
        print(token)





# レンマと品詞の抽出
print('\r\n【レンマと品詞の抽出】')
doc = nlp('第3月曜日の3:15に実行する。')
for sent in doc.sents:
   for token in sent:
       print(
           str(token.i)+', '+ # トークン番号
           token.text+', '+ # テキスト
           token.lemma_+', '+ # レンマ            
           token.pos_+' ,'+ # 品詞
           token.tag_) # 品詞詳細




# 単語間の係り受け解析
print('\r\n【単語間の係り受け解析】')
doc = nlp('銀座でランチをご一緒しましょう。')
for sent in doc.sents:
    for token in sent:
        print(token.text+' ← '+token.head.text+', '+token.dep_)

# グラフ表示
from spacy import displacy
displacy.render(doc, style='dep', jupyter=True, options={'compact':True, 'distance': 90})