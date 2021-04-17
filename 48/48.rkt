#lang racket

(define (self_powers_sum n)
  (if (= n 1) 1 
      (+ (expt n n) 
         (self_powers_sum (- n 1)))))

(define (last_digits num digits)
  (last_digits_aux num digits 0))

(define (last_digits_aux num digits index)
  (if (= digits 0) 0 
      (+ (*(remainder num 10) 
           (expt 10 index)) 
         (last_digits_aux (quotient num 10) (- digits 1) (+ index 1)))))


(last_digits (self_powers_sum 1000) 10)
