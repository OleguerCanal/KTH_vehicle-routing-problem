(define (domain airline)
    (:requirements :typing :fluents)
    (:types city group plane)

    (:predicates
                (plane-at ?p -plane ?x -city)
                (group-at ?g -group ?x -city)
                (group-want ?g -group ?y -city)
                (group-in-plane ?g -group ?p -plane)
                (group-just-unboarded ?g -group ?p -plane)
    )

    (:functions
                (add-distance ?x ?y -city)  ; Distance between cities
                (group-number ?g -group)  ; Number of people in group
                (plane-seats ?p -plane)  ; Number of seats in place
                (plane-onboard ?p -plane) ; Number of group in plane

                (total-distance)
                (time)  ; TODO(oleguer) This should be plane time
                (happy-people)
    )

    (:action fly :parameters (?p -plane ?x ?y -city)  ; Fly plane p from city x to city y
                 :precondition (plane-at ?p ?x)
                 :effect (and (plane-at ?p ?y)
                              (not (plane-at ?p ?x))
                              (increase (total-distance) (add-distance ?x ?y))
                              (decrease (time) 1)
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
                                    (increase (happy-people) (group-number ?g)))
                            )
    )    
)
