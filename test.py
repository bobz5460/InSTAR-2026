from OMPython import OMCSessionZMQ

omc = OMCSessionZMQ()

# Define a simple Modelica model: x decreases over time.
loaded = omc.sendExpression("""
loadString("
model SimpleModel
  Real x(start=1, fixed=true);
equation
  der(x) = -x;
end SimpleModel;
")
""")

if not loaded:
    raise RuntimeError(omc.sendExpression("getErrorString()"))

# Run from time 0 to 5 seconds.
result = omc.sendExpression("simulate(SimpleModel, stopTime=5)")

if not result["resultFile"]:
    raise RuntimeError(omc.sendExpression("getErrorString()"))

# Read x at the end of the simulation.
x = omc.sendExpression("val(x, 5)")
print("x at 5 seconds:", x)  # Approximately 0.00674