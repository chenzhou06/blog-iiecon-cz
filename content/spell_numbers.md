Title: Spell Numbers
Author: Chen Zhou
Date: 2015-11-07 22:17
Category: Programming
Tags: programming, racket

There is a very interesting challenge in
[Project Euler](https://projecteuler.net/problem=17), which requires
you to spell out every number between 1 and 1000 inclusively and count
the number of letters in their words. For example, for number `342`, the
result is `"three hundred and forty-two"` and it contains 23 letters
(whitespace and hyphens are not included).

Today I implemented a very restricted solution which can only handle
four-digits numbers, but it can be extended to more complicated cases
very easily. As far as I am a novice at using the Racket language, the
code below may do not follow its conventional style.

Let's start with three lists of strings from which we will extract
corresponding words.

```{.scheme}
(define ones '("zero" "one" "two" "three"
               "four" "five" "six" "seven" "eight" "nine"))
(define teens
  '("ten" "eleven" "twelve" "thirteen" "fourteen" "fifteen"
    "sixteen" "seventeen" "eighteen" "nineteen"))
(define tys
  '("twenty" "thirty" "forty" "fifty" "sixty" "seventy" "eighty" "ninety"))
```

In the code above, `ones` contains numbers from 0 to 9. Then, we can
easily handle the base condition---one-digit numbers. For a number
`num` we just need to extract the `num`th item in the list of `ones`.

```{.scheme}
(define (speak-digit num)
  ;; 0 <= num < 9
  (list-ref ones num))

(speak-digit 5)
;; "five"

```

Upon the one-digit situation, we can step into a more complex
condition---two-digits numbers, in which we should handle two main
sub-situations: First, the numbers from 11 to 19 is spelled
irregularly; Second, for numbers which are multiples of ten, we should
not append a `"zero"` to their spelling.

```{.scheme}
(define (speak-two-digits num)
  ;; num: 10~99
  (cond
    [(or (< num 10) (> num 99)) #f]
    [(< num 20) (list-ref teens (- num 10))]
    [else (let ([ten-digit (quotient num 10)]
                [one-digit (remainder num 10)])
            (if (zero? one-digit)
                (list-ref tys (- ten-digit 2))
                (string-append (list-ref tys (- ten-digit 2)) " "
                               (speak-digit one-digit))))]))

```

Then, combining two functions above leads us to the solution to spell all
positive numbers with two digits. If `num` is less than 10, then we
use `speak-digit` to spell a digit. If `num` contains two digits, we
spell it with `speak-two-digits`. The name of function
`speak-under-two-digits` is improperly named, actually it does not just
spell numbers "under" two digits, it should spell numbers have exactly
two digits as well.

```{.scheme}
(define (speak-under-two-digits num)
  (if (< num 10)
      (speak-digit num)
      (speak-two-digits num)))


(speak-under-two-digits 55)
;; "fifty five"
```

Now, two-digits situation is handled, we can advance to the more
challenging situation---three digits. Functions above will save a lot
of work for us here. We can split a number with three digits into two
parts, one part is the number at its hundred position, another is the
rest digits which can be dealt with
`speak-under-two-digits`. Attention! There is a pitfall when a number
is an exact multiple of 100 which have no "rest digits" at all.

```{.scheme}
(define (speak-three-digits num)
  ;; num: 100~999
  (cond
    [(or (< num 100) (> num 999)) #f]
    [else (let ([hundred-digit (quotient num 100)]
                [last-two-digits (remainder num 100)])
            (if (zero? last-two-digits)
                (string-append (speak-digit hundred-digit)
                               " hundred")
                (string-append (speak-digit hundred-digit)
                               " hundred and "
                               (speak-under-two-digits last-two-digits))))]))

```

You may have noticed if a number is out of range, the
`speak-*-digit(s)` functions would return a `#f`. Of course there is
better methods to throw an error, but a `#f` is good enough for this tiny
practice.

Also, we now can handle any numbers with three digits at most by
combining `speak-under-two-digits` and `speak-three-digits`.

```{.scheme}
(define (speak-under-three-digits num)
  (if (< num 100)
      (speak-under-two-digits num)
      (speak-three-digits num)))

(speak-under-three-digits 555)
;; "five hundred and fifty five"
```

With a similar procedure, our method can be easily extended to four
digits situation.

```{.scheme}
(define (speak-four-digits num)
  (cond
    [(or (< num 1000 ) (> num 9999)) #f]
    [else (let ([thousand-digit (quotient num 1000)]
                [rest-digits (remainder num 1000)])
            (if (zero? rest-digits)
                (string-append (speak-digit thousand-digit)
                               " thousand")
                (string-append (speak-digit thousand-digit)
                               " thousand "
                               (speak-under-three-digits rest-digits))))]))

(define (speak-under-four-digits num)
  (if (< num 1000)
      (speak-under-three-digits num)
      (speak-four-digits num)))

```

Finally, with a very functional-styled `foldl`, I construct a function
`count-letters` which first split a string into a list of
words by whitespace, then count how many letters each word has, in the
end return the sum of them.

```{.scheme}
(define (count-letters sentence)
  (foldl (λ (word acc) (+ (string-length word) acc))
         0
         (string-split sentence)))

```

The answer is about to come. We map `speak-under-four-digits` to
numbers from 1 to 1000 to spell out every number in between, then
count letters in each outcome and sum them all.

```{.scheme}
(foldl (λ (words acc) (+ (count-letters words) acc))
       0
       (map speak-under-four-digits (range 1 1001))) ; 21124

```

After all the effort, we have figured out there are 21124 letters if we
spell out all numbers from 1 to 1000.
