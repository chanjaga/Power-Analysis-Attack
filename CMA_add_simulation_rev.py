#CMA適用時に
#オーバフローを無視する加算結果から被加数を減算すると加数が復元できるか確認するプログラム
#任意ビット

import itertools
from tqdm import tqdm

count = 0
#ここでビット幅を指定
bit_number = 10
# 2つの8要素の配列を作成し、要素に1または0を代入
a = [0]*bit_number
b = [0]*bit_number

# 任意ビットの加算を全パターン行う
for a in tqdm(itertools.product([0, 1], repeat = bit_number)):
  for b in itertools.product([0, 1], repeat = bit_number):

    # 初期化
    carry = 0
    result = [0]*bit_number

    # CMA適用時の加算処理
    for j in range(bit_number):
        bit1 = a[bit_number -1 -j]   
        bit2 = b[bit_number -1 -j]    
        
        # 加算処理
        # 桁上げ出力は常に0なので加算処理に含めない
        sum_bit = bit1 or bit2
        result[bit_number - 1 -j] = sum_bit   # 加算結果を格納

    # 各ビットに対して減算処理を行う（オーバーフロー無視）
    # a = result - b

    # 補数表現で-bを実現
    hosuu_pre = [0]*bit_number
    hosuu_pre[-1] = 1
    minas_b = [0]*bit_number
    
    b_inv = list(b)
    for h in range(bit_number):
      if b_inv[h] == 1:
        b_inv[h] = 0
      elif b_inv[h] == 0:
        b_inv[h] = 1

    minas_carry = 0
    for f in range(bit_number): 
      bit1 = hosuu_pre[bit_number - 1 -f]
      bit2 = b_inv[bit_number - 1 -f]
      # 加算処理
      minas_sum =  (bit1 + bit2 + minas_carry) % 2
      if bit1 + bit2 + minas_carry >= 2:
          minas_carry = 1
      else:
          minas_carry = 0
      minas_b[bit_number -1 -f] = minas_sum   # 加算結果を格納

    # a = result - bになるかシミュレーション（CMA適用時）
    result_a = [0]*bit_number
    carry_sub = 0
    for j in range(bit_number):
        bit1_sub = result[bit_number - 1 -j]   # array1のビット値
        bit2_sub = minas_b[bit_number -1 -j]    # array2のビット値
        
        # 加算処理
        # 桁上げ出力は常に0なので加算処理に含めない
        sum_sub =  bit1_sub or bit2_sub
        result_a[bit_number -1 -j] = sum_sub   # 加算結果を格納
    
    # 結果を表示
    #a = list(a)
    if list(a) == result_a:
      count += 1
      #print("復号可能")
      #print(f"a:           {list(a)}")
      #print(f"b:           {list(b)}")
      #print("")
      #print(f"b_inv:      {b_inv}")
      #print(f"mainas_b    {minas_b}")
      #print(f"Result:      {result}\n")
      #print(f"Result - b = {result_a}\n")


print(f"復号可能回数:      {count}")
