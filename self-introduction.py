import random
print("profileと入力してください")
x = input()
if x == "profile":
    print("ITスペシャリスト科一年 木村 瑠真 \n 19歳　6/23生まれ　AB型 \n 趣味 ラジオを聴く(ほぼアニラジ)、アニメ \n 特技 サッカー、野球、バスケ、バレー、テニス、卓球 \n 好きな食べもの ラーメン 唐揚げ \n 性格 冷静、好きなこと以外の集中力が皆無、メンタルは強い方")
else:
    print(random.choice(["一番好きなラノベは魔法科高校の劣等生","好きなアイマスのキャラは高坂海美","好きなアニラジは高田憂希・千本木彩花のしゃかりきちゃん","好きなアニメは響けユーフォニアム","好きな声優は上田麗奈","カラオケで得意な曲はX JAPANの紅","ハマっているソシャゲはFGO"]))

