(define (problem flights)
    (:domain airline)
    (:objects A B C D - city
              p1 p2 - people)
    (:init
            ; DISTANCES BETWEEN CITIES
            (= (add-distance A B) 1)
            (= (add-distance A C) 5)
            (= (add-distance C A) 1)
            (= (add-distance B C) 1)
            (= (add-distance C B) 1)
            (= (add-distance B D) 1)
            (= (add-distance C D) 3)

            ; PEOPLE
            (= (people-number p1) 2)
            (people-at p1 A)
            (people-want p1 B)

            (= (people-number p2) 3)
            (people-at p2 C)
            (people-want p2 D)

            
            ; STARTING CONDITIONS
            (= (total-distance) 0)
            (= (seats) 6)
            (= (onboard) 0)
            (= (time) 40)
            (= (happy-people) 0)
            
            (plane-at A))
            
    (:metric minimize (total-distance))
    ; (:goal (and (<= (time) 0)))
    (:goal (>= (happy-people) 4))
)
