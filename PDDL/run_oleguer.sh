CODE_DIR="$(pwd)/"
cd /home/oleguer/software/Metric-FF-v2.1/
./ff -p $CODE_DIR -o domain.pddl -f problem.pddl -s 4 -w 1
cd $CODE_DIR 