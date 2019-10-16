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
            (group-at g2 A)
            (group-want g2 B)

            (= (group-number g3) 1)
            (group-at g3 A)
            (group-want g3 B)

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

            (= (tot-people) 3)
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
