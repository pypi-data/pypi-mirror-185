# TuiTse-TsuSin

[![PyPI version](https://badge.fury.io/py/TuiTse-TsuSin.svg)](https://badge.fury.io/py/TuiTse-TsuSin)
[![Build Status](https://travis-ci.org/i3thuan5/TuiTse-TsuSin.svg?branch=master)](https://travis-ci.org/i3thuan5/TuiTse-TsuSin)

|M̄-tio̍h|Tio̍h|
|-|-|
|![圖片](https://user-images.githubusercontent.com/6355592/102592756-e62e9880-414e-11eb-9daf-5146905ab3e2.png)|![圖片](https://user-images.githubusercontent.com/6355592/102593010-44f41200-414f-11eb-8576-8280dff555f4.png)|


這包套件是為著leh整理台語漢字、羅馬字對照語料，掠出一句台語文伊漢字kah羅馬字tó-uī對無齊。主要是一字一字去對，看ta̍k字有合[教典用字](https://github.com/i3thuan5/kau3-tian2_iong7-ji7)--bô；mā會用得換做家己sù-sī ê 用字判斷。

## Tàu/Installation
```
pip install TuiTse-TsuSin
```

## Iōng/Usage
```python
from tuitse import kiamtsa
from tuitse.html import tuitse_html

kiatko = tuitse_html(kiamtsa('雞蛋', 'ke-nn̄g'))
```
對齊結果html生做按呢：
```html
<ruby>
  <rb>ke</rb><rt>雞</rt>
  <rb>-</rb><rt></rt>
  <rb class='fail'>nn̄g</rb><rt class='fail'>蛋</rt>
</ruby>
```

![圖片](https://user-images.githubusercontent.com/6355592/102592756-e62e9880-414e-11eb-9daf-5146905ab3e2.png)

CSS `.fail` 會記得寫寫--leh。
```css
ruby .fail {
   color: red;
}
```

##### Ka-tī kuat-tīng html/Only get the result of alignment
```python
from tuitse import kiamtsa

kiatko = kiamtsa('雞蛋', 'ke-nn̄g')
```
是傳一份json轉--來，生做按呢：
```
[
    ('雞', 'ke', 1, True), ('蛋', 'nn̄g', 2, False)
]
```
##### Ka-tī phuànn-tuàn jī ū tio̍h--bô/Custom comparison
有時仔咱想欲kā一寡情形放水，像講地名「基隆 ke-lâng」ê「基 ke」。咱ē-īng-eh家己判。
###### Siá hâm-sik/Custom function
```python
from tuitse import kiamtsa
from tuitse.html import tuitse_html

pangtsui = (lambda _x: True)

tuitse_html(kiamtsa('基隆','ke-lâng', hamsik_tsitji_ubo=pangtsui))
```
###### Khí āu-tâi/Django admin
提醒，這法度限定Django專案。自動tī Django admin註冊用字表，uì後台一字一字管理啥物字hōo過。

settings.py
```python
INSTALLED_APPS = [
 ...
 'django.contrib.sites',
 '用字',
 ]
```
好勢！像下底按呢用。
```python
from tuitse import kiamtsa
from tuitse.html import tuitse_html

from 用字.models import 用字表

tuitse_html(kiamtsa('基隆','ke-lâng', pio=用字表))
```

## Bôo-tsoo/Module
* tuitse._kiamtsa.py
```python
def kiamtsa(hanji, lomaji, hamsik_tsitji_ubo=None, pio=建議)
```

