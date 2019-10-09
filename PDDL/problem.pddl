(define (problem flights)
    (:domain airline)
    (:objects Stockholm Paris Rome Berlin - city
              p1 p2 - person)
    (:init
            ; DISTANCES BETWEEN CITIES
            (= (add-distance Stockholm Berlin) 3)
            (= (add-distance Berlin Rome) 2)
            (= (add-distance Rome Paris) 1)
            (= (add-distance Paris Rome) 1)
            (= (add-distance Paris Stockholm) 4)
            
            ; STARTING CONDITIONS
            (= (total-distance) 0)
            (= (seats) 5)
            (= (time) 40)
            (= (people-at Stockholm) 10)
            (= (people-at Rome) 0)
            (plane-at Stockholm))
            
    (:metric minimize (total-distance))
    (:goal (and (<= (time) 0)))
)
