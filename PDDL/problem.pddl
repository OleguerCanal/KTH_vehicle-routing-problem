(define (problem flights)
    (:domain airline)
    (:objects A B C D - city
              g1 g2 g3 - group
              p1 p2 p3 - plane)
    (:init
            ; Cities
            (= (city-distance A B) 1)
            (= (city-distance B C) 1)
            (= (city-distance C D) 1)

            ; People groups
            (= (group-number g1) 2)
            (group-at g1 A)
            (group-want g1 C)

            (= (group-number g2) 3)
            (group-at g2 B)
            (group-want g2 C)

            ; Planes
            (plane-at p1 A)
            (= (plane-seats p1) 2)

            (plane-at p2 B)
            (= (plane-seats p2) 5)

            ; Common
            (= (group-time g1) 0)
            (= (group-time g2) 0)
            (= (plane-onboard p1) 0)
            (= (plane-onboard p2) 0)
            (= (plane-time p1) 0)
            (= (plane-time p2) 0)

            (= (tot-people) 5)

            ; Starting Conditions
            (= (total-distance) 0)
            (= (max-time) 40)
            (= (happy-people) 0)    
        )

    (:goal (or
               ;(forall ?p - plane (>= (plane-time ?p) (max-time)))
               (>= (happy-people) (tot-people))
           )
    )
    (:metric minimize (total-distance))
)
