from github3 import login

gh = login('user', password='<pass>')

user_ = gh.me()
# <AuthenticatedUser [sigmavirus24:Ian Stapleton Cordasco]>

print(user_.name)
# Ian Stapleton Cordasco
print(user_.login)
# sigmavirus24
print(user_.followers_count)
# 4

for f in gh.followers():
    print(str(f))

anujtyagi = gh.user('user_')
# <User [kennethreitz:Kenneth Reitz]>

print(user_.name)
print(user_.login)
print(user_.followers_count)

followers = [str(f) for f in gh.followers('anujtyagi')]