import cadquery as cq
result = cq.Workplane("XY").box(90, 50, 20) \
    .faces(">Z").workplane().hole(10)

if __name__=='__main__':
    show_object(result)