import ita
d=ita.array.make1d(4)
Data=ita.array.make1d(81)

def save_r(o):
 for i in range(3):
      d[i]=d[i+1]
 d[3]=o
 te=0
 for i in range(4):
   if d[i]=='g':
     te+=2*3**i
   elif d[i]=='c':
     te+=1*3**i
 Data[te]+=1
  
def largest_n(a):
  l=0
  n=0
  for i in range(len(a)):
   if l<a[i]:
    l=a[i]
    n=i
  return(n)
  
def janken_j(a,b):
 if (a,b)==('g','c') or (a,b)==('c','p') or (a,b)==('p','g'):
   return('勝ち')
 elif a==b:
   return('あいこ')
 else:
   return('負け') 


def janken():
 win=0
 lose=0
 game=0
 a=0
 print('何をしたいか入力するか、次の手をg、c、pで入力してね＞＞')
 while a==0:
   b=input()
   if b=='end':
    print('プログラムを終わります。バイバイ')
    a=1
   elif b=='g' or b=='c' or b=='p':
    save_r(b)
    print('処理が完了しました')
    print('続けて入力が可能です。何をしたいか入力するか、次の手をg、c、pで入力してね＞＞')
   elif b=='game':
     print('僕の手を準備しています・・・')
     te_=0
     for i in range(1,4):
       if d[i]=='g':
        te_+=2*3**(i-1)
       elif d[i]=='c':
        te_+=1*3**(i-1)
     l=largest_n([Data[te_],Data[te_+27],Data[te_+54]])
     if l==2:
       t='パー'
       t_='p'
     elif l==1:
       t='グー'
       t_='g'
     else:
       t='チョキ'
       t_='c'
     print('僕の手は準備完了です。あなたの手をg、c、pで入力して下さい＞＞')
     w=0
     while w==0:
      o=input()
      if o=='g' or o=='c' or o=='p':
       if janken_j(t_,o)=='あいこ':
        print('僕の手は'+t+'だからあいこだね')
       else:
        if janken_j(t_,o)=='勝ち':
         win+=1
        else:
         lose+=1
        print('僕の手は'+t+'だから'+'僕の'+janken_j(t_,o)+'だね') 
       w=1
      else:
       print('正しく入力をしないといけませんよ。正しく入力してください＞＞')
     print('今回の試合のデータを保存しています・・・')
     game+=1
     save_r(o)
     print('保存が完了しました。また遊んでね')
     print('続けて入力が可能です。何をしたいか入力するか、次の手をg、c、pで入力してね＞＞')
   elif b=='result':
     print('僕の戦績を表示します。')
     if game==0:
      print('まだ試合をしていませんね・・・「game」と入力すれば僕と試合が出来ますよ。')
     else:
      print('試合数',game,'回中・・・')
      print('勝ち：',win,'回')
      print('負け：',lose,'回')
      print('引き分け：',game-win-lose,'回')
      rate=(win*100)/game
      if rate<10:
       print('勝率',rate,'%です。あなたはとてもランダムな手を出せてます。')
      elif rate<50:
       print('勝率',rate,'%です。少し手ごわいですね・・・')
      elif rate<90:
       print('勝率',rate,'%です。')
      else:
       print('勝率',rate,'%です。')
      print('何をしたいか入力するか、次の手をg、c、pで入力してね＞＞')
   elif b=='rate_next':
     te_=0
     for i in range(1,4):
       if d[i]=='g':
        te_+=2*3**(i-1)
       elif d[i]=='c':
        te_+=1*3**(i-1)
     s=Data[te_+54]+Data[te_+27]+Data[te_]
     if s!=0:
      print('グーを出す確率',(Data[te_+54]*100)/s,'%')
      print('チョキを出す確率',(Data[te_+27]*100)/s,'%')
      print('パーを出す確率',(Data[te_]*100)/s,'%')
     else:
      print('グーを出す確率',1/3,'%')
      print('チョキを出す確率',1/3,'%')
      print('パーを出す確率',1/3,'%')      
     print('何をしたいか入力するか、次の手をg、c、pで入力してね＞＞')    
   else:
     print('正しく入力をしないといけませんよ。正しく入力してください＞＞')
     
janken()
