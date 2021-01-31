%create random numbers and run the simulation
function f = randomizer
    X = randi([1 10000],1,1)
    Y = randi([1 10000],1,1)
    Z = randi([1 100],1,1)
    F = randi([1 10000],1,1)
    BC = randi([3 6],1,2)
    BC1 = BC(1,1)
    BC2 = BC(1,2)
    simu(X,Y,Z,F,BC1,BC2)
end