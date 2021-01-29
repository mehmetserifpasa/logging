## logging
Basit bir şekilde loglama işlemi yapar.

## Usage
Dosyayı kendi dosyamıza import ediyoruz.
```
from logging import log
```

Bir log dosyası oluşturuyoruz.
```
logging = log()
logging.Create("example.log")
```

Hangi türde loglama yapacağımızı ve logun hangi mesajı yazmasını istediğimizi bu şekilde veriyoruz. Örnek kullanım:
```
logging("info", "Failed to connect with local 0xf8b12a Client process!")
logging("error", "Failed to connect with local 0xf8b12a Client process!")
logging("critical", "Failed to connect with local 0xf8b12a Client process!")
logging("trace", "Failed to connect with local 0xf8b12a Client process!")
logging("fatal", "Failed to connect with local 0xf8b12a Client process!")
logging("warning", "Failed to connect with local 0xf8b12a Client process!")
```
#### Output:
![Ekran Resmi 2021-01-29 20 01 10](https://user-images.githubusercontent.com/25556230/106305995-78f24500-626e-11eb-857b-e5b13baff031.png)

#### IDE regex
```
^\s*w(arn(ing)?)?\s*$
^\s*i(nfo)?\s*$
^\s*t(race)?\s*$
^\s*c(ritical)?\s*$
...
```
