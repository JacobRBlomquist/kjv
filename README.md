# WoG (Word of God)

Read the Word of God from your terminal

Forked from [https://github.com/bontibon/kjv.git](https://github.com/bontibon/kjv.git) but with the "Apocrypha", "Book of Mormon", "Pearl of Great Price", and
'Doctrine & Covenants' added.


## Usage

    usage: ./wog [flags] [reference...]

      -l      list books
      -W      no line wrap
      -h      show help

      Reference types:
          <Book>
              Individual book
          <Book>:<Chapter>
              Individual chapter of a book
          <Book>:<Chapter>:<Verse>[,<Verse>]...
              Individual verse(s) of a specific chapter of a book
          <Book>:<Chapter>-<Chapter>
              Range of chapters in a book
          <Book>:<Chapter>:<Verse>-<Verse>
              Range of verses in a book chapter
          <Book>:<Chapter>:<Verse>-<Chapter>:<Verse>
              Range of chapters and verses in a book

          /<Search>
              All verses that match a pattern
          <Book>/<Search>
              All verses in a book that match a pattern
          <Book>:<Chapter>/<Search>
              All verses in a chapter of a book that match a pattern
## Example
```sh
./wog Ether:12:27
```

```
Ether 
12:27   And if men come unto me I will show unto them their weakness. I give
        unto men weakness that they may be humble; and my grace is sufficient
        for all men that humble themselves before me; for if they humble
        themselves before me, and have faith in me, then will I make weak things
        become strong unto them.
```

## Build

WoG can be built by cloning the repository and then running make:

    git clone https://github.com/JacobRBlomquist/WoG.git
    cd WoG
    sudo make install

## License

Public domain
