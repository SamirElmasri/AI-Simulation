function f = simu(X,Y,Z,F,BC1,BC2)

    %geometry creation
    gm = multicuboid(X,Y,Z);
    model = createpde('structural','static-solid');
    model.Geometry = gm;
    
    %create material properties
    structuralProperties(model,'YoungsModulus',200e9,'PoissonsRatio',0.3);
    
    %set boundary conditions and loads
    structuralBC(model,'Face',[BC1,BC2],'Constraint','fixed');
    structuralBoundaryLoad (model,'Face',2,'SurfaceTraction',[0;0;F]);
    
    %create mesh and solve
    mesh = generateMesh(model);
    result = solve(model);
    
    %extract vertecies + nodes coordinates + displacement values
    vertices = gm.vertexCoordinates(1:gm.NumVertices);
    ver = []
    for i = 1:8
        ver = [ver,vertices(i,:)]
    end
    node = transpose (mesh.Nodes);
    dis = result.Displacement.uz;
    vermatrix = repmat(ver,length(dis),1)
    forcevec = repmat(F,length(dis),1)
    BCvec = repmat ([BC1,BC2],length(dis),1)
    disnode = cat(2,node,vermatrix,forcevec,BCvec,dis);
    
    %save output
    format = '.csv'
    filename = string([X,Y,Z,F,BC1,BC2])
    str = strjoin(filename,',')
    file = append(str,format)
    writematrix(disnode,file) 
    
end

