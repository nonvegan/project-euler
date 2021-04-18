#lang racket

(define (num_fraction_square_root_exceeds_denom_counter  n)(num_fraction_square_root_exceeds_denom_counter_aux  n (/ 1 2) 0)) ;; On the procedure num_exceeds_counter_aux, count is 1 step behind the actual fraction value, so we start with the fraction 1/2

(define (num_fraction_square_root_exceeds_denom_counter_aux  n fraction count)(if (= n 0) count  (num_fraction_square_root_exceeds_denom_counter_aux (- n 1) (/ 1 (+ 2 fraction) ) ( + count (update_digits_counter  (+ 1 fraction)))))) ;;counter is 1 iteration behind the current fraction

(define (num_digits_greater_denom? num)(> (n-digits(numerator num))(n-digits(denominator num))))

(define (update_digits_counter fraction)(if (num_digits_greater_denom? fraction) 1 0))

(define (n-digits n)     (cond  
                         ((< n 0) (n-digits (abs n)))
                         ((< n 2) 1)
                         (else   (+(floor (log n 10)) 1) ))) ;;Slight bug when 10^b where b ∈ 3k. ex. (log 1000 10) -> 2.9999999999999996


(num_fraction_square_root_exceeds_denom_counter 1000)