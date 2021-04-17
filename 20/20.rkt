#lang racket

(define (factorial n)(if (< n 2) 1 (* n (factorial(- n 1)))))

(define (sum_digits n base) (if (= n 0) 0 (+ (remainder n base) (sum_digits (quotient n base)))))

(sum_digits (factorial 100 10))

