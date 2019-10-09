(define (problem flights)
    (:domain airline)
    (:objects A B C D - city
              g1 g2 - group
              p1 p2 - plane)
    (:init
            ; DISTANCES BETWEEN CITIES
            (= (add-distance A B) 1)
            (= (add-distance B C) 1)
            (= (add-distance A C) 100)

            ; People groups
            (= (group-number g1) 2)
            (group-at g1 A)
            (group-want g1 C)

            (= (group-number g2) 3)
            (group-at g2 B)
            (group-want g2 C)

            ; Planes
            (plane-at p1 A)
            ( = (plane-onboard p1) 0)
            ( = (plane-seats p1) 2)

            (plane-at p2 B)
            ( = (plane-onboard p2) 0)
            ( = (plane-seats p2) 6)


            ; STARTING CONDITIONS
            (= (total-distance) 0)
            (= (time) 40)
            (= (happy-people) 0)    
        )
    (:metric minimize (total-distance))
    ; (:goal (and (<= (time) 0)))
    (:goal (>= (happy-people) 4))
)
