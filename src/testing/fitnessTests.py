import random
def testFuncSimple(func,*args):
    realS = "TODAYWESHALLBETESTINGTHEFITNESSFUNCTIONSWITHAPIECEOFTEXTTHATIHAVEWRITTENWHICHISCLEARLYENGLISHXWESHALLBECOMPARINGTHISTEXTWITHAPIECEOFRANDOMLYGENERATEDEQUALLENGTHTEXT"
    real = [ord(x) - 65 for x in realS]
    fake = random.choices(range(26),k = len(real))
    realScore = func(real,*args)
    fakeScore = func(fake,*args)
    print(func.__name__, "with arguments", args)
    print("Real english score:",realScore)
    print("Fake english score:",fakeScore)
    print("Real is", realScore/fakeScore, "times bigger than the fake")
