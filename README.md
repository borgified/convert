# convert
convert files to utf8

on MacOS:

brew install libmagic

pip3 install filemagic

to run it:

```
./convert.py a.srt
```

the output file will be `a.srt_output`

==============================

bash version

on ubuntu:

apt-get install iconv

```
./srt_convert.sh a.srt
```

the output file will be `a_out.srt`
