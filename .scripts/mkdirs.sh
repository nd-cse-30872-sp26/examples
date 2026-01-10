#!/bin/sh

for i in $(seq 0 12); do
    n=$(printf "%02d" $i)
    mkdir reading$n

    cat > reading$n/README.md <<EOF
# Reading $n
EOF
done

for c in $(seq 0 23); do
    n=$(printf "%02d" $c)
    mkdir challenge$n
    cat > challenge$n/README.md <<EOF
# Challenge $n
EOF
done

for c in $(seq 1 4); do
    n=$(printf "%02d" $c)
    mkdir contest$n
    cat > contest$n/README.md <<EOF
# Contest $n
EOF
done

for c in $(seq 1 2); do
    n=$(printf "%02d" $c)
    mkdir external$n
    cat > external$n/README.md <<EOF
# External $n
EOF
done

for c in $(seq 1 2); do
    n=$(printf "%02d" $c)
    mkdir interview$n
    cat > interview$n/README.md <<EOF
# Interview $n
EOF
done
