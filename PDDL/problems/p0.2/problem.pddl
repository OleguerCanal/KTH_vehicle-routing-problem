(define (problem flights)
    (:domain airline)
    (:objects A B C D - city
              g1 g2 g3 g4 g5 - group
              p1 - plane)
    (:init
            ; Cities
            (= (city-distance A B) 1)
            (= (city-distance B C) 1)
            (= (city-distance A C) 100)

            ; People groups
            (= (group-number g1) 2)
            (group-at g1 A)
            (group-want g1 C)

            (= (group-number g2) 3)
            (group-at g2 B)
            (group-want g2 D)

            ; Planes
            (plane-at p1 C)
            (= (plane-seats p1) 1000)

            ; Starting Conditions
            (= (group-time g1) 0)
            (= (group-time g2) 0)
            
            (= (plane-onboard p1) 0)
            (= (plane-time p1) 0)

            (= (tot-people) 5)
            (= (deadline) 100000)
            (= (happy-people) 0)
            (= (tot-flights) 0)
            (= (obj) 1)
            (= (one) 1)
        )

    (:goal (= (happy-people) (tot-people))
    )
    (:metric minimize (tot-flights))
)
