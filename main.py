from fastapi import FastAPI
from routers import student, guardian, placement   # this imports the modules
# then use the router objects inside them

app = FastAPI(title="School Management API")

app.include_router(student.router)
app.include_router(guardian.router)
app.include_router(placement.router)   # <-- this works only if placement.py defines `router`

from routers import student, guardian, placement, status

app.include_router(student.router)
app.include_router(guardian.router)
app.include_router(placement.router)
app.include_router(status.router)

from routers import student, guardian, placement, status, profile

app.include_router(student.router)
app.include_router(guardian.router)
app.include_router(placement.router)
app.include_router(status.router)
app.include_router(profile.router)


from routers import student, guardian, placement, status, profile, integration

app.include_router(student.router)
app.include_router(guardian.router)
app.include_router(placement.router)
app.include_router(status.router)
app.include_router(profile.router)
app.include_router(integration.router)

from routers import student, guardian, placement, status, profile, integration, reporting

app.include_router(student.router)
app.include_router(guardian.router)
app.include_router(placement.router)
app.include_router(status.router)
app.include_router(profile.router)
app.include_router(integration.router)
app.include_router(reporting.router)


from routers import student, guardian, placement, status, profile, integration, reporting, dashboard

app.include_router(student.router)
app.include_router(guardian.router)
app.include_router(placement.router)
app.include_router(status.router)
app.include_router(profile.router)
app.include_router(integration.router)
app.include_router(reporting.router)
app.include_router(dashboard.router)
