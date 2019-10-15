(define (problem flights)
    (:domain airline)
    (:objects Paris Rome Stockholm - city
              g1 g2 g3 g4 - group
              p1 p2 p3 - plane)
    (:init
            ; Cities
            (= (city-distance Rome Paris) 10)
            (= (city-distance Rome Stockholm) 10)
            (= (city-distance Paris Stockholm) 10)
            (= (city-distance Paris Rome) 10)
            (= (city-distance Stockholm Rome) 10)
            (= (city-distance Stockholm Paris) 10)

            (= (ticket-cost Rome Paris) 110)
            (= (ticket-cost Paris Rome) 90)
            (= (ticket-cost Paris Stockholm) 110)
            (= (ticket-cost Stockholm Paris) 100)
            (= (ticket-cost Stockholm Rome) 80)
            (= (ticket-cost Rome Stockholm) 150)

            ; People groups
            (= (group-number g1) 1)
            (group-at g1 Paris)
            (group-want g1 Rome)

            (= (group-number g2) 1)
            (group-at g2 Stockholm)
            (group-want g2 Rome)

            (= (group-number g3) 1)
            (group-at g3 Stockholm)
            (group-want g3 Paris)

            (= (group-number g4) 2)
            (group-at g4 Rome)
            (group-want g4 Stockholm)

            ; Planes
            (plane-at p1 Stockholm)
            (= (plane-seats p1) 100)

            ; Starting Conditions
            (= (group-time g1) 0)
            (= (group-time g2) 0)
            (= (group-time g3) 0)
            (= (group-time g4) 0)
            (= (group-flights-count g1) 0)
            (= (group-flights-count g2) 0)
            (= (group-flights-count g3) 0)
            (= (group-flights-count g4) 0)
            (= (plane-onboard p1) 0)
            (= (plane-onboard p2) 0)
            (= (plane-time p1) 0)
            (= (plane-time p2) 0)

            (= (tot-people) 5)
            (= (total-distance) 0)
            (= (deadline) 10000)
            (= (happy-people) 0)    
            (= (revenue) 0)
        )

    (:goal (or
               (forall (?p - plane) (deadline-reached ?p))
               (= (happy-people) (tot-people))
           )
    )
    (:metric minimize (- revenue))
Total Cost:11.0
)
