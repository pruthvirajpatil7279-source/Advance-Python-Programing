import gc
import time

# Check garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())

# Create objects
a = []
b = []
a.append(b)
b.append(a)

# Delete references
del a
del b

# Check garbage collector count
print("\nBefore Garbage Collection:")
print(gc.get_count())

# Measure time
start = time.time()

# Perform manual garbage collection
collected = gc.collect()

end = time.time()

print("\nGarbage Collection Results:")
print("Objects Collected:", collected)
print("Time Taken:", end - start, "seconds")

# Check garbage collection status
print("\nGarbage Collection Enabled:", gc.isenabled())