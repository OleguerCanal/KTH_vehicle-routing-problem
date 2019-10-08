(define (problem flights)
    (:domain airline)
    (:objects Stockholm Paris Rome Berlin Barcelona - city)
    (:init
            ; DISTANCES BETWEEN CITIES
            (= (add-distance Stockholm Berlin) 3)
            (= (add-distance Berlin Rome) 3)
            (= (add-distance Berlin Barcelona) 1)
            (= (add-distance Barcelona Rome) 1)
            (= (add-distance Stockholm Paris) 2)
            (= (add-distance Paris Rome) 4)
            
            ; STARTING CONDITIONS
            (= (total-distance) 0)
            (plane-at Stockholm))
            
    (:metric minimize (total-distance))
    (:goal (plane-at Rome))
)