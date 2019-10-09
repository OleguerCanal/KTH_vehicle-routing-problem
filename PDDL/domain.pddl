(define (domain airline)
    (:requirements :typing :fluents)
    (:types city person)

    (:predicates
                (plane-at ?x - city)
                (person-at ?p - person ?x - city)
    )

    (:functions
                (add-distance ?x - city ?y - city)
                (total-distance)
                (time)
                (onboard)
                (seats)
                (add-person ?p -person ?x ?y - city)
    )

    (:action fly :parameters (?x - city ?y - city)
                 :precondition (plane-at ?x)
                 :effect (and (plane-at ?y)
                              (not (plane-at ?x))
                              (increase (total-distance) (add-distance ?x ?y))
                              (decrease (time) 1)
                         )
    )


    (:action board :parameters(?x - city ?p -person)
                   :precondition (and (person-at ?p ?x)
                                      (plane-at ?x)
                                      (>= (- (seats) (onboard)) )
                                 )
                   :effect ()
    )

;    (:action board :parameters (?x - city)
;                   :precondition (and (plane-at ?x)
;                                      (> (- (seats) (onboard)) 0)
;                                      (> (people-at ?x) 0)
;                                 )
;                   :effect (and (when (> (people-at ?x) (- (seats) (onboard)))
;                                      (and (decrease () ()) ())
;                                )
;
;                           )
;    )
    
)
