(define (problem flights)
    (:domain airline)
    (:objects A B C - city
              p1 p2 - people)
    (:init
            ; DISTANCES BETWEEN CITIES
            (= (add-distance A B) 1)
            (= (add-distance B C) 1)

            ; PEOPLE
            (= (people-number p1) 2)
            (people-at p1 A)
            (people-want p1 C)

            
            ; STARTING CONDITIONS
            (= (total-distance) 0)
            (= (seats) 5)
            (= (onboard) 0)
            (= (time) 40)
            (= (happy-people) 0)
            
            (plane-at A))
            
    (:metric minimize (total-distance))
    ; (:goal (and (<= (time) 0)))
    (:goal (= (happy-people) 2))
)
