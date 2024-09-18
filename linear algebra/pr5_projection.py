import numpy as np
print("Anshu")
def ofProjection(of_vec, on_vec):
    vec1=np.array(of_vec)
    vec2=np.array(on_vec)
    scalar=np.dot(vec1,vec2)/np.dot(vec2,vec2)
    print("Scalar",scalar)

    project=scalar*vec2
    print("Projection",project)
    return scalar,project
print("\nfirst",ofProjection([1.2,4.3],[3.2,4.0]))
print("\nsecond",ofProjection([1.2,2.1],[2.1,3.3]))