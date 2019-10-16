(define (domain airline)
    (:requirements :typing :fluents)
    (:types city group plane)

    (:predicates
                ; Planes
                (plane-at ?p - plane ?x - city)

                ; People groups
                (group-at ?g - group ?x - city)
                (group-want ?g - group ?y - city)
                (group-in-plane ?g - group ?p - plane)
                (group-just-unboarded ?g - group ?p - plane)
                (deadline-reached ?p - plane) ; This plane can't fly anymore
    )

    (:functions
                (city-distance ?x ?y - city)  ; Distance between cities
                
                (group-number ?g - group)  ; Number of people in group
                (group-time ?g - group) ; Group stopwatch
                (group-flights-count ?g - group) ; How many times group ?g was unboarded

                (plane-seats ?p - plane)  ; Number of seats in place
                (plane-onboard ?p - plane) ; Number of group in plane
                (plane-time ?p - plane) ; Plane stopwatch

                ; Global
                (obj)
                (zero)
                (one)
                (deadline)
                (happy-people)
                (tot-people)
                (tot-time)
                (tot-flights)
    )

    (:action fly :parameters (?p - plane ?x ?y - city)  ; Fly plane p from city x to city y
                 :precondition (and (plane-at ?p ?x)
                                    (not (deadline-reached ?p))
                               )
                 :effect (and (plane-at ?p ?y)
                              (not (plane-at ?p ?x))
                              (increase (plane-time ?p) (city-distance ?x ?y))
                              (increase (tot-time) (city-distance ?x ?y))
                              (when (>= (plane-time ?p) (deadline)) (deadline-reached ?p))
                              (increase (tot-flights) 1)
                         )
    )

    (:action board :parameters(?g - group ?p - plane ?x - city)  ; Board group g at plane p in city x
                   :precondition (and (not (deadline-reached ?p))
                                      (group-at ?g ?x)
                                      (not (group-want ?g ?x))
                                      (not (group-just-unboarded ?g ?p))
                                      (plane-at ?p ?x)
                                      (>= (-(plane-seats ?p) (plane-onboard ?p)) (group-number ?g))
                                )
                   :effect (and (increase (plane-onboard ?p) (group-number ?g))
                                (not (group-at ?g ?x))
                                (group-in-plane ?g ?p)
                                (when (> (group-time ?g) (plane-time ?p))
                                      (assign (plane-time ?p) (group-time ?g))
                                )
                            )
    )

    (:action unboard :parameters(?g - group ?p - plane ?x - city)  ; Unboard group g from plane p in city x
                   :precondition (and (group-in-plane ?g ?p)
                                      (plane-at ?p ?x)
                                 )
                   :effect (and (decrease (plane-onboard ?p) (group-number ?g))
                                (group-at ?g ?x)
                                (group-just-unboarded ?g ?p)
                                (not (group-in-plane ?g ?p))
                                (when (group-want ?g ?x)
                                    (increase (happy-people) (group-number ?g))
                                )
                                (assign (group-time ?g) (plane-time ?p))
                            )
    )    
)
