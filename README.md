[![image](https://img.shields.io/pypi/v/g2pk.svg)](https://pypi.org/project/g2pk/)
[![image](https://img.shields.io/pypi/l/g2pk.svg)](https://pypi.org/project/g2pk/)
[![image](https://img.shields.io/pypi/pyversions/g2pk.svg)](https://pypi.org/project/g2pk/)

# g2pK: g2p module for Korean

g2p means a task that converts graphemes to phonemes. Hangul, the main script for Korean, is phonetic, but the pronunciation rules are notoriously complicated.
So it is never easy to learn how to read a text in Korean. That's why g2p is necessary in various nlp tasks like TTS.
. There's a open source g2p library for Korean, [KoG2P](https://github.com/scarletcho/KoG2P). It is 
simple and works well, but I think we need a better one. Please read through the following section (main features and usage)
to understand the philosophy of g2pK and how to use g2pK. We know it is not perfect in present. 
That's one of the reasons your contributions are more than welcome.

## Requirements
* python >= 3.6
* jamo
* [python-mecab-ko](https://github.com/jonghwanhyeon/python-mecab-ko)
* nltk

## Installation
```
pip install g2pk
```

## Main features & Usage
* Returns text as it is pronounced, keeping punctuations.
```
>>> from g2pk import G2p
>>> g2p = G2p()
>>> g2p("어제는 날씨가 맑았는데, 오늘은 흐리다.")
어제는 날씨가 말간는데, 오느른 흐리다.
```
* Determines pronunciation seeing context, thanks to Mecab, a morphological analyzer.
In the following example, note that the first and second 신고 are pronounced differently.
```
>>> g2p("신을 신고 얼른 동사무소에 가서 혼인 신고 해라")
시늘 신꼬 얼른 동사무소에 가서 호닌 신고 해라
```
* Returns two types of results, that is, prescriptive (default) and descriptive (with the option `descriptive=True`) pronunciation.
For example,  josa 의 is pronounced 의 in principle, but in real life, it is often pronounced 에.
Also, 계 is much more often pronounced 게. 
```
>>> sent = "나의 친구는 계산이 아주 빠르다"
>>> g2p(sent)
나의 친구는 계사니 아주 빠르다
>>> g2p(sent, descriptive=True)
나에 친구는 게사니 아주 빠르다
```
* This distinction becomes more obvious if you set `group_vowels=True`.
In contemporary colloquial speech, some vowels are hard to distinguish from each other.
For example, in the example below, the vowel ㅒ is normalized to ㅖ.
```
>>> sent = "저는 예전에 그 얘기를 들은 적이 있습니다"
>>> g2p(sent)
저느 녜저네 그 얘기를 드른 저기 읻씀니다
>>> g2p(sent, group_vowels=True)
저느 녜저네 그 예기를 드른 저기 읻씀니다
```
* By default, it returns the standard Korean script, where letters are assembled to form a syllable.
 If you set `to_syl=False`,  however, it returns Hangul letters or jamo. This can be useful for many applications like speech synthesis.
\*Depending on the font you are using, the two results below may look the same, but actually they are not.
```
>>> sent = "어제는 날씨가 맑았는데, 오늘은 흐리다."
>>> g2p(sent)
어제는 날씨가 말간는데, 오느른 흐리다.
>>> g2p(sent, to_syl=False)
어제는 날씨가 말간는데, 오느른 흐리다.
```
* English words in alphabets are converted into Hangul. 
This is possible due to [cmu pronouncing dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict).
```
>>> sent = "그 사람은 좀, old school 같아"
>>> g2p(sent)
그 사라믄 좀, 올드 스쿨 가타
```
* Arabic numbers are spelled out to their context.
 Note that the first 12 is pronounced 열두, whereas the second 12 is pronounced 십이.
```
>>> sent = "지금 시각은 12시 12분입니다"
>>> g2p(sent)
지금 시가그 녈두시 시비부님니다
```
* It is natural that rules can NOT cover every single case. Add special idioms to `idioms.txt`.
* If you set `verbose=True`, you will see the conversion processes with relevant information.
```
>>> sent = "학교에 갔다 와서, 엄마가 해 주신 밥을 먹었다."
>>> g2p(sent, verbose=True)
학교에 갔다 와서, 엄마가 해 주신 밥을 먹었다. -> 학꾜에 갔다 와서, 엄마가 해 주신 밥을 먹었다.
 제23항　받침 'ㄱ(ㄲ, ㅋ, ㄳ, ㄺ), ㄷ(ㅅ, ㅆ, ㅈ, ㅊ, ㅌ), ㅂ(ㅍ, ㄼ, ㄿ, ㅄ)' 뒤에 연결되는 'ㄱ, ㄷ, ㅂ, ㅅ, ㅈ'은 된소리로 발음한다.
-> 국밥[국빱], 깎다[깍따], 넑받이[넉빠지], 삯돈[삭똔]
-> 닭장[닥짱], 칡범[칙뻠], 뻗대다[뻗때다], 옷고름[옫꼬름]
-> 있던[읻떤], 꽂고[꼳꼬], 꽃다발[꼳따발], 낯설다[낟썰다]
-> 밭갈이[받까리], 솥전[솓쩐], 곱돌[곱똘], 덮개[덥깨]
-> 옆집[엽찝], 넓죽하다[넙쭈카다], 읊조리다[읍쪼리다], 값지다[갑찌다] 
학꾜에 갔다 와서, 엄마가 해 주신 밥을 먹었다. -> 학꾜에 갇따 와서, 엄마가 해 주신 밥을 먹얻따.
 제9항　받침 'ㄲ, ㅋ', 'ㅅ, ㅆ, ㅈ, ㅊ, ㅌ', 'ㅍ'은 어말 또는 자음 앞에서 각각 대표음 [ㄱ, ㄷ, ㅂ]으로 발음한다.
-> 닦다[닥따], 키읔[키윽], 키읔과[키윽꽈], 옷[옫]
-> 웃다[욷따], 있다[읻따], 젖[젇], 빚다[빋따]
-> 꽃[꼳], 쫓다[쫃따], 솥[솓], 뱉다[밷따]
-> 앞[압], 덮다[덥따]
제23항　받침 'ㄱ(ㄲ, ㅋ, ㄳ, ㄺ), ㄷ(ㅅ, ㅆ, ㅈ, ㅊ, ㅌ), ㅂ(ㅍ, ㄼ, ㄿ, ㅄ)' 뒤에 연결되는 'ㄱ, ㄷ, ㅂ, ㅅ, ㅈ'은 된소리로 발음한다.
-> 국밥[국빱], 깎다[깍따], 넑받이[넉빠지], 삯돈[삭똔]
-> 닭장[닥짱], 칡범[칙뻠], 뻗대다[뻗때다], 옷고름[옫꼬름]
-> 있던[읻떤], 꽂고[꼳꼬], 꽃다발[꼳따발], 낯설다[낟썰다]
-> 밭갈이[받까리], 솥전[솓쩐], 곱돌[곱똘], 덮개[덥깨]
-> 옆집[엽찝], 넓죽하다[넙쭈카다], 읊조리다[읍쪼리다], 값지다[갑찌다] 
학꾜에 갇따 와서, 엄마가 해 주신 밥을 먹얻따. -> 학꾜에 갇따 와서, 엄마가 해 주신 바블 머걷따.
 제13항　홑받침이나 쌍받침이 모음으로 시작된 조사나 어미, 접미사와 결합되는 경우에는, 제 음가대로 뒤 음절 첫소리로 옮겨 발음한다.
-> 깎아[까까], 옷이[오시], 있어[이써], 낮이[나지]
-> 꽂아[꼬자], 꽃을[꼬츨], 쫓아[쪼차], 밭에[바테]
-> 앞으로[아프로], 덮이다[더피다] 
```


## References

If you use our software for research, please cite:

```
@misc{park2019g2pk,
  author = {Park, Kyubyong},
  title = {g2pK},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Kyubyong/g2pk}}
}
```
