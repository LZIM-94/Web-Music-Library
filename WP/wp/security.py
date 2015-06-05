

USERS = {'admin':'password',
          'foo':'bar'}
GROUPS = {'admin':['group:editors'], 'foo':['group:editors']}

def groupfinder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
