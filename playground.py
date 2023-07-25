from app import app, db, User, Pulse, Result, Sample, Test

with app.app_context():
    user = User.query.all()[0]
print(user.email)

with app.app_context():
    pulses = Pulse.query.all()
    for pulse in pulses:
        print(pulse.severity)

with app.app_context():
    samples = Sample.query.all()
    for sample in samples:
        print(sample.id)

with app.app_context():
    results = Result.query.all()
    for result in results:
        print(result.id)

with app.app_context():
    tests = Test.query.all()
    for test in tests:
        print(test.id)

#with app.app_context():
#    pulse = Pulse.query.filter(Pulse.severity=='Low').first()
#    print(pulse.id)

