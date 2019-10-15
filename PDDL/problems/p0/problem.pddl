(define (problem flights)
    (:domain airline)
    (:objects A B C D - city
              g1 g2 g3 g4 g5 - group
              p1 - plane)
    (:init
            ; Cities
            (= (city-distance A B) 1)
            (= (city-distance A C) 1)
            (= (city-distance A D) 1)
            (= (city-distance B A) 1)
            (= (city-distance B C) 1)
            (= (city-distance B D) 1)
            (= (city-distance C A) 1)
            (= (city-distance C B) 1)
            (= (city-distance C D) 1)
            (= (city-distance D A) 1)
            (= (city-distance D B) 1)
            (= (city-distance D C) 1)

            ; People groups
            (= (group-number g1) 1)
            (group-at g1 A)
            (group-want g1 B)

            (= (group-number g2) 1)
            (group-at g2 B)
            (group-want g2 C)

            (= (group-number g3) 1)
            (group-at g3 B)
            (group-want g3 C)

            (= (group-number g4) 1)
            (group-at g4 C)
            (group-want g4 A)

            (= (group-number g5) 1)
            (group-at g5 C)
            (group-want g5 B)

            ; Planes
            (plane-at p1 B)
            (= (plane-seats p1) 1000)

            ; Starting Conditions
            (= (group-time g1) 0)
            (= (group-time g2) 0)
            (= (group-time g3) 0)
            (= (group-time g4) 0)
            (= (group-time g5) 0)
            (= (plane-onboard p1) 0)
            (= (plane-time p1) 0)

            (= (tot-people) 5)
            (= (tot-time) 1)
            (= (deadline) 10000)
            (= (happy-people) 0)    
            (= (tot-flights) 0)
        )

    (:goal (or
               ;(forall (?p - plane) (deadline-reached ?p))
               ;(= (happy-people) (tot-people))
               (= (tot-flights) 10)
           )
    )
    (:metric minimize (- (happy-people)))
   ; (:metric minimize (- (happy-people) (tot-flights)))
)
