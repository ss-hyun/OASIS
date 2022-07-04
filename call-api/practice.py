import jpype
import json

key = "d37b8b723965a806f02a19e9a9d69963"
classpath = 'kobis-opcl-rest-v1.0.jar'
jpype.startJVM(
    jpype.getDefaultJVMPath(),
    "-Djava.class.path={classpath}".format(classpath=classpath),
    convertStrings=True,
)
rest_pkg = jpype.JPackage('kr.or.kobis.kobisopenapi.consumer.rest')
rest_class = rest_pkg.KobisOpenAPIRestService
kobisAPI = rest_class(key)

daily = kobisAPI.getDailyBoxOffice(True, "20211115", "1", "N", "K", None)
jo = json.loads(daily)

print(daily)

page = 1
while True:
    mvlist = kobisAPI.getMovieList(
        True, str(page), "10", None, None, "2021", None, None, None, None, None)
    ls = json.loads(mvlist)
    if not ls["movieListResult"]["totCnt"]:
        break
    print(mvlist)
    page += 1


# for i in jo.items():
#     print(i[0])
#     for j in i[1].items():
#         print(j)
