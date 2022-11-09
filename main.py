# demo exceptions

import exception_basics.exceptions_basics as exc

exc_basics = exc.exception_basics("Joseph", 36, "male")

print(exc_basics)
print(f"{exc_basics.name}'s driving age ({exc.driving_age}) ratio is: {exc_basics.driving_age_ratio()}")
try:
    print(f"{exc_basics.name}'s lifespan age ({exc.average_lifespan}) ratio is: {exc_basics.lifespan_age_ratio()}")
except exc.ExpectedError as error:
    print(f"an expected error has occurred: {error}")

exc_basics2 = exc.exception_basics(new_age=-1)

print(exc_basics2)
print(f"{exc_basics2.name}'s driving age ({exc.driving_age}) ratio is: {exc_basics2.driving_age_ratio()}")
# no ExpectedError execpt clause within the try-except structure is here to catch the ExpectedError
print(f"{exc_basics2.name}'s lifespan age ({exc.average_lifespan}) ratio is: {exc_basics2.lifespan_age_ratio()}")
