#オーバフローを無視する加算結果から被加数を減算すると加数が復元できることを確認するプログラム

import itertools

# 2つの8要素の配列を作成し、要素に1または0を代入
a = [0, 0, 0, 0, 0, 0, 0, 0]
b = [0, 0, 0, 0, 0, 0, 0, 0]

# 8ビットの加算を全パターン行う
for a in itertools.product([0, 1], repeat=8):
  for b in itertools.product([0, 1], repeat=8):

    # 初期化
    carry = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0]

    # 各ビットに対して加算処理を行う（オーバーフロー無視）
    for j in range(8):
        bit1 = a[7-j]   # array1のビット値
        bit2 = b[7-j]    # array2のビット値
        
        # 加算処理
        sum_bit =  (bit1 + bit2 + carry) % 2
        if bit1 + bit2 + carry >= 2:
          carry = 1
        else:
          carry = 0
        result[7-j] = sum_bit   # 加算結果を格納

    # 各ビットに対して減算処理を行う（オーバーフロー無視）
    # a = result - b

    # 補数表現で-bを実現
    hosuu_pre = [0, 0, 0, 0, 0, 0, 0, 1]
    minas_b = [0, 0, 0, 0, 0, 0, 0, 0]
    
    b_inv = list(b)
    for h in range(8):
      if b_inv[h] == 1:
        b_inv[h] = 0
      elif b_inv[h] == 0:
        b_inv[h] = 1

    minas_carry = 0
    for f in range(8): 
      bit1 = hosuu_pre[7-f]
      bit2 = b_inv[7-f]
      # 加算処理
      minas_sum =  (bit1 + bit2 + minas_carry) % 2
      if bit1 + bit2 + minas_carry >= 2:
          minas_carry = 1
      else:
          minas_carry = 0
      minas_b[7-f] = minas_sum   # 加算結果を格納

    #for j in range(8):
     #   bit1 = result[7-j]   # array1のビット値
      #  bit2 = minas_b[7-j]    # array2のビット値

    # a = result - b
    result_a = [0, 0, 0, 0, 0, 0, 0, 0]
    carry_sub = 0
    for j in range(8):
        bit1_sub = result[7-j]   # array1のビット値
        bit2_sub = minas_b[7-j]    # array2のビット値
        
        # 加算処理
        sum_sub =  (bit1_sub + bit2_sub + carry_sub) % 2
        if bit1_sub + bit2_sub + carry_sub >= 2:
          carry_sub = 1
        else:
          carry_sub = 0
        result_a[7-j] = sum_sub   # 加算結果を格納

    # CMA適用時の加算処理
    #for j in range(8):
     #   bit1 = a[7-j]   # array1のビット値
      #  bit2 = b[7-j]    # array2のビット値
        
        # 加算処理
        # 桁上げ出力は常に0なので加算処理に含めない
       # sum_bit = bit1 or bit2
        #result[7-j] = sum_bit   # 加算結果を格納

    
    # 結果を表示
    #a = list(a)
    if list(a) == result_a:
      print("復号可能")
      print(f"a:           {list(a)}")
      print(f"b:           {list(b)}")
    #print(f"b_inv:      {b_inv}")
    #print(f"mainas_b    {minas_b}")
      print(f"Result:      {result}\n")
      print(f"Result - b = {result_a}\n")
