(define (problem flights)
    (:domain airline)
    (:objects Paris Rome Stockholm NY Amsterdam - city
              g1 g2 g3 g4 g5 g6 g7- group
              p1 p2 p3 - plane)
    (:init
            ; Cities
            (= (city-distance Rome Paris) 2)
            (= (city-distance Rome Stockholm) 4)
            (= (city-distance Paris Stockholm) 3)
            (= (city-distance Paris Rome) 2)
            (= (city-distance Stockholm Rome) 4)
            (= (city-distance Stockholm Paris) 3)
            (= (city-distance Amsterdam NY) 10)
            (= (city-distance NY Amsterdam) 10)
            (= (city-distance NY Stockholm) 14)
            (= (city-distance Stockholm NY) 14)
            (= (city-distance NY Rome) 10)
            (= (city-distance Rome NY) 10)

            ; People groups
            (= (group-number g1) 20)
            (group-at g1 Paris)
            (group-want g1 Rome)

            (= (group-number g2) 30)
            (group-at g2 Stockholm)
            (group-want g2 Amsterdam)

            (= (group-number g3) 50)
            (group-at g3 Stockholm)
            (group-want g3 Paris)

            (= (group-number g4) 15)
            (group-at g4 Rome)
            (group-want g4 NY)

            ; Planes
            (plane-at p1 Stockholm)
            (= (plane-seats p1) 50)

            (plane-at p2 Rome)
            (= (plane-seats p2) 30)
            
            (plane-at p3 NY)
            (= (plane-seats p3) 30)

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
            (= (plane-onboard p3) 0)
            (= (plane-time p1) 0)
            (= (plane-time p2) 0)
            (= (plane-time p3) 0)

            (= (tot-people) 5)
            (= (tot-time) 1)
            (= (deadline) 10000)
            (= (happy-people) 0)    
        )

    (:goal (or
               (forall (?p - plane) (deadline-reached ?p))
               (= (happy-people) (tot-people))
           )
    )
    (:metric minimize (- (/ (happy-people) (tot-time)) ))
)
