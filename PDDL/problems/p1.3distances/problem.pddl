(define (problem flights)
    (:domain airline)
    (:objects A B C D E - city
              g1 g2 g3 g4 g5 - group
              p1 p2 - plane)
    (:init
            ; Cities
            (= (city-distance A B) 4)
            (= (city-distance A C) 4)
            (= (city-distance A D) 7)
            (= (city-distance A E) 8)
            (= (city-distance B A) 4)
            (= (city-distance B C) 2)
            (= (city-distance B D) 7)
            (= (city-distance B E) 6)
            (= (city-distance C A) 4)
            (= (city-distance C B) 2)
            (= (city-distance C D) 5)
            (= (city-distance C E) 5)
            (= (city-distance D A) 7)
            (= (city-distance D B) 7)
            (= (city-distance D C) 5)
            (= (city-distance D E) 5)
            (= (city-distance E A) 8)
            (= (city-distance E B) 6)
            (= (city-distance E C) 5)
            (= (city-distance E D) 5)

            ; People groups
            (= (group-number g1) 2)
            (group-at g1 B)
            (group-want g1 E)

            (= (group-number g2) 1)
            (group-at g2 B)
            (group-want g2 A)

            (= (group-number g3) 2)
            (group-at g3 D)
            (group-want g3 A)
            
            (= (group-number g4) 1)
            (group-at g4 D)
            (group-want g4 E)
            
            (= (group-number g5) 2)
            (group-at g5 E)
            (group-want g5 A)
            
            ; Planes
            (plane-at p1 B)
            (= (plane-seats p1) 5)

            (plane-at p2 D)
            (= (plane-seats p2) 3)

            ; Starting Conditions
            (= (group-time g1) 0)
            (= (group-time g2) 0)
            (= (group-time g3) 0)
            (= (group-time g4) 0)
            (= (group-time g5) 0)
            (= (plane-onboard p1) 0)
            (= (plane-time p1) 0)
            (= (plane-onboard p2) 0)
            (= (plane-time p2) 0)

            (= (tot-people) 8)
            (= (deadline) 10000)
            (= (happy-people) 0)
            (= (tot-flights) 0)
            (= (tot-time) 0)
            (= (obj) 1)
            (= (one) 1)
        )

    (:goal (or
               (= (happy-people) (tot-people))
           )
    )
    (:metric minimize (tot-time))
)
