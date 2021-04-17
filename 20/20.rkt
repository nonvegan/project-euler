#lang racket

(define (factorial n)(if (< n 2) 1 (* n (factorial(- n 1)))))

(define (sum_digits n) (if (= n 0) 0 (+ (remainder n 10) (sum_digits (quotient n 10)))))

(sum_digits (factorial 100))

