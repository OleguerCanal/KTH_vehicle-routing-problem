(define (domain airline)
    (:requirements :typing :fluents)
    (:types city group plane)

    (:predicates
                ; Planes
                (plane-at ?p -plane ?x -city)
                (plane-done ?p -plane)  ; True when plane cant fly any more (due to lack of time)

                ; People groups
                (group-at ?g -group ?x -city)
                (group-want ?g -group ?y -city)
                (group-in-plane ?g -group ?p -plane)
                (group-just-unboarded ?g -group ?p -plane)
    )

    (:functions
                (city-distance ?x ?y -city)  ; Distance between cities
                
                (group-number ?g -group)  ; Number of people in group
                (group-time ?g -group) ; Group stopwatch

                (plane-seats ?p -plane)  ; Number of seats in place
                (plane-onboard ?p -plane) ; Number of group in plane
                (plane-time ?p -plane) ; Plane stopwatch

                ; Global
                (max-time)
                (total-distance)
                (obj)
                (zero)
                (one)
                (deadline)
                (happy-people)
    )

    (:action fly :parameters (?p -plane ?x ?y -city)  ; Fly plane p from city x to city y
                 :precondition (and (plane-at ?p ?x)
                                (< (plane-time ?p) (max-time))
                                )
                 :effect (and (plane-at ?p ?y)
                              (not (plane-at ?p ?x))
                              (increase (total-distance) (city-distance ?x ?y))
                              (increase (plane-time ?p) (city-distance ?x ?y))
                         )
    )

    (:action board :parameters(?g -group ?p -plane ?x -city)  ; Board group g at plane p in city x
                   :precondition (and (group-at ?g ?x)
                                      (plane-at ?p ?x)
                                      (not (group-want ?g ?x))
                                      (not (group-just-unboarded ?g ?p))
                                      (>= (-(plane-seats ?p) (plane-onboard ?p)) (group-number ?g))
                                )
                   :effect (and (increase (plane-onboard ?p) (group-number ?g))
                                (not (group-at ?g ?x))
                                (group-in-plane ?g ?p)
                                ; (= (plane-time ?p) (max (plane-time ?p) (group-time ?g)))
                                (when (>= (group-time ?g) (plane-time ?p))
                                    (assign (plane-time ?p) (group-time ?g)))  ; Update time
                            )
    )


    (:action unboard :parameters(?g -group ?p -plane ?x -city)  ; Unboard group g from plane p in city x
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
