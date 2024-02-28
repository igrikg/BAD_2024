# Test tasks for "Become A Developer 2024"

--- 
This repository is a test challenge for PortaOne's Become a Developer 2024 program
https://education.portaone.com/

---
# Description

This program can calculate min, max, mean, median,
maximum length of increasing and decreasing sequences (numpy variant
is not include this options) from file or array. 

This python script was tested on Python 3.11. Median calculation uses the
algorithm represented in https://habr.com/ru/articles/346930/

___

# Run
    $ python  main.py -f "10m.txt"

```bazaar
options:
  -h, --help            show this help message and exit
  -f [FILE], --file [FILE]
                        File name, (default: 10m.txt)
  -t {own,numpy}, --type_calculation {own,numpy}
                        type calculation own developed or use numpy (default: own). For use numpy you should install this module.
  -a ARRAY [ARRAY ...], --array ARRAY [ARRAY ...]
                        Array for calculate. If it is defined then the file name is ignore

```

___

# Requirements install ( for test and use with numpy)

    $ pip install -r requirements.txt

---
## Links:

- https://habr.com/ru/articles/346930/ Мой любимый алгоритм: нахождение медианы за линейное время
- https://education.portaone.com/ Навчальний центр PortaOne