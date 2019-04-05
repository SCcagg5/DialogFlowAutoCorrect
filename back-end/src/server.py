from bottle import run, route, get, post, response, request, hook
import time
from returnvalue import ret
from params import check
from dialogflow import dialogflowapi

"""route to test if api is up"""
@get('/test/')
@post('/test/')
def base():
    try:
        params = check.json(request)
    except:
        params = []
    toret = ret(request.route.rule, params)
    return toret.ret()

@post('/correct/')
def base():
    try:
                params = check.json(request)
    except:
                params = []
    toret = ret(request.route.rule, params)

    if not toret.err:
        err = check.contain(params, ["bearer", "exercice"])
        if not err[0]:
            toret.add_error(err[1], err[2])

    if not toret.err:
        df = dialogflowapi(params["bearer"])
        err = df.test(params["exercice"])
        if not err[0]:
            toret.add_error(err[1], err[2])
        else:
            toret.add_data(err[1])

    return toret.ret()


if __name__ == '__main__':
        run(host='0.0.0.0', port=5000)
