# Syobopy

Syobopy is [Syoboi Calender](http://cal.syoboi.jp/) API wrapper for python


## Usage

  from Syobopy.client import Client

  client = Client()

### db.php

#### ProgLookup

http://cal.syoboi.jp/db.php?Command=ProgLookup

ex).

  $ client.db.proglookup(ChID=6, StTime="20170702_080000-20170702_083000")

    {
      '@id': '406976',
      'LastUpdate': '2017-06-11 00:15:30',
      'PID': '406976',
      'TID': '4309',
      'StTime': '2017-07-02 08:00:00',
      'StOffset': '0',
      'EdTime': '2017-07-02 08:30:00',
      'Count': '37',
      'SubTitle': 'None',
      'ProgComment': 'None',
      'Flag': '0',
      'Deleted': '0',
      'Warn': '0',
      'ChID': '6',
      'Revision': '1',
      'STSubTitle': 'White knightの覚悟！'
    }


#### TitleLookup

http://cal.syoboi.jp/db.php?Command=TitleLookup

ex).

  $ client.db.titlelookup(TID=3306)

    {
      'Code': '200',
      'Message': None,
      'TitleItem': {
        '@id': '4309',
        'TID': '4309',
        'LastUpdate': '2017-07-02 17:16:58',
        'Title': '仮面ライダーエグゼイド',
        'ShortTitle': 'None',
        'TitleYomi': 'かめんらいだーえぐぜいど',
        'TitleEN': 'KAMEN RIDER EX-AID',
        'Comment': '*リンク
          -[[テレビ朝日 http://www.tv-asahi.co.jp/ex-aid/]]
          -[[東映 http://www.toei.co.jp/tv/ex-aid/]]
          -[[twitter https://twitter.com/toei_EXAID]]

          *スタッフ
          :原作:石ノ森章太郎
          :スーパーバイザー:小野寺章(石森プロ)
          :チーフプロデューサー:佐々木基(テレビ朝日)
          :プロデューサー:大森敬仁(東映)、菅野あゆみ(テレビ朝日)
          :脚本:高橋悠也
          :監督:中澤祥次郎
          :音楽:ats-、清水武仁、渡辺徹
          :クリーチャーデザイン:寺田克也
          :特撮監督:佛田洋
          :アクション監督:宮崎剛(ジャパンアクションエンタープライズ)
          :制作:テレビ朝日、東映、ADK

          *オープニングテーマ「EXCITE」
          :作詞:三浦大知、岡嶋かな多
          :作曲:岡嶋かな多、Carpainter
          :編曲:Carpainter、UTA
          :歌:三浦大知
          :使用話数:#2～#11、#13～#14、#25～
          -#1、#15、#19～#24はオープニングテーマなし、エンディングテーマとして使用
          -#12、#16～#18はオープニングテーマなし

          *挿入歌「Let's Try Together」
          :作詞:BOUNCEBACK & kenko-p
          :作曲・編曲:日比野裕史
          :歌:仮面ライダーGIRLS
          :使用話数:#13、#14

          *挿入歌「Wish in the dark」
          :作詞:森月キャス、Mio Aoyama
          :作曲:清水武仁
          :編曲:渡辺徹
          :歌:貴水博之
          :使用話数:#17

          *挿入歌「PEOPLE GAME」
          :作詞:高橋悠也
          :作曲:大西克巳
          :編曲:渡辺徹、ats-
          :歌:ポッピーピポパポ(松田るか)
          :使用話数:#24、#25、#26

          *挿入歌「Real Game」
          :作詞:田澤孝介
          :作曲:都啓一
          :編曲・歌:Rayflower
          :使用話数:#29

          *挿入歌「JUSTICE」
          :作詞:Mio Aoyama
          :作曲:夏海
          :編曲:貴水博之、渡辺徹
          :歌:貴水博之
          :使用話数:#33

          *挿入歌「Time of Victory」
          :作詞:桑谷実沙、森月キャス
          :作曲:桑谷実沙
          :編曲:ats-
          :歌:仮面ライダーGIRLS
          :使用話数:#36

          *キャスト
          :宝生永夢:飯島寛騎
          :鏡飛彩:瀬戸利樹
          :花家大我:松本享恭
          :仮野明日那／ポッピーピポパポ:松田るか
          :檀黎斗:岩永徹也
          :九条貴利矢:小野塚勇人(劇団EXILE)
          :西馬ニコ:黒崎レイナ
          :パラド:甲斐翔真
          :グラファイト:町井祥真
          :天ヶ崎恋:小手伸也
          :鏡灰馬:博多華丸
          :日向恭太郎:野村宏伸
          :檀正宗:貴水博之
          **声の出演
          :ライダーガシャット:影山ヒロノブ
          :ナレーション:諏訪部順一',
        'Cat': '4',
        'TitleFlag': '0',
        'FirstYear': '2016',
        'FirstMonth': '10',
        'FirstEndYear': 'None',
        'FirstEndMonth': 'None',
        'FirstCh': 'テレビ朝日',
        'Keywords': '仮面ライダー,wikipedia:仮面ライダーエグゼイド',
        'UserPoint': '50',
        'UserPointRank': '1448',
        'SubTitles': '*01*I'm a 仮面ライダー！
          *02*天才二人はno thank you?
          *03*BANしたあいつがやってくる！
          *04*オペレーションの名はDash!
          *05*全員集結、激突Crash!
          *06*鼓動を刻めin the heart!
          *07*Some lieの極意！
          *08*男たちよ、Fly high!
          *09*Dragonをぶっとばせ！
          *10*ふぞろいのDoctors!
          *11*Who's黒い仮面ライダー？
          *12*クリスマス特別編 狙われた白銀のXmas!
          *13*定められたDestiny
          *14*We're 仮面ライダー！
          *15*新たなChallenger現る！
          *16*打倒MのParadox
          *17*規格外のBURGSTER?
          *18*暴かれしtruth!
          *19*Fantasyは突然に!?
          *20*逆風からのtake off!
          *21*mysteryを追跡せよ！
          *22*仕組まれたhistory!
          *23*極限のdead or alive!
          *24*大志を抱いてgo together!
          *25*New game起動！
          *26*生存を賭けたplayers
          *27*勝者に捧ぐlove&peace!
          *28*Identityを超えて
          *29*We're 俺!?
          *30*最強VS最強！
          *31*禁断のContinue?
          *32*下されたJudgment!
          *33*Company再編！
          *34*果たされしrebirth!
          *35*Partnerを救出せよ！
          *36*完全無敵のGAMER!
          *37*White knightの覚悟！
          *38*涙のperiod'
        }
    }
