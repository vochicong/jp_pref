# JP Pref.
> Japan prefecture names and codes


## Install

`pip install jp_pref`

## How to use

```python
from jp_pref.prefecture import *
```

or

```python
from jp_pref.prefecture import df, name2code, code2name
```

### Dataframe

Dataframe of prefecture names and codes

```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>short_name</th>
    </tr>
    <tr>
      <th>code</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>北海道</td>
      <td>北海</td>
    </tr>
    <tr>
      <th>2</th>
      <td>青森県</td>
      <td>青森</td>
    </tr>
    <tr>
      <th>3</th>
      <td>岩手県</td>
      <td>岩手</td>
    </tr>
    <tr>
      <th>4</th>
      <td>宮城県</td>
      <td>宮城</td>
    </tr>
    <tr>
      <th>5</th>
      <td>秋田県</td>
      <td>秋田</td>
    </tr>
    <tr>
      <th>6</th>
      <td>山形県</td>
      <td>山形</td>
    </tr>
    <tr>
      <th>7</th>
      <td>福島県</td>
      <td>福島</td>
    </tr>
    <tr>
      <th>8</th>
      <td>茨城県</td>
      <td>茨城</td>
    </tr>
    <tr>
      <th>9</th>
      <td>栃木県</td>
      <td>栃木</td>
    </tr>
    <tr>
      <th>10</th>
      <td>群馬県</td>
      <td>群馬</td>
    </tr>
    <tr>
      <th>11</th>
      <td>埼玉県</td>
      <td>埼玉</td>
    </tr>
    <tr>
      <th>12</th>
      <td>千葉県</td>
      <td>千葉</td>
    </tr>
    <tr>
      <th>13</th>
      <td>東京都</td>
      <td>東京</td>
    </tr>
    <tr>
      <th>14</th>
      <td>神奈川県</td>
      <td>神奈川</td>
    </tr>
    <tr>
      <th>15</th>
      <td>新潟県</td>
      <td>新潟</td>
    </tr>
    <tr>
      <th>16</th>
      <td>富山県</td>
      <td>富山</td>
    </tr>
    <tr>
      <th>17</th>
      <td>石川県</td>
      <td>石川</td>
    </tr>
    <tr>
      <th>18</th>
      <td>福井県</td>
      <td>福井</td>
    </tr>
    <tr>
      <th>19</th>
      <td>山梨県</td>
      <td>山梨</td>
    </tr>
    <tr>
      <th>20</th>
      <td>長野県</td>
      <td>長野</td>
    </tr>
    <tr>
      <th>21</th>
      <td>岐阜県</td>
      <td>岐阜</td>
    </tr>
    <tr>
      <th>22</th>
      <td>静岡県</td>
      <td>静岡</td>
    </tr>
    <tr>
      <th>23</th>
      <td>愛知県</td>
      <td>愛知</td>
    </tr>
    <tr>
      <th>24</th>
      <td>三重県</td>
      <td>三重</td>
    </tr>
    <tr>
      <th>25</th>
      <td>滋賀県</td>
      <td>滋賀</td>
    </tr>
    <tr>
      <th>26</th>
      <td>京都府</td>
      <td>京都</td>
    </tr>
    <tr>
      <th>27</th>
      <td>大阪府</td>
      <td>大阪</td>
    </tr>
    <tr>
      <th>28</th>
      <td>兵庫県</td>
      <td>兵庫</td>
    </tr>
    <tr>
      <th>29</th>
      <td>奈良県</td>
      <td>奈良</td>
    </tr>
    <tr>
      <th>30</th>
      <td>和歌山県</td>
      <td>和歌山</td>
    </tr>
    <tr>
      <th>31</th>
      <td>鳥取県</td>
      <td>鳥取</td>
    </tr>
    <tr>
      <th>32</th>
      <td>島根県</td>
      <td>島根</td>
    </tr>
    <tr>
      <th>33</th>
      <td>岡山県</td>
      <td>岡山</td>
    </tr>
    <tr>
      <th>34</th>
      <td>広島県</td>
      <td>広島</td>
    </tr>
    <tr>
      <th>35</th>
      <td>山口県</td>
      <td>山口</td>
    </tr>
    <tr>
      <th>36</th>
      <td>徳島県</td>
      <td>徳島</td>
    </tr>
    <tr>
      <th>37</th>
      <td>香川県</td>
      <td>香川</td>
    </tr>
    <tr>
      <th>38</th>
      <td>愛媛県</td>
      <td>愛媛</td>
    </tr>
    <tr>
      <th>39</th>
      <td>高知県</td>
      <td>高知</td>
    </tr>
    <tr>
      <th>40</th>
      <td>福岡県</td>
      <td>福岡</td>
    </tr>
    <tr>
      <th>41</th>
      <td>佐賀県</td>
      <td>佐賀</td>
    </tr>
    <tr>
      <th>42</th>
      <td>長崎県</td>
      <td>長崎</td>
    </tr>
    <tr>
      <th>43</th>
      <td>熊本県</td>
      <td>熊本</td>
    </tr>
    <tr>
      <th>44</th>
      <td>大分県</td>
      <td>大分</td>
    </tr>
    <tr>
      <th>45</th>
      <td>宮崎県</td>
      <td>宮崎</td>
    </tr>
    <tr>
      <th>46</th>
      <td>鹿児島県</td>
      <td>鹿児島</td>
    </tr>
    <tr>
      <th>47</th>
      <td>沖縄県</td>
      <td>沖縄</td>
    </tr>
  </tbody>
</table>
</div>



### name2code & code2name

都道府県名の文字列、リスト、もしくは pandas series をコードに変換

```python
name2code("東京都")
```




    13



```python
name2code("東京")
```




    13



```python
code2name(13)
```




    '東京都'



```python
name2code(["東京都", "大阪府", "北海道"])
```




    [13, 27, 1]



```python
name2code(["東京", "大阪", "北海"])
```




    [13, 27, 1]



```python
code2name([13, 27, 1])
```




    ['東京都', '大阪府', '北海道']


